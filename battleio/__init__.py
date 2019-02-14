from battleio import webBrowser
from battleio.webBrowser import GameWebBrowser, GameMode

if __name__ == '__main__':
    webBrowser = GameWebBrowser()
    webBrowser.loadGame()
    
    webBrowser.changeServer('sa')
    webBrowser.startGame(GameMode.PLAY_SOLO)