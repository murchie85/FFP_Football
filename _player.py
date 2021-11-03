class playerSprite():
    def __init__(self,imageFrames):
        self.imageFrames = imageFrames
        self.numFrames   = len(self.imageFrames)
        

        self.framePos    = 0
        self.x           = 0
        self.y           = 0
        self.w           = self.imageFrames[0].get_rect().w
        self.h           = self.imageFrames[0].get_rect().h
        self.frameTime   = 0


        self.u           = False
        self.d           = False
        self.l           = False
        self.r           = False

        self.currentDirection   = None


    

    def getDirection(self,gui):

        direction = None

        # reset
        self.u,self.d,self.l,self.r = False,False,False,False
        
        if(gui.userInput.up):    self.u = True
        if(gui.userInput.down):  self.d = True
        if(gui.userInput.left):  self.l = True
        if(gui.userInput.right): self.r = True

        if(self.u): direction = 'up'
        if(self.d): direction = 'down'
        if(self.l): direction = 'left'
        if(self.r): direction = 'right'

        return(direction)




    def animate(self,gui,interval=0.2,stop=False):
        """
        animages image every interval (in seconds)
        once image reaches end, it resets to first image
        """

        # Update direction Frames
        direction = self.getDirection(gui)

        if(self.currentDirection!=direction):
            print('updateDirection')
            self.currentDirection = direction

        

        if(stop):
            gui.screen.blit(self.imageFrames[0],(self.x,self.y))
            return()
        

        #-----------animate
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

        self.sprite.animate(gui)
        #if(gui.userInput.down):  self.y += self.vy
        #if(gui.userInput.left):  self.x -= self.vx
        #if(gui.userInput.right): self.x += self.vx

            #print(gui.userInput.returnedKey)
        

        # update animation
        self.updateSprite()

    def updateSprite(self):
        self.sprite.x,self.sprite.y = self.x,self.y