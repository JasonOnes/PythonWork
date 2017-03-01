from flask import Flask, render_template

app = Flask(__name__)


@app.route('/searchy_wordy')#URL
def search_word(phrase: str, letters: str) -> set:
    #print(set(letters).intersection(set(phrase)))
    return set(letters).intersection(set(phrase))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the Dumbest letter search online!')

                          
app.run()
