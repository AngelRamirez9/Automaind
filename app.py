from flask import Flask, render_template, request, jsonify
import http.client
import json
from datetime import datetime

app = Flask(__name__)

SUPABASE_URL = 'widtzsbgfpwztzfqaofe.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndpZHR6c2JnZnB3enR6ZnFhb2ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjcyNzE3NDEsImV4cCI6MjA0Mjg0Nzc0MX0.wzza60NYwlHdCeyVvO1WOLW2ASmGsOciKXy2rWB_lss'
SUPABASE_TABLE = 'movimientos'

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar_datos():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    monto = request.form['monto']
    lugar = request.form['lugarEnvio']
    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datos = {
        'nombre': nombre,
        'telefono': telefono,
        'correo': correo,
        'monto': monto,
        'lugar_envio': lugar,
        'fecha_hora': fecha_hora
    }
    
    headers = {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}'
    }

    conn = http.client.HTTPSConnection(SUPABASE_URL)
    conn.request("POST", f"/rest/v1/{SUPABASE_TABLE}?on_conflict=telefono", body=json.dumps(datos), headers=headers)
    
    response = conn.getresponse()
    status = response.status
    response_text = response.read().decode()

    if status == 201:
        return jsonify({'message': 'Datos guardados o actualizados en Supabase con éxito'})
    else:
        return jsonify({'error': f"Error al guardar los datos: {status} {response_text}"}), 400

if __name__ == '__main__':
    app.run(debug=True)

