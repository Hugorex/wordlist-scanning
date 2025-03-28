import requests

def scan_url(target_url, word):
    full_url = f"{target_url.rstrip('/')}/{word}"
    try:
        response = requests.get(full_url, timeout=5)
        
        # Si la respuesta es 200, el recurso existe
        if response.status_code == 200:
            print(f"Encontrado: {full_url} (Código {response.status_code})")
        elif response.status_code == 403:
            print(f"Acceso denegado: {full_url} (Código {response.status_code})")
        elif response.status_code == 404:
            print(f"No encontrado: {full_url} (Código {response.status_code})")
        else:
            print(f"Estado desconocido: {full_url} (Código {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con {full_url}: {e}")

# --- Parámetros del escaneo ---
TARGET_URL = "http://127.0.0.1:8000"  # Cambia por el sitio a escanear

# Leer las palabras desde un archivo
with open("wordlist.txt", "r") as file:
    words = file.readlines()

# Eliminar saltos de línea
words = [word.strip() for word in words]

# --- Ejecutar escaneo ---
print(f"Buscando las palabras en {TARGET_URL}...\n")

for word in words:
    scan_url(TARGET_URL, word)