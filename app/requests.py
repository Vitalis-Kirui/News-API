from app import app
import urllib.request,json
from .models import sources

Source = sources.Sources

#Getting the api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]

def get_sources(source):
    """
    Function to get the json response to our url request
    """
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results =process_results(sources_results_list)

    return sources_results
