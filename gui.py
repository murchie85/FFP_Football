class gui():
	def __init__(self,width,height,font):
		self.width        = width
		self.height       = height
		self.font 		  = font



		self.running      = True
		self.dt 		  = 0
		self.gameElapsed  = 0
		self.debugSwitch  = False
		self.mx			  = 0
		self.my	          = 0



	def debug(self,debugMessage):
		if(self.debugSwitch):
			print(debugMessage)

