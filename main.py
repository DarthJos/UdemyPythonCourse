def get_todos():
    print("INICIA ==>  getTodos()")
    
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    
    return todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()  # .strip(): sin argumentos quita los espacios al final en una cadena, con argumentos quita el simbolo parametrizado

    # match: para comparar strings y se usan case para cada caso encontrado
# ==========================================    ADD     ==========================================
    if user_action.lower().startswith('add'):

        todo = input("Enter a todo: ") if len(user_action) < 4 else user_action[4:]

        todos = get_todos()     #Llama a la función get_todos para abrir archivo y llenar la lista

        todos.append(todo+'\n')  # Se añade el nuevo elemento a la lista

        # file = open('todos.txt', 'w')  # Se vuelve a abrir el archivo pero ahora para escribir
        # file.writelines(todos)  # Se reescriben las lineas del archivo con la lista actualizada
        # file.close()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

# ==========================================    SHOW    ==========================================
    elif user_action.lower().startswith('show'):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for id, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{id + 1}. {item}")

# ==========================================    EDIT     ==========================================
    elif user_action.lower().startswith('edit'):
        try:

            todos = get_todos()

            user_index_to_edit = int(input("Number of the todo to edit: ")) if len(user_action) < 5 else int(user_action[5:])
            real_index_to_edit = user_index_to_edit - 1
            todos[real_index_to_edit] = input(f"Type new todo for '{todos[real_index_to_edit].strip('\n')}': ") + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except IndexError:
            print(f"Sorry, there is no item with that number. Please enter a number between 1 and {len(todos)}")

        except ValueError:
            todo_to_edit = user_action[5:] + '\n'

            if todo_to_edit in todos:
                index_found = todos.index(todo_to_edit)
                print(f"Seems that you are trying to edit todo: {index_found + 1}. {todos[index_found]}")
                proceed = input("Proceed editing the item? Y/N")

                if proceed.lower().startswith('y'):
                    todos[index_found] = input(f"Type new todo for '{todos[index_found].strip('\n')}': ") + '\n'

                    with open('todos.txt', 'w') as file:
                        file.writelines(todos)
            else:
                print("Todo not found...\n")

# ==========================================    COMPLETE    ==========================================
    elif user_action.lower().startswith('complete'):
        try:
            index_to_remove = int(input("Number of the todo to complete: ")) if len(user_action) < 9 else int(user_action[9:])
            index_to_remove -= 1

            todos = get_todos()

            todo_to_remove = todos[index_to_remove].strip('\n')
            print(todo_to_remove)
            todos.pop(index_to_remove)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print(f"Sorry, there is no item with that number. Please enter a number between 1 and {len(todos)}")

        except ValueError:
            print(f"Please enter the number of the to do. Choose from 1 to {len(todos)}")
# ==========================================        EXIT     ==========================================
    elif user_action.lower().startswith('exit'):
        break
    # Esto es como el case default, pero en vez de default, añadimos una variable vacía

# ========================================== UNKNOWN COMMAND ==========================================
    else:
        print("You entered an unknown command...")

print("Bye!")
