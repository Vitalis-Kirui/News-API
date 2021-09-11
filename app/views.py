from flask import render_template
from app import app
from .requests import get_sources, get_articles

#Index route and view function
@app.route('/')
def index():
    """
    View root page function that returns the index page and it's content
    """
    title  = "News Centre. "
    heading = "Welcome to News Centre, A site for all the news from various sources. This page will have all the news outlets/sources"

    #Getting the sources
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    tech_sources = get_sources('technology')

    return render_template('index.html', title=title, heading=heading, general = general_sources, sports = sports_sources, business = business_sources, entertainment = entertainment_sources, tech = tech_sources)

@app.route('/sources/<id>')
def articles(id):
    """
    View page function that returns articles page and and its content.
    """
    articles_title = "Articles"
    read_article = get_articles(id)
    # title = f'{read_article.title}'

    return render_template("articles.html", id = id, read_article=read_article, articles_title = articles_title )