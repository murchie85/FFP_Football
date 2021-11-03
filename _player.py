class playerSprite():
    def __init__(self,imageFrames,x,y):
        self.imageFrames = imageFrames
        self.numFrames   = len(self.imageFrames)
        self.framePos    = 0
        self.x           = x
        self.y           = y
        self.w           = self.imageFrames[0].get_rect().w
        self.h           = self.imageFrames[0].get_rect().h
        self.vx          = 0
        self.vy          = 0
        self.frameTime   = 0

    def animate(self,gui,interval=0.5):
        """
        animages image every interval (in seconds)
        once image reaches end, it resets to first image
        """
        
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
