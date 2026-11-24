import yt_dlp

def descargar_maximaDefinicion(url):

    url = url

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
