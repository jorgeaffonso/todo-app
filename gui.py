import time
import functions
import PySimpleGUI as sg
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button= sg.Button("Complete")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

while True:
    event,value = window.read(timeout=200)  # show the window and wait a action. The return is a tuple

    window["clock"].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                if new_todo[-1] != '\n':
                    new_todo = new_todo +'\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select a item first",font=("Helvetica",20))
        case 'Complete':
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select a item first",font=("Helvetica",20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()



