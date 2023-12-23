# Get username from the user as the app is being launched and greet the player 
username = input("Hi there! Welcome to the world's best To-Do list app! Please type in your name: ")
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



def displayTasks():
    print("Here is the list of your awesome endeavours:")
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
        f = open("to_do_app.txt", "at")
        addNewTask()
    elif fileEdit == "E":
        #put code here
        print("test")
    elif fileEdit == "D":
        lineToDelete = input("Please specify which task (by the number) you wish to delete: ")
        deleteLines(lineToDelete)        
    #elif fileEdit == "E":



def createNewToDoList():
    f = open("to_do_app.txt", "wt")
    print("That's a great start! Let's jump right into organizing your tasks!")
    addNewTask(f)
      
    
    # Check that there are tasks in the list
    displayTasks()
    
    modifyToDoList()
    
    
        
        

if isNewUser == "Y":
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



        