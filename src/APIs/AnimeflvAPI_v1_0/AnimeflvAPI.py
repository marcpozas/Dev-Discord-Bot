import os
import requests
from bs4 import BeautifulSoup
from ..UtilsAPI import UtilsAPI

class AnimeflvAPI:
    """
    AnimeflvAPI
    ~~~
    COMPLETE
    """

    def __init__(self) -> None:
        self.get_directory()

    def get_directory(self, pagesNumber:int=3):
        """
        COMPLETE
        """
        directory_data = {}
        for pageNumber in range(pagesNumber):
            actual_url = f'https://www3.animeflv.net/browse?page={pageNumber+1}'
            actual_soup = self.get_soup(url=actual_url)
            page_data = self.analyze_soup(soup=actual_soup)
            directory_data += page_data
    
    def analyze_soup(soup:BeautifulSoup):
        """
        COMPLETE
        """
        ul_list_animes = soup.find('ul', class_='ListAnimes')
        li_list_animes = ul_list_animes.find_all('li')
        print(li_list_animes)


    def send_request(self, url:str) -> requests.Response:
        """
        Send a GET request to the specified URL and return the response.

        Args:
            url (str): The URL to send the request to.

        Returns:
            Response: The response object.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an error status code.
        """
        headers = {
            'User-Agent':UtilsAPI.get_UserAgent(mode='random')
        }
        print(headers)
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        return response
    
    def get_soup(self, url:str):
        """
        Create a BeautifulSoup object from the response content of the url sended.

        Args:
            url (str): The url.

        Raises:
            Exception: If an error occurs while creating the BeautifulSoup object.

        Returns:
            BeautifulSoup: The BeautifulSoup object.
        """
        response = self.send_request(url=url)
        
        try:
            soup = BeautifulSoup(response.content, 'lxml')
            return soup
        except Exception as e:
            raise Exception("An error occurred while creating the BeautifulSoup object:", e)

api = AnimeflvAPI()