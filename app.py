from flask import Flask, session, redirect, flash, request
from flask import render_template, url_for



app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)

