import json

class Utils:
    """
    COMPLETE
    """
    @staticmethod
    def get_json(file:str):
        """
        COMPLETE
        """
        try:
            with open(file=file, mode='r', encoding='UTF8') as f:
                data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file '{file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON syntax in file '{file}'.")
        
        return data