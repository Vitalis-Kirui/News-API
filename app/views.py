from flask import render_template
from app import app

#Index route and view function
@app.route('/')
def index():
    """
    View root page function that returns the index page and it's content
    """
    title  = "News Centre. "
    heading = "Welcome to News Centre, A site for all the news from various sources"
    return render_template('index.html', title=title, heading=heading)