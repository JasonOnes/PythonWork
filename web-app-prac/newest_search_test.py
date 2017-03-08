""" latest version of vsearch4web from book Headfirst Python """


from flask import Flask, render_template, request, escape, session
from vsearch import search_word

from freshDBcm import UseDatabase, ConnectionError, CredentialsError#imprts mysyql connector already
from checker import check_logged_in

app = Flask(__name__)
""" data base connection characteristics """
app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'ok',
                           'database': 'vsearchlogDB2', }

def log_request(req: 'flask_request', res: str):
    """ This should log the details of the web request and results into our dB"""
    # conn = mysql.connector.connect(**dbconfig)
    # cursor = conn.cursor() contained within UseDatabase method

    """ The UseDatabase context manager expects a dictionary fo db connection characteristics"""
    with UseDatabase(app.config['dbconfig']) as cursor:#the context manager returns "cursor"
        _SQL = """ insert into log
                   (phrase, letters, ip, browser_string, results)
                   values
                   (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))

app.secret_key = 'YouWillNeverGuess'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return "You are logged in!"

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return "You are now logged out!"



@app.route('/search4', methods=['POST'])#URL
def do_the_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here\'s your results buddy!'
    results = str(search_word(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failied with this error:',str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)
                        #    assigning python variables to their jinja2 counterparts
                # corresponding to the 4 arg values in results.html

#rather than redirect we can simply add more routes to try
@app.route('/')
@app.route('/entry')
@app.route('/taco')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to the Dumbest letter search online!')

# @app.route('/viewlog')
# def view_the_log() ->str:
#     with open('vsearch.log', 'r') as log:
#         contents = log.read()
#         return contents

@app.route('/viewlog')
@check_logged_in
def view_the_log():
    """ display the contents of the log file as a HTML table."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ select phrase, letters, ip, browser_string, results
                       from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results',)
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as err:
        print('Is your databse switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-ID/Password issues. Error:', str(err))
    except SQLError as err:
        print('Maybe your query is queer(y)? Error:', str(err))
    except Exception as err:
        print('Something has gone wrong:', str(err))
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
