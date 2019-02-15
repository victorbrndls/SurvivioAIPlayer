from battleio import webBrowser
from battleio.webBrowser import GameWebBrowser, GameMode

from battleio import information_extractor as IE

if __name__ == '__main__':
    webBrowser = GameWebBrowser()
    webBrowser.loadGame()
    
    webBrowser.changeServer('sa')
    webBrowser.startGame(GameMode.PLAY_SOLO)
    
    IE.init_threads(webBrowser)
    