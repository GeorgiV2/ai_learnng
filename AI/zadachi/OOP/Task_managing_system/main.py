from datetime import datetime, timedelta
from task import Task
from task_manager import Task_Manager
from user_manager import User_Manager
from user import User

tasks = Task_Manager()
users = User_Manager()
base_date = datetime.now()

users.add_user(1,"Ivan","new","ivangultacha@gmail.com")
users.add_user(2, "John Doe", "new", "john.doe@example.com")
users.add_user(3, "Alice Smith", "engineer", "alice.smith@example.com")
users.add_user(4, "David Johnson", "manager", "david.johnson@example.com")
users.add_user(5, "Emily Brown", "new", "emily.brown@example.com")
users.add_user(6, "Michael Wilson", "engineer", "michael.wilson@example.com")
users.add_user(7, "Jessica Lee", "manager", "jessica.lee@example.com")
users.add_user(8, "Matthew Taylor", "new", "matthew.taylor@example.com")
users.add_user(9, "Sarah Anderson", "engineer", "sarah.anderson@example.com")
users.add_user(10, "Christopher Thomas", "manager", "christopher.thomas@example.com")
users.add_user(11, "Samantha Martinez", "new", "samantha.martinez@example.com")

tasks.add_task(1, "Code a web scraping script", "Write Python script to scrape data from a website", "done", base_date + timedelta(days=3), 1)
tasks.add_task(2, "Update website UI", "Redesign website user interface for better user experience", "active", base_date + timedelta(weeks=1), 2)
tasks.add_task(3, "Create user registration system", "Develop a system to allow users to register on the website", "active", base_date + timedelta(weeks=2), 3)
tasks.add_task(4, "Implement search functionality", "Add search feature to the website to allow users to search for content", "done", base_date + timedelta(weeks=3), 1)
tasks.add_task(5, "Optimize database queries", "Improve performance by optimizing database queries", "done", base_date + timedelta(weeks=4), 2)
tasks.add_task(6, "Fix bug in checkout process", "Investigate and fix the bug causing errors during checkout", "active", base_date + timedelta(weeks=5), 3)
tasks.add_task(7, "Write API documentation", "Document the API endpoints and usage for developers", "done", base_date + timedelta(weeks=6), 1)
tasks.add_task(8, "Test website compatibility", "Test website on different browsers and devices for compatibility", "done", base_date + timedelta(weeks=7), 2)
tasks.add_task(9, "Deploy new feature to production", "Deploy new feature to live website after testing", "active", base_date + timedelta(weeks=8), 3)
tasks.add_task(10, "Improve website security", "Enhance security measures to protect against cyber threats", "done", base_date + timedelta(weeks=9), 1)

# ============================== Uncomment part by part to see its functionalities =================================================================

# ============================== Filter tasks by Status ==============================
# done = tasks.filterByStatus("done")
# for i in range(len(done)):
#     print(done[i].id, done[i].title, done[i].status)
# ==============================


# ============================== Filter tasks by Priority ==============================
# tasks.filterByPriority()
# tasks.listTasks()
# ==============================

# ============================== Update status of a task ==============================
# tasks.updateStatus(3,"done")
# tasks.listTasks()
# ==============================

# ============================== Assign task to a user ==============================
# users.assign_task(1,tasks.get_task(3))
# users.listUsers()
# ==============================

# ============================== Filter users by Role ==============================
# filtered = users.filterByRole("new")
# for i in range(len(filtered)):
#     print(filtered[i].id, filtered[i].name, filtered[i].role)
# ==============================

# ============================== Update User ==============================
# users.update_user(1,"name","Georgi")
# users.listUsers()
# ==============================