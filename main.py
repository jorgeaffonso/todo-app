
# MESMO PROGRAMA QUE O main_first.py  SÓ QUE BASEADO EM OPERAÇÕES 'if' & 'ifel'

#Como importar as Funções
#from functions import get_todos, write_todos
#           ou
import functions as fuk
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

user_prompt = "Type add, show, edit or exit: "
todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]+'\n'

        todos = fuk.get_todos()

        todos.append(todo)
        fuk.write_todos(todos)

    elif user_action.startswith('show'):
        todos = fuk.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = fuk.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo +'\n'

            fuk.write_todos(todos)

        except ValueError:
            print('this command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = fuk.get_todos()
            item_to_remove = todos[number].strip('\n')
            todos.pop(number)

            fuk.write_todos(todos)

            message = f'The item -{item_to_remove}- was removed from de list'
            print(message)
        except IndexError:
            print('There  isn´t that index in the list')
            continue
    elif user_action.startswith('exit'):
            break
    else:
        print('This command es not valid')

print("bye")
