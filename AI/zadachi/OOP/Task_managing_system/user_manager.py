import datetime
from task import Task
from user import User

class User_Manager():

    def __init__(self):
        self.users = []

    def add_user(self,id:int,name:str,role:str,email:str,assigned_tasks=None):
        self.users.append(User(id,name,role,email,assigned_tasks))
    
    def update_user(self,id,o,newindex):
        for user in self.users:
            if user.id == id:
                setattr(user, o, newindex)

    def listUsers(self):
        for user in self.users:
            print("User:", user.name)
            print("Email:", user.email)
            print("Role:", user.role)
            print("Assigned Tasks:")
            if user.assigned_tasks:
                for task in user.assigned_tasks:
                    print("  -", task.title, "-", task.description, "-", task.status)
            else:
                print("  - No tasks assigned")
            print()  # Add an empty line between users for clarity

    
    def filterByRole(self,str):
          if str == "new":
             new = [obj for obj in self.users if obj.role == "new"]
             return new
          elif str == "engineer":
                eng = [obj for obj in self.users if obj.role == "engineer"]
                return eng
          elif str == "manager":
                manager = [obj for obj in self.users if obj.role == "manager"]
                return manager
        
    def assign_task(self, id, task: Task):
        for user in self.users:
            if user.id == id:
                if user.role == "new" and user.assigned_tasks is None:
                    user.assigned_tasks = [task]
                elif user.role != "new":
                    user.assigned_tasks.append(task)
                else:
                    return "This is a new user and they have already been given a task!"
        return "There is no user associated with this id"

    def get_user(self,id):
        for i in range(len(self.users)):
            if self.users[i].id == id:
                return self.users[i]
        return "User not found"