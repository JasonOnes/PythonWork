""" Creates a decorated function that checks if user is logged in. """


from flask import session
from functools import wraps

def check_logged_in(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return funct(*args, **kwargs)
        else:
            return "You are NOT logged in!"
    return wrapper
