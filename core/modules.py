import yt_dlp
import os

def descargar_maximaDefinicion(url, carpeta_destino):
    # Ruta al archivo de cookies (está en la raíz de web/)
    ruta_cookies = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cookies.txt")
    
    outtmpl = os.path.join(carpeta_destino, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'outtmpl': outtmpl,
        'format': 'bestvideo+bestaudio/best',
        'restrictfilenames': True, 
        'cookiefile': ruta_cookies,  # <--- AQUÍ LE DECIMOS QUE USE LAS COOKIES
        'source_address': '0.0.0.0',  # <-- Fuerza IPv4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        archivo_final = ydl.prepare_filename(info)
        
        if not os.path.exists(archivo_final):
            base, _ = os.path.splitext(archivo_final)
            archivo_final = base + ".mp4"
            
        if not os.path.exists(archivo_final):
            archivos = [os.path.join(carpeta_destino, f) for f in os.listdir(carpeta_destino)]
            if archivos:
                archivo_final = max(archivos, key=os.path.getctime)

        return archivo_final