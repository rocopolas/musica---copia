import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TRCK

def renombrar_archivos(directorio):
    for carpeta_raiz, subcarpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            # Solo procesamos archivos .mp3
            if archivo.lower().endswith('.mp3'):
                ruta_completa = os.path.join(carpeta_raiz, archivo)
                nombre, extension = os.path.splitext(archivo)
                
                indice_guion = nombre.split('-')
                
                audio = MP3(ruta_completa, ID3=ID3)
                numero_de_pista = str(audio.get('TRCK')).split("/")[0]
                
                nuevo_nombre = f"{numero_de_pista} {indice_guion[1]}{extension}"
                nueva_ruta = os.path.join(carpeta_raiz, nuevo_nombre)
                
                os.rename(ruta_completa, nueva_ruta)

if __name__ == "__main__":
    # Especifica la ruta del directorio que deseas procesar
    directorio = "D:\Descargas\musica - copia"
    renombrar_archivos(directorio)