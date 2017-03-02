from flask import Flask, render_template
from vsearch import search_word

app = Flask(__name__)


@app.route('/search4')#URL
def do_the_search()-> set:
    return str(search_word('Whateva I do what I want', 'eiru'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the Dumbest letter search online!')


app.run()
