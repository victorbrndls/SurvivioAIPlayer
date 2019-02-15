import threading
import time


class GameLogger(threading.Thread):

    def __init__(self, webBrowser):
        super().__init__()
        self.webBrowser = webBrowser
    
    def run(self):
        self.waitForGameToStart()
        
        while(self.isAlive()):
            print(self.webBrowser.getPlayerX())
            time.sleep(1)
    
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
