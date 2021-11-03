class playerSprite():
    def __init__(self,imageFrames):
        self.imageFrames = imageFrames
        

        self.upF         = self.imageFrames[:3]
        self.downF       = self.imageFrames[3:6]
        self.rightF      = self.imageFrames[6:9]
        self.leftF       = self.imageFrames[9:12]

        self.liveFrames  = self.downF
        self.numFrames   = len(self.downF)





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

        if(self.u): 
            direction = 'up'
            self.liveFrames = self.upF
        if(self.d): 
            direction = 'down'
            self.liveFrames = self.downF
        if(self.l): 
            direction = 'left'
            self.liveFrames = self.leftF
        if(self.r): 
            direction = 'right'
            self.liveFrames = self.rightF

        return(direction)




    def animate(self,gui,interval=0.2,stop=False):
        """
        animages image every interval (in seconds)
        once image reaches end, it resets to first image
        """

        # Update direction Frames
        direction = self.getDirection(gui)


        # --------change sprite templates
        if(self.currentDirection!=direction):
            self.currentDirection = direction
            self.framePos = 0
            self.numFrames = len(self.liveFrames)


        

        if(stop):
            gui.screen.blit(self.liveFrames[0],(self.x,self.y))
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
        
        gui.screen.blit(self.liveFrames[self.framePos],(self.x,self.y))




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



    def dribble(self,colliding,fitba,gui,bounce=2):
        if(colliding):
            if(gui.userInput.kick):
                print('kicking')
            if(self.sprite.u): fitba.y -= bounce*self.vy
            if(self.sprite.d): fitba.y += bounce*self.vy
            
            if(self.sprite.l):  
                fitba.x -= bounce*self.vx
                fitba.y  = self.y + (0.6*self.sprite.h)
            
            if(self.sprite.r): 
                fitba.x += bounce*self.vx
                fitba.y  = self.y + (0.6*self.sprite.h)

    def collides(self,playerPos,otherObj):
        x,y,w,h = otherObj.x,otherObj.y,otherObj.w,otherObj.h
        px,py,pw,ph = playerPos[0],playerPos[1],self.sprite.w,self.sprite.h

        if x > px-(0.5*pw) and x < px + (0.5*pw):
            if y > py and y < py + ph:
                return(True)
        return(False)
    
    def play_selected(self,gui,fitba):

        #self.sprite.animate(gui,stop=True)
        stop = (gui.userInput.up==False and gui.userInput.down==False and gui.userInput.left==False and gui.userInput.right==False)
        
        self.u,self.d,self.l,self.r = False,False,False,False
        
        if(gui.userInput.up):    self.u = True
        if(gui.userInput.down):  self.d = True
        if(gui.userInput.left):  self.l = True
        if(gui.userInput.right): self.r = True
        
        # Manage Velocity
        if(gui.userInput.up):    self.y -= self.vy
        if(gui.userInput.down):  self.y += self.vy
        if(gui.userInput.left):  self.x -= self.vx
        if(gui.userInput.right): self.x += self.vx

        # -------check if colliding
        colliding = self.collides((self.x,self.y),fitba)
        
        # ------ dribble ball
        self.dribble(colliding,fitba,gui)
        
        # ------Animate
        self.sprite.animate(gui,stop=stop)

        # -------update position
        self.updateSprite(gui)

    def updateSprite(self,gui):
        self.sprite.x,self.sprite.y = self.x,self.y