from __future__ import unicode_literals
import PySimpleGUI as sg
from yt_dlp import YoutubeDL

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'ffmpeg_location': r'_internal\ffmpeg.exe',  # Specify the path to your FFmpeg executable

    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

sg.theme("Topanga")
layout = [
    [sg.Text("")],
    [sg.Text('Video Link', size=(8, 1)), sg.InputText(enable_events=True)],
    [sg.Text(" ", size=(50, 5), key='progress')],
    [sg.Button("Download", key="Enter"), sg.Button("Close", key='Close')]
]
def parse_string(input_string):
    return input_string[7:12]

window = sg.Window("Download Youtube Video", layout, size=(600, 300), return_keyboard_events=True)
def my_hook(d):
    
    new_x = parse_string(d['_percent_str'])
    if d['status'] == 'downloading':
        window['progress'].update(f"Downloading: {video_title}({new_x})%")

    if d['status'] == 'finished':
        window['progress'].update("Finished!")
    window.refresh()  # Add this line to force the window to refresh and show the updated text

while True:
    event, values = window.read()
    text_elem = window['progress']
    if event == sg.WIN_CLOSED or event == 'Close':  # if the user closes the window or clicks cancel
        break
    if event == "Enter":
        

        url = values[0]
        with YoutubeDL(ydl_opts) as ydl:
            window.refresh()
            ydl.add_progress_hook(my_hook)
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            window['progress'].update(f"Downloading: {video_title}")
            window.refresh()  # Force the window to refresh and show the updated text
            ydl.download([url])
            #break


window.close()