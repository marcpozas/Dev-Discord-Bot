import requests

class CataasAPI:
    """
    CataasAPI
    ~~~
    
    A Python wrapper for the Cataas API that allows retrieving cat images with optional parameters.
    
    Args:
        url (str, optional): The base URL for the Cataas API. Defaults to "https://cataas.com".
        tag (str, optional): The tag to filter cat images.
        gif (bool, optional): A flag indicating whether to retrieve a GIF image.
        text (str, optional): The text to be displayed on the cat image.
        type_cat (str, optional): The type of cat image (e.g., "jpg", "png").
        filter_cat (str, optional): The filter to apply to cat images.
        width (int, optional): The desired width of the cat image.
        height (int, optional): The desired height of the cat image.

    Attributes:
        generated_cat (str): The URL of the generated cat image.

    Methods:
        - getCat(url: str, tag: str, gif: bool, text: str, type_cat: str, filter_cat: str, width: int, height: int) -> str:
            Construct a URL for retrieving a cat image with optional parameters.

        - get_tags() -> list:
            Returns the list of tags.

        - get_filters() -> list:
            Returns a list of available filters.

        - get_types() -> list:
            Returns a list of available image types.
        
        - send_request(url: str) -> Response:
            Send a GET request to the specified URL and return the response.

        - get_json(url: str) -> dict:
            Send an HTTP GET request to the specified URL and return the response JSON.
    """

    def __init__(self, url:str="https://cataas.com", tag:str=None, gif:bool=None, text:str=None, type_cat:str=None, filter_cat:str=None, width:int=None, height:int=None) -> None:
        """
        Initialize a new instance of the CataasAPI class.

        Args:
            url (str, optional): The base URL for the Cataas API. Defaults to "https://cataas.com".
            tag (str, optional): The tag to filter cat images.
            gif (bool, optional): A flag indicating whether to retrieve a GIF image.
            text (str, optional): The text to be displayed on the cat image.
            type_cat (str, optional): The type of cat image (e.g., "small", "square").
            filter_cat (str, optional): The filter to apply to cat images.
            width (int, optional): The desired width of the cat image.
            height (int, optional): The desired height of the cat image.
        """
        self.generated_cat = self.getCat(url=url, tag=tag, gif=gif, text=text, type_cat=type_cat, filter_cat=filter_cat, width=width, height=height)
    
    def send_request(self, url:str):
        """
        Send a GET request to the specified URL and return the response.

        Args:
            url (str): The URL to send the request to.

        Returns:
            Response: The response object.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an error status code.
        """
        response = requests.get(url=url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        return response

    def get_json(self, url:str):
        """
        Send an HTTP GET request to the specified URL and return the response JSON.

        Args:
            url (str): The URL to send the request to.

        Returns:
            dict: The response JSON.

        Raises:
            ValueError: If the response cannot be parsed as JSON.
        """
        response = self.send_request(url=url)

        try:
            response_JSON = response.json()
            return response_JSON
        except ValueError as e:
            raise ValueError("Invalid JSON response received.") from e

    def getCat(self, url:str, tag:str, gif:bool, text:str, type_cat:str, filter_cat:str, width:int, height:int):
        """
        Construct a URL for retrieving a cat image with optional parameters.

        Parameters:
            url (str): The base URL for the cat API.
            tag (str): The tag to filter cat images.
            gif (bool): A flag indicating whether to retrieve a GIF image.
            text (str): The text to be displayed on the cat image.
            type_cat (str): The type of cat image (e.g., "jpg", "png").
            filter_cat (str): The filter to apply to cat images.
            width (int): The desired width of the cat image.
            height (int): The desired height of the cat image.

        Returns:
            str: The constructed URL for retrieving the cat image.
        """
        tag = tag
        gif = gif
        text = text
        type_cat = type_cat
        filter_cat = filter_cat
        width = width
        height = height

        final_url = f'{url}/cat'

        if tag:
            final_url += f'/{tag}'
        if gif:
            final_url += f'/{gif}'
        if text:
            final_url += f'/says/{text}'
        
        if type_cat or filter_cat or width or height:
            final_url += f'?'
        if type_cat:
            final_url += f'type={type_cat}&'
        if filter_cat:
            final_url += f'fi={filter_cat}&'
        if width:
            final_url += f'width={width}&'
        if height:
            final_url += f'height={height}&'
        
        return final_url.strip('&').strip('/')
    
    def get_tags(self):
        """
        Returns the list of tags.
        """
        tags = ["", "#christmascat", "#scottishfold", "2cats", "4", "@Beardlyness", "Beer", "Belfast", "BelfastMet", "Black", "Box", "Buckley", "Cat", "Cat in a faucet", "Catto", "Chair", "Christmas", "CryptoWorld Cat", "Curious", "Cute", "Dark", "FAT", "Female", "Friends", "Fulgencio", "Going shopping?", "Grumpy", "Hiding", "Lay", "Luz", "Maine Coon", "Male", "Maskcat", "Mimi", "My cat(Mamay(мамай)) bebrik.xyz", "NSFW", "Norwegian", "Norwegian Forest Cat", "Orange", "Outside", "Quantico", "Ragdoll", "Relaxed", "Roar", "Sad", "Scout", "Shhhsh", "Sleepy", "Sniper", "Summer", "Tabby", "Tassilo", "Teeth", "Tired cat", "TorWorld Cat", "Torte", "Torte Tabby", "Trippy", "Weegie", "Wet", "White", "X-MAS", "Yeet", "advent-calendar-2016", "afraid", "alcoholic", "alien", "ange", "angel", "angry", "angry cat", "annilou91", "anoyed", "anstrengend", "approaching", "artist", "asking", "attack", "attention", "attitude", "ava", "baby", "background", "bamgu", "banker", "banzai", "basin", "basket", "bath", "beautiful", "bed", "beer", "beg", "begging", "belly", "belly rubs", "bengal", "big", "big eyes", "big-eyes", "bigfloppa", "bird", "biscuit", "black", "black & white", "black an white", "black and white", "black cat", "blanket", "blep", "blini", "blue", "blur", "blurred", "bombay", "boot", "box", "boxe", "brasileira", "brazilian", "brazilian cat", "bread", "british shorthair", "british-shorthair", "brown", "bubble", "bucket", "bun", "burrito", "burrito-cat", "bw", "cake", "calico", "calvin", "candle", "car", "caracal", "cash", "cat", "cat eyes", "cat face", "cat kneading", "cat meowing", "cat on table", "cat wallpaper", "cat_winston", "cats", "catto", "chair", "chaos", "check", "chonker", "christmas", "clawing", "climb", "close", "closed eyes", "closeup", "clothes", "coat", "color", "colorful", "comfy", "computer", "confused", "cooking", "cool", "costume", "couch", "cow", "cowboy", "crazy", "crazy russian pussycat", "creation", "creeper", "creepy", "crying", "cup", "curiosity", "curious", "curly", "cute", "cute cat", "dancer", "dangerous", "dark", "darkness", "daydreaming", "decorated", "deer", "dentist", "desperate", "destroy", "determined", "devil", "dewey", "dino", "disappointed", "dish", "displeased", "disturbed", "diva", "diving", "dog", "doll", "donut", "door", "doritos", "dreaming", "drinking", "drunk", "duck", "duckling", "duke", "ear", "easter", "eating", "egyptian", "elegant", "elvis", "energy", "engineer", "envious", "evil", "exhausted", "eyes", "face", "falling", "fancy", "fancy cat", "fangs", "fast", "fat", "feather", "feet", "felipe", "feral", "festive", "few", "field", "fierce", "fight", "filthy", "final", "finger", "fire", "fish", "fishbowl", "fit", "flame", "flamingo", "flapper", "flash", "florida", "fluff", "fluffy", "fluffy cat", "flying", "focused", "food", "foot", "forest", "forest cat", "forever", "forgetful", "fountain", "freaky", "friend", "frustrated", "fun", "funny", "funny cat", "fur", "furry", "futuristic", "fuzzy", "fuzzy face", "garden", "garfield", "german", "german cat", "get", "ghost", "giant", "ginger", "glasses", "glowing", "golden", "goodnight", "graceful", "grass", "grateful", "gray", "green", "grooming", "group", "grumpy", "guilty", "guitar", "gus", "hairy", "halloween", "hand", "hanging", "happiness", "happy", "harry", "hat", "head", "headphone", "headphones", "headshot", "healing", "health", "heart", "heavy", "heisenberg", "help", "hide", "high", "hippie", "hipster", "hitler", "hobbit", "hocus pocus", "holding", "holiday", "home", "homemade", "hope", "horn", "horned", "hot", "hug", "hugging", "human", "hungry", "husband", "hybrid", "hyper", "i", "ice", "ice cream", "ice-cream", "imposter", "in pocket", "indian", "indoor", "innocent", "insane", "inside", "instrument", "intense", "intimidating", "intrigued", "invisible", "isolation", "japan", "japanese", "japanese cat", "jealous", "jew", "jewelry", "jogging", "jump", "jumping", "jungle", "junk", "kanye", "karma", "kawaii", "key", "keyboard", "kick", "kid", "kissing", "kitty", "kitty in a box", "kitty-eyes", "kittybox", "kneading", "knife", "knight", "kitten", "kitten in a box", "kitty", "kitty-cat", "kitty-ears", "kitty-eats", "kitty-love", "kitty-ma", "kitty-monster", "kitty-nose", "kitty-paws", "kitty-peek", "kitty-pet", "kitty-plant", "kitty-sleepy", "kitty-soft", "kitty-yawn", "kittylove", "knit", "knockout", "koi", "korea", "korean", "korean cat", "kpop", "kpop cat", "krazy", "lazy", "leaning", "leap", "leaves", "legs", "leopard", "leprechaun", "let's play", "lick", "licking", "lightsaber", "lil", "lion", "lioness", "listening", "little", "live", "lizard", "long hair", "longcat", "looking", "lost", "love", "love cat", "lovely", "lover", "low", "lying", "lying down", "macbook", "magician", "magnificent", "male", "maneki", "maneki-neko", "manga", "mango", "mardi gras", "mask", "master", "max", "meaw", "meal", "meerkat", "meeting", "melting", "memphis", "merlin", "mesmerizing", "mess", "metal", "mew", "mice", "mickey", "milk", "mind", "mine", "minion", "mischievous", "miss you", "mist", "model", "modern", "moody", "moon", "mop", "morning", "mouse", "mouse hunt", "mouth", "moustache", "movie", "mug", "musical", "mysterious", "mystery", "mystic", "mythical", "nails", "napping", "nazi", "neck", "need", "nerd", "nerdy", "new year", "new year's eve", "new year's resolution", "night", "ninja", "noir", "noodle", "norwegian", "nose", "notebook", "nurse", "office", "one", "orange", "outdoor", "paint", "pajamas", "panther", "panting", "parade", "parasol", "party", "passionate", "pathetic", "peace", "peacock", "peek", "peekaboo", "peep", "pen", "pensive", "perfect", "pet", "petting", "phantom", "phone", "piano", "pick", "pickle", "picnic", "picture", "piercing", "pigeon", "pilot", "pink", "pipe", "pita", "play", "playing", "please", "pleased", "plush", "poised", "polar bear", "pole", "polish", "pool", "portrait", "posing", "postcard", "potato", "pounce", "pouncing", "power", "prayer", "precious", "presents", "pretty", "pride", "princess", "profile", "protect", "pumpkin", "puppy", "purr", "purring", "push", "pushing", "quarantine", "queen", "quiet", "rabbit", "radiant", "rain", "rainbow", "rainy", "rambo", "reading", "real", "rebel", "reflection", "refreshing", "relax", "relaxation", "relaxed", "reminder", "rescue", "rest", "resting", "rhino", "ribbon", "rich", "ride", "ring", "river", "roar", "rock", "rooster", "rose", "rough", "round", "royal", "royalty", "rude", "running", "rusty", "sad", "safe", "safety", "saint", "samurai", "sand", "santa", "sassy", "scarf", "scared", "scarfie", "scary", "scientist", "scratch", "scratching", "scream", "screech", "searching", "selfie", "serious", "shadow", "shake", "shark", "sharp", "sheep", "shelter", "shine", "ship", "shirt", "shocked", "shoe", "shooting", "shopping", "short", "short hair", "shot", "shoulder", "shower", "sick", "silly", "silver", "simple", "singer", "singing", "sitting", "skate", "skating", "sketch", "skeleton", "skiing", "skilled", "skinny", "sky", "sleep", "sleeping", "sleepy", "slide", "slippers", "sloth", "slow", "small", "smell", "smile", "smiling", "smoke", "smoky", "snack", "snake", "sneak", "sneaky", "sneezing", "snow", "snowball", "snowflake", "snowman", "snuggle", "so", "soft", "solar", "soldier", "solitude", "song", "sorry", "soul", "space", "spaghetti", "sparkle", "sparkling", "speaker", "speed", "spider", "spinning", "spooky", "spot", "spread", "spring", "squat", "squishy", "stable", "staff", "standing", "star", "starfish", "staring", "startled", "stealing", "steam", "steampunk", "stern", "sticking", "stickout", "sticky", "stinky", "stitch", "stoic", "stone", "stop", "stopping", "storm", "strawberry", "street", "stretch", "stretching", "strike", "striped", "stripy", "strong", "stuck", "study", "stuffed", "stunned", "stylish", "submissive", "sugar", "suit", "summer", "sun", "sunbathing", "sunglasses", "super", "superhero", "surprised", "surreal", "swan", "sweet", "swing", "sword", "tail", "tall", "tanuki", "tattoo", "taxi", "tea", "teacher", "tears", "teddy", "telephone", "tense", "terrible", "texture", "thirsty", "thoughtful", "throne", "thunder", "tidy", "tie", "tiger", "tiger cat", "timid", "tiny", "tired", "toast", "together", "toilet", "tongue", "tool", "top", "torch", "toronto", "tortoise", "touch", "tough", "tower", "toy", "train", "transform", "trap", "travel", "treasure", "treat", "tree", "trick", "trip", "trippy", "trouble", "true", "trust", "tumble", "tunnel", "turkey", "twilight", "twist", "two", "tyrant", "umbrella", "under", "undercover", "understand", "unicorn", "uniform", "unique", "unusual", "up", "upside down", "vacation", "valentine", "vampire", "victory", "view", "vintage", "violet", "visitor", "vogue", "voice", "volunteer", "wait", "wake", "waking up", "walk", "walking", "wall", "wand", "wanderer", "warm", "warrior", "washing", "watch", "water", "watermelon", "wave", "waving", "wealthy", "weird", "welcome", "wet", "whiskers", "whisper", "white", "wide", "wild", "window", "wink", "winter", "witch", "wobble", "wolf", "wonder", "wonderful", "wood", "wool", "work", "world", "worn", "worried", "wound", "wrapped", "wrestling", "wrist", "writing", "yarn", "yawning", "yellow", "yoga", "yoga cat", "yummy", "zebra", "zombie", "zoom"]
        return tags

    def get_filters(self):
        """
        Returns a list of available filters.
        """
        filters = ["blur", "mono", "sepia", "negative", "paint", "pixel"]
        return filters

    def get_types(self):
        """
        Returns a list of available image types.
        """
        types = ["small", "medium", "square", "original"]
        return types