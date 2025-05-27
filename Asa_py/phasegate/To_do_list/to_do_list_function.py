todo_s = []

def create_console(task):
	todo = [task]
	todo_s.append(todo)

def view_tasks():
	for tasks in todo_s:
		print(tasks)

def mark_task_completed(choose):
	for item in todo_s:
		if item == choose:
			todo_s[item] = ('[X]')
			

def delete_task_completed(choose):
	for task in todo_s:
		if task == choose:
			todo_s[0].remove


