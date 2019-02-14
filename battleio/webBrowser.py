from selenium import webdriver

from battleio import settings
from enum import Enum

GAME_URL = "https://surviv.io/"

# The moduleRaid is a script used to unpack modules from webpackJsonp
# https://github.com/pixeldesu/moduleRaid
moduleRaidScript = '''
    var raidScript = document.createElement('script');
    raidScript.type= 'text/javascript';
    raidScript.src = 'https://unpkg.com/moduleraid@4.0.1/moduleraid.js';
    document.querySelector('head').append(raidScript);
'''


class GameMode(Enum):
    '''
    PLAY_MODE-NAME = 'id of the button that is clicked to start the game in the 
    respective mode'
    '''
    PLAY_SOLO = 'btn-start-solo'
    PLAY_DUO = 'btn-start-duo'
    PLAY_SQUAD = 'btn-start-squad'


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
        
        print("Loading the game")
        settings.driver.get(GAME_URL)
        self.injectRaidModuleScript()
        
    def _createDriver(self):
        print("Creating the WebDriver")
        settings.driver = webdriver.Firefox(executable_path="D:\\Workspace\\Apps\\DataCrawler\\geckodriver.exe")

    def injectRaidModuleScript(self):
        "Injects the moduleRaid script into the page"
        print("Inject moduleRaid script")
        settings.driver.execute_script(moduleRaidScript)

    def changeServer(self, server):
        '''
        Server:
            'sa': South America
            'na': North America
        '''
        print("Changing server to {0}".format(server))
        settings.driver.execute_script("document.querySelector(\"#server-select-main\").value = '{0}'".format(server))

    # Methods that interact with the game
    def startGame(self, mode):
        '''
        Starts the game in the chosen mode(GameMode)
        '''
        print("Starting the game [{0}]".format(mode))
        settings.driver.find_element_by_css_selector("#" + mode.value).click()
    
