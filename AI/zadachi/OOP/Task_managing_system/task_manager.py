import datetime
from task import Task
from user import User


class Task_Manager():
    def __init__(self):
        self.tasks = []

    def add_task(self,id,title:str, description:str,status:str,due_date:datetime,priority:int):
        task= Task(id,title, description,status,due_date,priority)
        self.tasks.append(task)

        
    def updateStatus(self,id:int,status:str):
       for i in range(len(self.tasks)):
           if self.tasks[i].id == id:
               self.tasks[i].status = status
    
    def listTasks(self):
        for i in range(len(self.tasks)):
            print(self.tasks[i].id ,self.tasks[i].title, self.tasks[i].priority, self.tasks[i].status   )
    
    def filterByStatus(self,str):
        if str == "active":
             active = [obj for obj in self.tasks if obj.status == "active"]
             return active
        elif str == "done":
             done = [obj for obj in self.tasks if obj.status == "done"]
             return done

    def filterByPriority(self):
        n = len(self.tasks)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.tasks[j].priority > self.tasks[j+1].priority:
                    self.tasks[j], self.tasks[j+1] = self.tasks[j+1], self.tasks[j]
    
    def get_task(self,id):
        for i in range(len(self.tasks)):
            if self.tasks[i].id == id:
                return self.tasks[i]
        return "Task not found"
            
