while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()  # .strip(): sin argumentos quita los espacios al final en una cadena, con argumentos quita el simbolo parametrizado

    # match: para comparar strings y se usan case para cada caso encontrado
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            # file = open('todos.txt', 'r')  # Se abre un archivo y se lee
            # todos = file.readlines()  # Se leen las líneas que componen el archivo y se guardan en forma de lista
            # file.close()  # Se cierra el archivo, es recomendable cerrarlo cada que terminamos de trabajar con él

            # Accediendo al archivo usando context manager
            with open('todos.txt', 'r') as file:
                todos = file.readlines()  # ya no es necesario cerrar el archivo con .close()

            todos.append(todo)  # Se añade el nuevo elemento a la lista

            # file = open('todos.txt', 'w')  # Se vuelve a abrir el archivo pero ahora para escribir
            # file.writelines(todos)  # Se reescriben las lineas del archivo con la lista actualizada
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for id, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{id + 1}. {item}")

        case 'edit':
            print("Got it!")

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index_to_edit = int(input("Number of the todo to edit: ")) - 1
            todos[index_to_edit] = input(f"Type new todo for '{todos[index_to_edit]}': ") + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            index_to_remove = int(input("Number of the todo to complete: ")) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove =  todos[index_to_remove].strip('\n')
            todos.pop(index_to_remove)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)

        case 'exit':
            break
        # Esto es como el case default, pero en vez de default, añadimos una variable vacía
        case _:
            print("You entered an unknown command...")

print("Bye!")
