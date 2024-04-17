import datetime

class Task:
    def __init__(self,id,title: str,description: str,status:str,due_date: datetime,priority:int):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority