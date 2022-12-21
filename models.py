from flask_login import login_required, login_manager,login_user,logout_user,login_remembered
from flask_bcrypt import BCrypt
import psycopg2
from forms import LoginForm, RegistrationForm
from app import *
bcrypt = BCrypt()


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        #searching the user by email
        conn = psycopg2.connect(host="localhost", database="users",user="#",password="#")
        cursor = conn.cursor()
        
        conn.execute("SELECT * FROM users WHERE email=%s", (email,))
        result = cursor.fetchone()
        password = bcrypt.generate_password_hash(password)
        
        if not result:
            try:
                cursor.execute("""INSERT INTO users (username, email, password) VALUES (%s, %s, %s), (username, email, password)""")
                #commit to the users database
                conn.commit()
            except:
                flash('something is wrong',"danger")
                return redirect(url_for('register'))
            else:
                flash("Successful Registration", "success")
                cursor.close()
            return redirect(url_for('login'))
        else:
            flash("Your email has already being registered. Please Login","danger")
            cursor.close()
            return redirect(url_for('login'))
    # get the request      
    return render_template('register.html',form=form,title="Register")


@app.route('/login',Methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.is_valid():
        email = form.email.data
        password_candidate = form.password.data
        
        #searching the user by email
        conn = psycopg2.connect(host="localhost", database="users",user="#",password="#")
        cursor = conn.cursor()
        
        conn.execute("SELECT * FROM users WHERE email=%s", (email,))
        account = cursor.fetchone()
        print (account)
        
        if account:
            #check password if is correct/comparing passwords
            password = account['password']
            
            if bcrypt.check_password_hash(password, password_candidate):
                session['email'] =email
                session['logged_in'] = True
                print(session['email'])
                flash("Login successful","success")
                cursor.close()
                return(url_for('recommendation'))
            else:
                cursor.close()
                flash("Login failed, INCORRECT password","danger")
                return render_template('login.html', form=form, title = 'login')
        else:
            # User email doesn't exist
            cursor.close()
            flash('EMAIL not Found, Please Register', 'danger')
            return render_template('register.html', form=form, title='Register')
    return render_template('login.html', form=form, title='login')


@login_required
@app.route("/logout")
#this finctions logs out the user in session
def logout():
    session.clear()
    logout_user()
   
    return render_template('home.html')
