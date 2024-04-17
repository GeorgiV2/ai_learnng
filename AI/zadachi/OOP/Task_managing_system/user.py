class User:
    def __init__(self,id:int, name:str,role:str,email:str,assigned_tasks=None):
        self.id = id
        self.name = name
        self.role = role
        self.email = email
        self.assigned_tasks = assigned_tasks
