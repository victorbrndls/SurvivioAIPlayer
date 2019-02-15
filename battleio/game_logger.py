import threading
import time
from selenium.common.exceptions import WebDriverException


class GameLogger(threading.Thread):

    def __init__(self, webBrowser):
        super().__init__()
        self.webBrowser = webBrowser
    
    def run(self):
        self.waitForGameToStart()
        
        while(self.isAlive()):
            try:
                print("X: {0}, Y: {1}".format(self.webBrowser.getPlayerX(), self.webBrowser.getPlayerY()))
                time.sleep(1)
            except WebDriverException:  # If the browser is closed this exception is thrown
                print("Closing GameLogger")
                break;
    
    def waitForGameToStart(self):
        '''
        Wait until the game has initialized and the javascript variables are
        available 
        '''
        while(self.webBrowser.hasGameInitialized() is None):
            print("Waiting for the game to initialize...")
            time.sleep(0.5)

    
def init_threads(webBrowser):
    GameLogger(webBrowser).start()
