#abstract class specifying the interface for the AIs
class AI(): 
	def __init__(self,engine,start_time,time_per_move):
		self.engine = engine
		self.start_time = start_time
		self.time_per_move = time_per_move
	
	def get_starting_state(self):
		raise NotImplementedError

	def get_move(self):
		raise NotImplementedError