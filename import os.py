import os
import shutil
from datetime import datetime, timedelta

def move_to_trash_and_delete(images_folder, trash_folder, delete_after_days=2):
    # Überprüfe und erstelle die Ordner falls notwendig
    for folder in [images_folder, trash_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Liste alle Dateien im Download-Ordner auf
    for filename in os.listdir(images_folder):
        src_path = os.path.join(images_folder, filename)
        if os.path.isfile(src_path) and is_image_file(filename):  # Nur Bilddateien berücksichtigen
            dest_path = os.path.join(trash_folder, filename)
            # Verschiebe das Bild in den Trash-Ordner
            shutil.move(src_path, dest_path)
            print(f"{filename} wurde in den Trash-Ordner verschoben.")
    
    # Lösche Dateien im Trash-Ordner, die älter als delete_after_days sind
    # Lösche Dateien im Trash-Ordner, die älter als delete_after_days sind
    delete_cutoff_date = datetime.now() - timedelta(days=delete_after_days)
    for filename in os.listdir(trash_folder):
        file_path = os.path.join(trash_folder, filename)
        if os.path.isfile(file_path):
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if creation_time < delete_cutoff_date:
                os.remove(file_path)
                print(f"{filename} wurde aus dem Trash-Ordner gelöscht.")

def is_image_file(filename):
    return filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))

# Beispielaufruf der Funktion
user_name = os.getlogin()  # Dies erfasst den Benutzernamen des aktuell angemeldeten Benutzers
download_folder = os.path.join("C:\\Users", user_name, "Downloads")
trash_folder = os.path.join("C:\\Users", user_name, "Documents", "Trash")

# Überprüfe, ob der Ordner bereits existiert, andernfalls erstelle ihn
if not os.path.exists(trash_folder):
    os.makedirs(trash_folder)
    print("Ordner erstellt:", trash_folder)
else:
    print("Ordner existiert bereits:", trash_folder)


move_to_trash_and_delete(download_folder, trash_folder)
