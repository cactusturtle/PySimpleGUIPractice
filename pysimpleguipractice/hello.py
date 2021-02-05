import PySimpleGUI as sg
sg.theme('LightTeal')
#print(sg.theme_list())

# All things inside the window
layout = [    [sg.T('Hello! What is your name?')],
              [sg.T('Type your name here: '), sg.InputText()],
              [sg.OK(), sg.Cancel()]]

# Create a new Window
window = sg.Window('Hello', layout)

# Event loop to process 'events'
event, values = window.read()
window.close()

reply = "Hello " + values[0] + "!"
sg.Popup(event, reply)