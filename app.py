from flask import Flask, session, redirect, flash, request
from flask import render_template, url_for
from forms import *
from flask_login import login_required, login_manager,login_user,logout_user,login_remembered,LoginManager
import psycopg2
from forms import LoginForm, RegistrationForm
from app import *
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.session_protection = 'strong'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@benso7130@panasonic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = '9f4b5227ab07794dc2b3b390c7951793'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/services')
def services():
    #the services we offer
    
    return render_template('services.html')

@app.route('/contact')
def contact():
    #the contact form as well as the phone number
    return render_template('contact.html')

#the register route
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

#the login route
@app.route('/login',methods=['GET','POST'])
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
#this functions logs out the user in session
def logout():
    session.clear()
    logout_user()
   
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

