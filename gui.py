import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
add_buton = sg.Button("Add")
exit_buton = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_buton], [exit_buton]],
                   font=("Helvetica", 20))

while True:
    event,value = window.read()  # show the window and wait a action. The returno is a tuple
    print(event)
    print(value)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()