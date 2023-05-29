import os
import requests
import json

class InstagramAPI:
    """
    API class for getting user Profile data from Instagram.
    """
    def __init__(self, username:str) -> None:
        """
        Initialize the InstagramAPI object.

        Args:
            username (str): The username of the Instagram profile.

        Raises:
            FileNotFoundError: If the COOKIE.json file is not found.

        Attributes:
            profile_data (dict): The information of the Instagram User.
        """
        # We get the current script folder name
        script_path = os.path.abspath(__file__)
        script_folder = os.path.dirname(script_path)

        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
        print(url)
        cookie = self.get_cookie(file=f"{script_folder}\\COOKIE.json")
        json = self.get_json(url=url, cookie=cookie)
        self.profile_data = self.get_json_data(json=json)
    
    def send_request(self, url:str, cookie:dict, useCookie:bool=False):
        """
        Send a GET request to the specified URL and return the response.

        Args:
            url (str): The URL to send the request to.
            cookie (dict): The cookie in dict format to access the url.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an error status code.

        Returns:
            Response: The response object.
        """
        cookies = cookie if useCookie else None
        
        response = requests.get(url=url, cookies=cookies)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        return response

    def get_json(self, url:str, cookie:dict=None):
        """
        Send an HTTP GET request to the specified URL and return the response JSON.

        Args:
            url (str): The URL to send the request to.
            cookie (dict): The cookie in dict format to access the url.

        Returns:
            dict: The response JSON.

        Raises:
            InvalidJSONException: If the response cannot be parsed as JSON.
        """
        response = self.send_request(url=url, cookie=cookie)

        try:
            response_JSON = response.json()
            return response_JSON
        except ValueError:
            print("Invalid JSON response received.", ValueError)

    def get_json_data(self, json:dict):
        """
        Extract relevant information from a JSON object and return a dictionary containing the profile information.

        Args:
            json (dict): The JSON object containing the profile information.

        Returns:
            dict: A dictionary containing the extracted profile information.

        Raises:
            KeyError: If any key is missing or inaccessible in the JSON object.

        """
        profile_information = {}

        try:
            user_data = json.get('graphql', {}).get('user', {})
            profile_information['seo_category_info'] = [category[0] for category in json.get('seo_category_infos', [])]
            profile_information['biography'] = user_data.get('biography')
            profile_information['followers'] = user_data.get('edge_followed_by', {}).get('count')
            profile_information['full_name'] = user_data.get('full_name')
            profile_information['has_ar_effects'] = user_data.get('has_ar_effects')
            profile_information['has_clips'] = user_data.get('has_clips')
            profile_information['has_guides'] = user_data.get('has_guides')
            profile_information['has_channel'] = user_data.get('has_channel')
            profile_information['category_name'] = user_data.get('category_name')
            profile_information['is_verified'] = user_data.get('is_verified')
            profile_information['posts_count'] = user_data.get('edge_owner_to_timeline_media', {}).get('count')

            posts_data = user_data.get('edge_owner_to_timeline_media', {}).get('edges', [])
            posts = []

            for node in posts_data:
                post_data = {}

                post_data['accessibility_caption'] = node.get('node', {}).get('accessibility_caption')
                post_data['caption'] = node.get('node', {}).get('edge_media_to_caption', {}).get('edges', [{}])[0].get('node', {}).get('text')
                post_data['post_comments'] = node.get('node', {}).get('edge_media_to_comment', {}).get('count')
                post_data['post_likes'] = node.get('node', {}).get('edge_liked_by', {}).get('count')
                post_data['post_comments_disabled'] = node.get('node', {}).get('comments_disabled')
                post_data['post_taken_at_timestamp'] = node.get('node', {}).get('taken_at_timestamp')

                post_element = {}

                post_element['id'] = node.get('node', {}).get('id')
                post_element['shortcode'] = node.get('node', {}).get('shortcode')
                post_element['dimensions'] = node.get('node', {}).get('dimensions')
                post_element['is_video'] = node.get('node', {}).get('is_video')

                if post_element['is_video']:
                    post_element['video_url'] = node.get('node', {}).get('video_url')
                    post_element['display_url'] = node.get('node', {}).get('display_url')
                else:
                    post_element['display_url'] = node.get('node', {}).get('display_url')
                    post_element['video_url'] = None

                post = [post_element]
                post_children = node.get('node', {}).get('edge_sidecar_to_children', {}).get('edges', [])
                
                for posts_nodes in post_children:
                    post_element = {}

                    post_element['id'] = posts_nodes.get('node', {}).get('id')
                    post_element['shortcode'] = posts_nodes.get('node', {}).get('shortcode')
                    post_element['dimensions'] = posts_nodes.get('node', {}).get('dimensions')
                    post_element['is_video'] = posts_nodes.get('node', {}).get('is_video')

                    if post_element['is_video']:
                        post_element['video_url'] = posts_nodes.get('node', {}).get('video_url')
                        post_element['display_url'] = posts_nodes.get('node', {}).get('display_url')
                    else:
                        post_element['display_url'] = posts_nodes.get('node', {}).get('display_url')
                        post_element['video_url'] = None

                    post.append(post_element)

                posts.append({'post_data': post_data, 'post': post})
                profile_information['posts'] = posts

        except KeyError as e:
            raise KeyError(f"Missing or inaccessible key in JSON object: {e}")

        return profile_information
    
    def get_cookie(self, file:str):
        """
        Reads a JSON file and returns its contents as a Python dictionary.

        Args:
            file (str): The path to the JSON file.

        Raises:
            FileNotFoundError: If the JSON file is not found.
            json.JSONDecodeError: If the JSON file contains invalid syntax.

        Returns:
            dict: The contents of the JSON file as a dictionary.
        """
        try:
            with open(file=file, mode='r', encoding='UTF8') as f:
                data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file '{file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON syntax in file '{file}'.")
        
        return data