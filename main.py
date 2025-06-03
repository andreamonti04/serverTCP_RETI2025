import socket
import os
import datetime

# Configurazione del server
HOST = 'localhost'
PORT = 8080
WEB_ROOT = os.path.join(os.path.dirname(__file__), "www")

# Mappa delle estensioni MIME supportate
MIME_TYPES = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.jpg': 'image/jpeg',
    '.png': 'image/png',
}

# Salva nel file log.txt le richieste ricevute con timestamp.
def log_request(method, path, code):
    with open("log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - {method} {path} -> {code}\n")

# Restituisce il tipo MIME in base all'estensione del file.
def get_mime_type(filename):
    _, ext = os.path.splitext(filename)
    return MIME_TYPES.get(ext.lower(), 'application/octet-stream')

# Traduce il path richiesto in un file locale.
def resolve_path(path):
    routing = {
        "/": "index.html",
        "/storia": "storia.html",
        "/trofei": "trofei.html",
        "/servizi": "servizi.html",
    }
    return routing.get(path, path.lstrip("/"))

# Invia la risposta HTTP al client.
def send_response(client, status_code, content, content_type):
    if isinstance(content, str):
        content = content.encode('utf-8')
        content_type += "; charset=utf-8"
    headers = (
        f"HTTP/1.1 {status_code} {'OK' if status_code == 200 else 'Not Found'}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(content)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    ).encode('utf-8')
    client.sendall(headers + content)

# Gestisce una richiesta HTTP da parte di un client.
def handle_client(client_socket):
    try:
        request = client_socket.recv(1500).decode(errors="ignore")
        print(request)

        headers = request.split('\n')
        if not headers or len(headers[0].split()) < 2:
            return

        method, path = headers[0].split()[:2]
        filename = resolve_path(path)
        full_path = os.path.join(WEB_ROOT, filename)

        if os.path.exists(full_path):
            content_type = get_mime_type(filename)
            try:
                # Legge file binari (immagini)
                if content_type.startswith("image/") or content_type == "application/octet-stream":
                    with open(full_path, 'rb') as f:
                        content = f.read()
                else:
                    # Legge file di testo
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                send_response(client_socket, 200, content, content_type)
                log_request(method, path, 200)
            except Exception as e:
                print(f"Errore nel caricamento del file: {e}")
                error_msg = "Errore nel caricamento della pagina"
                send_response(client_socket, 404, error_msg, "text/plain")
                log_request(method, path, 404)
        else:
            # File non trovato
            error_msg = "Pagina non trovata"
            send_response(client_socket, 404, error_msg, "text/plain")
            log_request(method, path, 404)
    finally:
        client_socket.close()

#Avvia il server e gestisce le connessioni in arrivo.
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server in ascolto su http://localhost:{PORT} ...")

        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket)

if __name__ == "__main__":
    start_server()
