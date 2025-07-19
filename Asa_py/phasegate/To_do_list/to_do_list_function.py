todo_s = []

def create_console(task):
	todo = task
	todo_s.append(todo)

def view_tasks():
	for index, value in enumerate(todo_s):
		print(index, value)

def mark_task_completed(choose):
	for index, value in enumerate(todo_s):
		if index == choose:
			todo_s[choose] += '[X]'
			

def delete_task_completed(choose):
	for index, value in enumerate(todo_s):
		if index == choose:
			todo_s.pop(choose)
