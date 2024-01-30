todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()  # .strip(): sin argumentos quita los espacios al final en una cadena, con argumentos quita el simbolo parametrizado

    # match: para comparar strings y se usan case para cada caso encontrado
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' :
            for id, item in enumerate(todos):
                print(f"{id + 1}. {item}")
        case 'edit':
            print("Got it!")
            index_to_edit = int(input("Number of the todo to edit: ")) - 1
            todos[index_to_edit] = input(f"Type new todo for '{todos[index_to_edit]}': ")
        case 'complete':
            index_to_remove = int(input("Number of the todo to complete: ")) - 1
            todos.pop(index_to_remove)
        case 'exit':
            break
        # Esto es como el case default, pero en vez de default, añadimos una variable vacía
        case _:
            print("You entered an unknown command...")

print("Bye!")
