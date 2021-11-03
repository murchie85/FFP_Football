class playerSprite():
    def __init__(self,imageFrames):
        self.imageFrames = imageFrames
        self.numFrames   = len(self.imageFrames)
        

        self.framePos    = 0
        self.x           = 0
        self.y           = 0
        self.w           = self.imageFrames[0].get_rect().w
        self.h           = self.imageFrames[0].get_rect().h
        self.direction   = None
        self.frameTime   = 0

    def animate(self,gui,interval=0.2,stop=False):
        """
        animages image every interval (in seconds)
        once image reaches end, it resets to first image
        """

        # Update direction Frames

        if(stop):
            gui.screen.blit(self.imageFrames[0],(self.x,self.y))
            return()
        
        # incremented timer
        self.frameTime += gui.dt/1000
        
        # increment frame when interval reached
        if(self.frameTime>=interval):
            self.framePos  +=1
            self.frameTime  = 0
        
        # wrap image around
        if(self.framePos>=self.numFrames): 
            self.framePos=0
        
        gui.screen.blit(self.imageFrames[self.framePos],(self.x,self.y))




class playerObject():
    """
    takes in playersprite classs from utils
    """
    def __init__(self,playerSprite,x,y,vx,vy):
        self.sprite = playerSprite
        self.x      = x
        self.y      = y
        self.vx     = vx
        self.vy     = vy


    def play_selected(self,gui):

        self.sprite.animate(gui,stop=True)

        # Manage Velocity
        if(gui.userInput.up):    self.y -= self.vy
        if(gui.userInput.down):  self.y += self.vy
        if(gui.userInput.left):  self.x -= self.vx
        if(gui.userInput.right): self.x += self.vx

        if(gui.userInput.up):    self.sprite.animate(gui)
        #if(gui.userInput.down):  self.y += self.vy
        #if(gui.userInput.left):  self.x -= self.vx
        #if(gui.userInput.right): self.x += self.vx

            #print(gui.userInput.returnedKey)
        

        # update animation
        self.updateSprite()

    def updateSprite(self):
        self.sprite.x,self.sprite.y = self.x,self.y