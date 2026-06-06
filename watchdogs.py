import sys
import time
import random
import os
import shutil

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError:
    print("O módulo watchdog não está instalado.")
    print("Instale com: python -m pip install watchdog")
    raise

home_dir = os.path.expanduser("~")
from_dir = os.path.join(home_dir, "Downloads")
to_dir = os.path.join(from_dir, "Arquivos_baixados")

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        print("Evento criado:", event.src_path)

        filename = os.path.basename(event.src_path)
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        time.sleep(1)

        for key, extensions in dir_tree.items():
            if extension in extensions:
                dest_dir = os.path.join(to_dir, key)
                dest_path = os.path.join(dest_dir, filename)

                if not os.path.exists(event.src_path):
                    print("Arquivo não encontrado:", event.src_path)
                    return

                os.makedirs(dest_dir, exist_ok=True)
                print("movendo", filename, "para", dest_dir)

                try:
                    shutil.move(event.src_path, dest_path)
                except Exception as exc:
                    print("Erro ao mover arquivo:", exc)
                time.sleep(1)
                break

    def on_deleted(self, event):
        print(f"opa, alguem me excluiu {event.src_path}!")


# Inicialize a Classe Gerenciadora de Eventos
if not os.path.exists(from_dir):
    print(f"O diretório de origem não existe: {from_dir}")
    sys.exit(1)

os.makedirs(to_dir, exist_ok=True)

event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("o programa foi interrompido")
    observer.stop()
    observer.join()
