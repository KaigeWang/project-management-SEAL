class task:
    def __init__(self, id, description, start, end, participant): 
        pass
    

class participant:
    def __int__(self, id, name):
        self.id = id
        self.name = name
        
class seal:
    def __int__(self):
        self.participations = {1: participant(1, 'Rebecca')}
        self.task = dict()
        
    def addTask(self, task):
        
        self.task[task.getID()] = task
        
    def addParticipant(self, participant):
        pass