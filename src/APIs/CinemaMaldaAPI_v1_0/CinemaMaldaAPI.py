import requests
from bs4 import BeautifulSoup
import lxml

class CinemaMaldaAPI:
    """
    API class for fetching movie data from Cinema Malda website.
    """
    def __init__(self, url:str="https://www.cinemamalda.com/") -> None:
        """
        Initialize the CinemaMaldaAPI object.

        Args:
            url (str): The URL of the Cinema Malda website. Defaults to "https://www.cinemamalda.com/".

        Attributes:
            movie_data (list): The list of movie data.
        """
        response = self.send_request(url=url)
        soup = self.get_soup(response=response)
        self.movie_data = self.get_movies(soup=soup)
        [print("Movie:", movie, end="\n\n") for movie in self.movie_data]

    def send_request(self, url:str):
        """
        Send a GET request to the specified URL and return the response.

        Args:
            url (str): The URL to send the request to.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an error status code.

        Returns:
            Response: The response object.
        """
        response = requests.get(url=url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response
    
    def get_soup(self, response):
        """
        Create a BeautifulSoup object from the response content.

        Args:
            response (Response): The response object.

        Raises:
            Exception: If an error occurs while creating the BeautifulSoup object.

        Returns:
            BeautifulSoup: The BeautifulSoup object.
        """
        try:
            soup = BeautifulSoup(response.content, 'lxml')
            return soup
        except Exception as e:
            print("An error occurred while creating the BeautifulSoup object:", e)
    
    def get_movies(self, soup):
        """
        Extract movie data from the soup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.

        Returns:
            dict: A dictionary containing the movie data.

        Raises:
            AttributeError: If an error occurs while extracting movie data.
        """
        moviesObject = soup.find('div', class_='movies')
        movies = moviesObject.find_all('a', class_='movie')

        movies_data = []

        try:
            for movie in movies:
                movie_data = {}
                
                # Extract information from the movie element
                title = movie.find('h3').text.strip() if movie.find('h3') else "????"
                image_url = movie.find('img')['data-src'] if movie.find('img')['data-src'] else "????"
                release_status = movie.find('div', class_='day').text.strip() if movie.find('div', class_='day') else "????"
                href = movie['href'] if movie['href'] else "????"

                # Classify the data into a dictionary
                movie_data['title'] = title
                movie_data['image_url'] = image_url
                movie_data['release_status'] = release_status
                movie_data['href'] = href

                # Append the classified movie data
                if movie_data.get('title') != "Cartelera día a día" and movie_data.get('title') != "Tarifas":
                    movies_data.append(movie_data)

        except AttributeError as e:
            print(f"An error occurred while extracting movie data: {e}")
        
        return movies_data

#api = CinemaMaldaAPI()