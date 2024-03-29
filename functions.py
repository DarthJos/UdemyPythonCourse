FILEPATH = 'todos.txt'      # Filepath constant

def get_todos(local_filepath=FILEPATH):     # Added default value for get_todos argument
    """Read a text file and return the list of to-do items."""
    with open(local_filepath, 'r') as local_file:
        local_todos = local_file.readlines()

    return local_todos


def write_todos(todos_arg, local_filepath='todos.txt'):
    """Write the to-do items list in the text file."""
    with open(local_filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("\n ==== Esto solo se ejecuta cuando este archivo se ejecuta a sí mismo. ====")