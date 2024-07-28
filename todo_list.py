print("Welcome to the To-Do List App!")
print(
    '''
Menu:
1. Add a task 
2. View tasks 
3. Mark a task as complete
4. Delete a task 
5. Quit
'''
)

todolist = []

selection = input("What would you like to do first? Select a number from the list ")

try:
    while selection != "5":
        if selection == "1":
            addtask = str(input("What would you like to add to the list? "))
            todolist.append(addtask)
        elif selection == "2":
            print(''.join(todolist))
        elif selection == "3":
            markoff = str(input("What task would you like to mark as completed? "))
            if markoff in todolist:
                todolist.remove(markoff)
                print(f'Task "{markoff}" has been marked as completed.')
            else:
                print(f'Task "{markoff}" not found in the list.')
        elif selection == "4":
            deletetask = str(input("What task would you like to delete? "))
            if deletetask in todolist:
                todolist.remove(deletetask)
                print(f'Task "{deletetask}" has been deleted.')
            else:
                print(f'Task "{deletetask}" not found in the list.')
        else:
            print("Invalid selection. Please choose a number from the menu.")

        selection = input("What would you like to do next? Select a number from the list ")
except:
    print("Invalid input")
finally:
    print("Thank you for using the To-Do List App!")


