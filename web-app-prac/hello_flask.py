from flask import Flask

app = Flask(__name__)

@app.route('/')#function decorator
def hello() -> str:
    return 'Hello world from Flask!'

app.run()
