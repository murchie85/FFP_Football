class gui():
    def __init__(self,screen,width,height,font):
        self.screen       = screen
        self.width        = width
        self.height       = height
        self.font         = font



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


class playerObject():
    """
    takes in playersprite classs from utils
    """
    def __init__(self,playerSprite):
        self.sprite = playerSprite


    def play_selected(self,gui):
        self.sprite.animate(gui)