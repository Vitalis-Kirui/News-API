from flask import render_template
from app import app

#Index route and view function
@app.route('/')
def index():
    """
    View root page function that returns the index page and it's content
    """
    title  = "News Centre. "
    heading = "Welcome to News Centre, A site for all the news from various sources. \nThis page will have all the news outlets/sources"
    return render_template('index.html', title=title, heading=heading)

@app.route('/sources/<source_id>')
def articles(source_id):
    """
    View page function that returns articles page and and its content.
    """
    articles_title = "Articles"
    return render_template("articles.html",id = source_id, articles_title = articles_title)