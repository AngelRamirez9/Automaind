import tkinter as tk
import http.client
import json
from datetime import datetime

SUPABASE_URL = 'https://widtzsbgfpwztzfqaofe.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndpZHR6c2JnZnB3enR6ZnFhb2ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjcyNzE3NDEsImV4cCI6MjA0Mjg0Nzc0MX0.wzza60NYwlHdCeyVvO1WOLW2ASmGsOciKXy2rWB_lss'
SUPABASE_TABLE = 'movimientos'

root = tk.Tk()
root.title("Formulario")

nombre_var = tk.StringVar()
telefono_var = tk.StringVar()
correo_var = tk.StringVar()
monto_var = tk.StringVar()
lugarEnvio_var = tk.StringVar()

def guardar_datos():
    nombre = nombre_var.get()
    telefono = telefono_var.get()
    correo = correo_var.get()
    monto = monto_var.get()
    lugar = lugarEnvio_var.get()
    
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
    conn.request("POST", f"/rest/v1/{SUPABASE_TABLE}", body=json.dumps(datos), headers=headers)
    
    response = conn.getresponse()
    status = response.status
    response_text = response.read().decode()

    if status == 201:
        print("Datos guardados en Supabase con éxito")
    else:
        print(f"Error al guardar los datos: {status} {response_text}")

    nombre_var.set("")
    telefono_var.set("")
    correo_var.set("")
    monto_var.set("")
    lugarEnvio_var.set("")

tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=nombre_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Teléfono:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=telefono_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Correo:").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=correo_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Monto:").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=monto_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Lugar de Envío:").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=lugarEnvio_var).grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Guardar", command=guardar_datos).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
