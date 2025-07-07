import to_do_list_function
option = True
while option:
	message = '''
welcome to my todo list...

what would you like to do today?

1. Add a task
2. View all task
3. Mark a task as complete
4. Delete a task
0. Exit
'''
	print(message)
	user_choice = int(input('pick a number to choose what to do: '))
	match(user_choice):
		case 1:
			message = '''
Welcome to add task:
Add your task
'''
			user = input('Enter your task: ')
			to_do_list_function.create_console(user)
			message_task = '''
Task has been added succesfully

'''
			
		case 2:
			message = '''
Welcome to view task:
			
Here are you list of tasks...

press 0 to go back
'''			
			print(message)
			to_do_list_function.view_tasks()
			user = input('Enter 0 to go back: ')
			match(user):
				case 0:
					message_task = '''
Goodbye
'''
					print(message_task)
				case _:
					print('invalid input')

		case 3:
			message = '''
Welcome to Mark task:
			
Here are your list of tasks...

press 1 to choose task to mark
press 0 to go back
'''			
			print(message)
			to_do_list_function.view_tasks()
			user = int(input('Enter a number: '))
			match(user):
				case 1:
					choose = int(input('Enter the task to mark: '))
					to_do_list_function.mark_task_completed(choose)
					
				case 0:
					message_task = '''
Goodbye
'''
					print(message_task)
				case _:
					print('invalid input')


		case 4:
			message = '''
Welcome to delete task:
			
Here are your list of tasks...

press 1 to choose task to delete
press 0 to go back
'''			
			print(message)
			to_do_list_function.view_tasks()
			user = int(input('Enter a number: '))
			match(user):
				case 1:
					choose = int(input('Enter the delete to mark: '))
					to_do_list_function.delete_task_completed(choose)

				case 0:
					message_task = '''
Goodbye
'''
					print(message_task)
				case _:
					print('invalid input')

		case 0:
			option = False
			message_task = '''
Goodbye
'''
			print(message_task)
		case _:
			print('invalid input')
