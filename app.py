from flask import Flask, request, jsonify, send_file
import os
import tempfile

app = Flask(__name__)

# Carpeta temporal dentro del contenedor (se borra al reiniciar, es normal)
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
        # === AQUÍ IRÁ TU LLAMADA AL CORE ===
        # Por ahora, simulamos para probar que el deploy funciona
        # ruta_archivo = mi_funcion_del_core(url, ...)
        
        # Placeholder: crea un archivo de prueba
        ruta_archivo = os.path.join(TEMP_DIR, "prueba.txt")
        with open(ruta_archivo, "w") as f:
            f.write(f"Descarga simulada para: {url}")

        return send_file(ruta_archivo, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# NO pongas app.run() aquí. Gunicorn se encarga.