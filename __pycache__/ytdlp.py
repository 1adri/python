from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=YLRdnXsNT08']
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # prioritize MP4 format
    'outtmpl': '%(id)s.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
