import yt_dlp
import os

def descargar_maximaDefinicion(url, carpeta_destino):
    # Configuramos yt-dlp para que guarde en la carpeta_destino
    # y le pedimos que nos devuelva la ruta del archivo en el "hook" o al final.
    
    # Plantilla de salida: guarda en la carpeta con el título del video
    outtmpl = os.path.join(carpeta_destino, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'outtmpl': outtmpl,
        'format': 'bestvideo+bestaudio/best',
        # Opcional: esto ayuda a que no haya problemas con caracteres raros en nombres
        'restrictfilenames': True, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        # yt-dlp nos dice cuál fue el archivo final descargado
        # A veces pide fusionar (video+audio) y la extensión final cambia (ej. .mp4)
        archivo_final = ydl.prepare_filename(info)
        
        # Si el archivo final no existe (porque se fusionó con ffmpeg y cambió la extensión),
        # buscamos la versión .mp4 que es la típica tras la fusión.
        if not os.path.exists(archivo_final):
            base, _ = os.path.splitext(archivo_final)
            archivo_final = base + ".mp4"
            
        # Fallback de seguridad: si aún así no existe, buscamos cualquier cosa en la carpeta
        if not os.path.exists(archivo_final):
            # Busca el archivo más reciente en la carpeta destino
            archivos = [os.path.join(carpeta_destino, f) for f in os.listdir(carpeta_destino)]
            if archivos:
                archivo_final = max(archivos, key=os.path.getctime)

        return archivo_final