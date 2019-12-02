import logging 
import os
import requests 
    
log = logging.getLogger('__name__')

def search_reviews_by_author(author):
    
    """ 
    Queries for reviews by author. 
    Returns list of matching reviews if reviews found, 
    Returns empty list if no reviews, 
    Returns None if error connecting to API
    """

    url = 'https://api.nytimes.com/svc/books/v3/reviews.json'

    KEY = os.environ.get('NYT_API_KEY')
    if not KEY:
        log.warning('No API key provided. Sign up for one at https://developer.nytimes.com')
        return

    log.info(f'Searching for "{author}"')

    params = { 'author': author, 'api-key': KEY }

    try:

        response = requests.get(url, params=params)

        if response.status_code == 200: 
            json_response = response.json()
            review_results = json_response.get('results')
            if review_results is not None:
                log.info(f'Results are: {review_results}')
                return review_results
            else:
                log.warning(f'No results in JSON {json_response}')
        
        else:
            log.warning('Error response from NYT {response.status_code}')

    except Exception as e:
        log.e('Error fetching data from NYT', exc_info=e)
    
