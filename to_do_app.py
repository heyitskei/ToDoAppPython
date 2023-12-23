# Get username from the user as the app is being launched and greet the player 
username = input("Hi there! Welcome to the world's best To-Do list app! Please type in your name: ")

# Generate a new filename for the user
filename = f"{username}_to_do_app.txt"

print("Hi there " + username + "!\n")

# Check if the user is new or a returning user
isNewUser = input("Are you new here? Please type Y for yes and N for no. ")

# Function that adds new tasks to the list 
def addNewTask(f):
    print("Usage: keep adding tasks until you're all done. If you wish to stop, simply type in /q")
    
    # Assign an empty array to keep track of the tasks 
    tasks = []
    isNewTask = input("What are you up to: ")
    
    i = 1   
    while (isNewTask != "/q"):
        tasks.append(str(i) + "." + isNewTask)
        isNewTask = input("What else are you up to: ")
        i += 1  

    # Write tasks into a file as a single string separated by the new line
    f.writelines('\n'.join(tasks))

    f.close()
    
    return tasks



def displayTasks():
    print("Here is the list of your awesome endeavours:")
    f = open(filename, "rt")
    print(f.read())  
        


def deleteLines(filename, lineToDelete):
    
    # Open the file, read the lines and close it (load the contents into memory)
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    
    # lineToDelete == user enters the line number (without dot)

    # Search the doc for that line (number)
        # Need to search for the specific entry -> the line number + '."
        # Add the '.' after the number entered by the user 
        # Then search lines (file contents loaded above)
    
    # Find the correct line (find the number with '.') and get the WHOLE line (up to the next int)
    # Delete this line (i.e. rewite the entire doc without this line)
    # Save and close
    # Prompt the user to check if they wish to delete more lines
        # Yes - Start again (loop?)
        # No - Exit    
    
    f = open(filename, "a")
    for number, line in enumerate(lines, start=1):
        if number != lineToDelete:
            f.write(line)
            
    f.close()
    
    #print("Here is your updated list of tasks:\n")
    # Display the updated list of tasks
    displayTasks()



def modifyToDoList():
    
    print("Do you wish to add more tasks or edit existing ones?")
    
    fileEdit = input("Please type A for add, E for edit, D for deleting and C to cancel")
    
    if fileEdit.lower() == "a":
        f = open(filename, "at")
        addNewTask()
    elif fileEdit.lower() == "e":
        #put code here
        print("test")
    elif fileEdit.lower() == "d":
        lineToDelete = input("Please specify which task (by the number) you wish to delete: ")
        deleteLines(filename, lineToDelete)        



def createNewToDoList():
    f = open(filename, "wt")
    
    print("That's a great start! Let's jump right into organizing your tasks!")
    curr_task_list = addNewTask(f)
    curr_task_list_len = len(curr_task_list)
    
    # Check that there are tasks in the list
    if curr_task_list_len != 0: 
        displayTasks()
    
        modifyToDoList()
    
    
        
        
# Check if the user is new or a returning user
if isNewUser.lower() == "y":
    
    createNewToDoList()

if isNewUser.lower() == "n":
     f = open(filename, "rt")
     print("Here are all the awesome things you've been up to: ")
     print(f.read())
     print("And here are some cool things you can do: ")
     modifyToDoList()



        