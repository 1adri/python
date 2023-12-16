import PySimpleGUI as sg
layout= [
        [sg.Text("Hello")],
        [sg.Button("OK")]
        ]
window = sg.Window("Test App", layout, margins=(350,300))

while True:
    event, values= window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()