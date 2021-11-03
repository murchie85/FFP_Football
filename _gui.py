class gui():
    def __init__(self,screen,width,height,font):
        self.screen       = screen
        self.width        = width
        self.height       = height
        self.font         = font


        self.gameState    = 'ingame'
        self.userInput    = None # Loaded at runtime
        self.running      = True
        self.dt           = 0
        self.gameElapsed  = 0
        self.debugSwitch  = False
        self.mx           = 0
        self.my           = 0



    def debug(self,debugMessage):
        if(self.debugSwitch):
            print(debugMessage)

class fitbaObject():
    """
    takes in sprite classs from utils
    """
    def __init__(self,football):
        self.sprite = football
        self.x      = self.sprite.x
        self.y      = self.sprite.y
        self.w      = self.sprite.w
        self.h      = self.sprite.h
    
    def updateSprite(self,gui):
        self.sprite.x,self.sprite.y = self.x,self.y
        self.sprite.animate(gui)
