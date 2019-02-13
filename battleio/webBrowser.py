from selenium import webdriver

from battleio import settings

GAME_URL = "https://surviv.io/"

class GameWebBrowser():
    '''
    This class represents the web browser that opens the game, all information
    from the game is extracted though this class and all information sent to the 
    game is sent though this class
    '''
    
    def __init__(self):
        pass

    def loadGame(self):
        if settings.driver is None:
            self._createDriver()
        
        settings.driver.get(GAME_URL)        
        
    def _createDriver(self):
        settings.driver = webdriver.Firefox(executable_path="D:\\Workspace\\Apps\\DataCrawler\\geckodriver.exe")