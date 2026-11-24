from flask import Flask, request, jsonify, send_file
import os

# IMPORTANTE: Asegúrate de que el archivo se llame modules.py 
# y esté en la misma carpeta o en una carpeta llamada core/
from core.modules import descargar_maximaDefinicion

app = Flask(__name__)

TEMP_DIR = os.path.join(os.path.dirname(__file__), "temp")
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route("/")
def index():
    return "API funcionando correctamente en Render"

@app.route("/descargar", methods=["POST"])
def descargar_endpoint():
    datos = request.get_json()
    url = datos.get("url")
    
    if not url:
        return jsonify({"error": "Falta la URL"}), 400

    try:
        print(f"Iniciando descarga de: {url}")
        
        # Llamamos a tu función real
        ruta_archivo = descargar_maximaDefinicion(url, TEMP_DIR)

        if not os.path.exists(ruta_archivo):
            return jsonify({"error": "El archivo no se generó correctamente"}), 500

        print(f"Archivo generado en: {ruta_archivo}")

        # Enviamos el archivo al usuario
        return send_file(
            ruta_archivo, 
            as_attachment=True, 
            download_name=os.path.basename(ruta_archivo) 
        )
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Gunicorn se encarga de ejecutar esto