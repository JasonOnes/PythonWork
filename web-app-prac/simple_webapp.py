""" testing out control of web access to pages"""


from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return "You are logged in!"

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return "You are now logged out!"

@app.route('/status')
# def check_status():
#     if 'logged_in' in session:
#         return "You are logged in."
#     else:
#         return "You are NOT logged in!" taken care of by decorator!!


@app.route('/')
def hello():
    return "Hello from the simple webapp."

@app.route('/page1')
@check_logged_in #placing check_logged_in anywhere we want controlled access 
def page1():
    return "This is page1."

@app.route('/page2')
@check_logged_in
def page2():
    return "This is page2."

@app.route('/page3')
@check_logged_in
def page3():
    return "This is page3."

if __name__ == '__main__':
    app.run(debug=True)
