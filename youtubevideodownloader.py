import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

layout = [[sg.Text("Press a key or scroll mouse")],
        [sg.Text('Video Link', size =(15, 1)), sg.InputText(enable_events=True)], 

        [sg.Button("OK", key='OK')]]

window = sg.Window("Download Youtube Video", layout, size=(600, 300), return_keyboard_events=True)
# ---===--- Loop taking in user input --- #
text_recorded = ''
while True:
    event, values = window.read()
    print(values[0])    
    if event in ("OK", None):
        print(event, "exiting")
        break
