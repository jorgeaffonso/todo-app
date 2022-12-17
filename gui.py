import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_buton = sg.Button("Add")
exit_buton = sg.Button("Exit")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_buton], [exit_buton]])
window.read()  # show the window and wait a action
window.close()