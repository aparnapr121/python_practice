from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import logging
def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def is_a_good_response(resp):
    content_type=resp.headers['Content-Type'].lower()
    return (resp.status_code==200
            and content_type is not None
            and content_type.find('html') > -1
            )

def simple_get(url):
    try:
        with closing(get(url,stream=True)) as resp:
            if is_a_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error(str(e))
        return None

raw_html = simple_get('https://realpython.com/blog/')
print(len(raw_html))
