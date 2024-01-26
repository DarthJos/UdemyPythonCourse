todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.lower().strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for id, item in enumerate(todos):
                print(f"{id+1}. {item}")
        case 'edit':
            print("Got it!")
            number = int(input("Number of the todo to edit: "))
            todos[number-1] = input(f"Type new todo for '{todos[number-1]}': ")
        case 'exit':
            break

print("Bye!")