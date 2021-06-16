#!/usr/bin/python3
""" Using Beautiful Soup to scrape webdata from List of Flowers. By Damian Mercado """

# Import standard libraries
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def grab_flowers_good_response(resp):
    # Returns True if the response seems to be HTML, False otherwise    
    content_type = resp.headerts['Content-Type'].lower()



def grab_flowers(url):
    """ Attempt to get the content at 'url' by making an HTTP Get request. 
        If the content-type of response is some kind of HTML/XML, return the text content, otherwise return None.
        """
    try:
         with closing(get(url, stream=True)) as resp:
             # stream= True means Requests cannot release the connection until closed
             # closing() will close "resp" at the end of this block
             if grab_flowers_good_response(resp):
                 # .content() reads the HTML of the Request object
                 return resp.content
             else:
                 return None
    
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def main():
    request.get('https://florgeous.com/types-of-flowers/')

    print(len(raw_html))

if __name__ == "__main__":
    main()         

