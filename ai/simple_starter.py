from starter import Starter

class SimpleStarter(Starter):
    def __init__(self,start_time, state):
        super(SimpleStarter, self).__init__(start_time)
        self.start_state = state

    def start(self):
        return self.start_state