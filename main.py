#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#import in files that I created
from user import *

#Setting up Flask
app = Flask(__name__)

#This function brings the user to the login page.
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        user = User()
        # #Checking to see if the user is in the database.
        flag, not_found, password_no_match = user.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('home'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            if not_found:
                flash('Username not found, maybe sign up!')
            elif password_no_match:
                flash('Password does not match! Maybe sign up!')
    return render_template('login.html', title='Login Page')

#This function will bring the user to the home page.
@app.route('/home')
def home():
    return render_template('home.html')

#This function brings the user to the sign up page.
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Recieving the information from the form from the user.
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        user = User()
        print(password)
        #Encrypting the password
        password, hashed = user.encrypt_pass(password)
        #Adding the user to the database
        user.insert(name, username, hashed)
        #Letting them into the index Page
        return redirect(url_for('home'))
    return render_template('signup.html')

#This function will bring the user to the page to examine the data. 
@app.route('/examine')
def examine():
    return render_template('examine.html')

#This function will take the user to the page to visualize the data.
@app.route('/see')
def see():
   return render_template('see.html') 

#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)