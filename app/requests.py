from app import app
import urllib.request,json
from .models import sources

Source = sources.Sources

#Getting the api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]

def get_sources(category):
    """
    Function to get the json response to our url request
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results =process_results(sources_results_list)

    return sources_results

def process_results(sources_resulting_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    """
    sources_results = []
    for single_source in sources_resulting_list:
        id = single_source.get('id')
        name = single_source.get('name')
        description = single_source.get('description')
        url = single_source.get('url')
        category = single_source.get('category')
        country = single_source.get('country')

        source_object = Source(id, name, description, url, category, country)
        sources_results.append(source_object)

    return sources_results