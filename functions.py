# custom functions - is a slot where you put some code,allows you to eliminate repetitive code
# doc strings are used for commenting and explaining internally what a function is for


def get_todos(filepath="/home/gandii/Documents/pythonProjects/todos.txt"):
    # example of a doc string
    # """ This function is for reading out the content of a file """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# help(get_todos)


def write_todos(todos_arg, filepath= "/home/gandii/Documents/pythonProjects/todos.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)





print(__name__)
if __name__ == "__main__":
    print("hello")
