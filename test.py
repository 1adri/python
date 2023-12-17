from __future__ import unicode_literals
import PySimpleGUI as sg
from yt_dlp import YoutubeDL

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
}

sg.theme("Topanga")
layout = [
    [sg.Text("")],
    [sg.Text('Video Link', size=(8, 1)), sg.InputText(enable_events=True)],
    [sg.Text("", key='progress')],
    [sg.Image(f"")]
    [sg.Button("Enter", key="Enter"), sg.Button("Cancel", key='Cancel')]
]

window = sg.Window("Download Youtube Video", layout, size=(600, 300), return_keyboard_events=True)
def my_hook(d):

    window['progress'].update("Downloading!")
    window.refresh()  # Add this line to force the window to refresh and show the updated text

while True:
    event, values = window.read()
    text_elem = window['progress']
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if the user closes the window or clicks cancel
        break
    if event == "Enter":
        url = values[0]
        with YoutubeDL(ydl_opts) as ydl:
            ydl.add_progress_hook(my_hook)
            ydl.download([url])
            break


window.close()