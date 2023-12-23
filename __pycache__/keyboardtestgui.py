
import sys
import PySimpleGUI as sg


layout = [[sg.Text("Press a key or scroll mouse")],
          [sg.Text("a", size=(18, 1), key='text', enable_events=True, relief=sg.RELIEF_RIDGE)],
          [sg.Text("")],
          [sg.Button("OK", key='OK')]]

window = sg.Window("Keyboard Test", layout, size=(600, 300), return_keyboard_events=True)
# ---===--- Loop taking in user input --- #
text_recorded = ''
while True:
    event, values = window.read()
    text_elem = window['text']
    if event in ("OK", None):
        print(event, "exiting")
        break
    if len(event) == 1:
        input1 = value='%s' % (event)
        text_elem.update(text_recorded+input1)
        text_recorded = text_recorded+input1

    if event == "BackSpace:8":
        if text_recorded:
            text_recorded = text_recorded[:-1]
            text_elem.update(text_recorded)
        else:
            # Perform other action if text is empty
            print("No text to delete")


window.close()
print(text_recorded)