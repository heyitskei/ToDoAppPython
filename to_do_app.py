username = input("Hi there! Welcome to the world's best To-Do list app! Please type in your name: ")

# Generate a new filename for the user
filename = f"{username}_to_do_app.txt"

print("Hi there " + username + "!\n")

isNewUser = input("Are you new here? Please type Y for yes and N for no. ")

def addNewTask(f):
    print("Usage: keep adding tasks until you're all done. If you wish to stop, simply type in /q")
    isNewTask = input("What are you up to: ")
    
    while (isNewTask != "/q"):
        f.write(isNewTask)
        f.write("\n")
        #add formatting for list 1, 2, 3, etc
        # i = 1        
        isNewTask = input("What else are you up to: ")
        # f.write(i + isNewTask)
        # i+1
    
    f.close()
    
    return tasks



def displayTasks():
    print("Here are all the things you put in: \n")
    f = open("to_do_app.txt", "rt")
    print(f.read())
    


def deleteLines(lineToDelete):
    line = lineToDelete;
    
    #loop and prompt for more lines to be deleted?
    #this does not work
    
    f = open("to_do_app.txt", "r")
    lines = f.readlines()
    f.close()
    
    f = open("to_do_app.txt", "w")
    for number, line in enumerate(lines):
        if number != lineToDelete:
            f.write(line)
            
    f.close()
    
    print("Here is you updated list of tasks:\n")
    displayTasks()



def modifyToDoList():
    
    print("Do you wish to add more tasks or edit existing ones?")
    
    fileEdit = input("Please type A for add, E for edit, D for deleting and C to cancel")
    
    if fileEdit == "A":
        f = open(filename, "at")
        addNewTask()
    elif fileEdit == "E":
        #put code here
        print("test")
    elif fileEdit == "D":
        lineToDelete = input("Please specify which task (by the number) you wish to delete: ")
        deleteLines(lineToDelete)        
    #elif fileEdit == "E":



def createNewToDoList():
    f = open(filename, "wt")
    
    print("That's a great start! Let's jump right into organizing your tasks!")
    curr_task_list = addNewTask(f)
    curr_task_list_len = len(curr_task_list)
    
    # Check that there are tasks in the list
    if curr_task_list_len != 0: 
        displayTasks()
    
        modifyToDoList()
    
    
        
        
# Ignore the case 
if isNewUser.lower() == "y":
    
    createNewToDoList()
    
    #create a new file for writing
    #start adding tasks
    #when done, save and close

# if isNewUser == "N":
#     f = open("to_do_app.txt", "rt")
#     print("Here are all the awesome things you've been up to: ")
#     print(f.read())
#     print("And here are some cool things you can do: ")
#     #load options here: edit, add, delete



        