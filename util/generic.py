from pathlib import Path
from PIL import ImageTk, Image

def leer_imagen(nombre_archivo, size):
    # Obtén la ruta absoluta al script principal
    ruta_script_principal = Path(__file__).resolve().parent
    # Construye la ruta completa al archivo de imagen
    ruta_imagen = ruta_script_principal / nombre_archivo
    try:
        # Intenta abrir la imagen
        imagen = Image.open(ruta_imagen).resize(size)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_imagen}")
        return None

def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")