import json

class Utils:
    """
    Utils
    ~~~

    Class with utility functions that can be employed for multiple tasks.

    This class provides a collection of static methods that offer various utility functionalities. These methods can be used across different tasks and scenarios to simplify common operations and enhance code reusability.

    The `Utils` class does not require instantiation and should be accessed directly using the class name. It serves as a convenient container for organizing and categorizing utility functions.

    Available methods:
    - get_json(file: str) -> dict: Read a JSON file and return its contents as a Python dictionary.

    Example usage:
    ```python
    json_data = Utils.get_json('data.json')
    print(json_data)
    ```

    Note:
    - Each method within the `Utils` class is static, meaning they can be called directly on the class without the need for an instance of the class.
    - It is recommended to review the documentation of individual methods for more detailed information on their usage and behavior.
    """
    @staticmethod
    def get_json(file:str) -> dict:
        """
        Read a JSON file and return its contents as a Python dictionary.

        Args:
            file (str): The path to the JSON file.

        Returns:
            dict: The contents of the JSON file as a dictionary.

        Raises:
            FileNotFoundError: If the JSON file is not found.
            json.JSONDecodeError: If the JSON file contains invalid syntax.

        Example:
            >>> json_data = get_json('data.json')
            >>> print(json_data)
            {'key': 'value'}

        This static method reads a JSON file from the specified file path and returns its contents as a dictionary. The function can be used to easily load JSON data into your Python program.

        The function attempts to open the file in read mode and uses the `json.load()` function to parse the JSON contents into a dictionary. If the file is not found, a `FileNotFoundError` is raised. If the JSON file contains invalid syntax, a `json.JSONDecodeError` is raised.

        Example usage:

        ```python
        json_data = get_json('data.json')
        print(json_data)
        ```

        In this example, the function reads the contents of the 'data.json' file and stores it in the `json_data` variable. The contents are then printed, resulting in a dictionary object.

        Note:
        - Make sure the specified file path is correct and the file exists.
        - Verify that the JSON file has valid syntax to avoid `JSONDecodeError` exceptions.
        """
        try:
            with open(file=file, mode='r', encoding='UTF8') as f:
                data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file '{file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON syntax in file '{file}'.")
        
        return data