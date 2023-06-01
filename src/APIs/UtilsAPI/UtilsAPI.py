import random

class UtilsAPI:
    """
    UtilsAPI
    ~~~
    COMPLETE
    """

    @staticmethod
    def get_UserAgent(mode:str='random'):
        """
        COMPLETE
        """
        return random.choice(UtilsAPI.open_UserAgents())

    @staticmethod
    def open_UserAgents():
        """
        COMPLETE
        """
        with open(file='src/User-Agents.txt', mode='r', encoding='UTF8') as f:
            user_agents = [line.strip() for line in f]
            return user_agents