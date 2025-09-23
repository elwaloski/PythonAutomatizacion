import json
import os
import logging
import datetime
import time

class Main():

    if not os.path.exists("logs"):
        try:
            os.makedirs("logs")
        except OSError as e:
            print(f"Se producto al crear un el directorio: 'logs' - {e}")
    #Configuracion log
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logging.basicConfig(
        filename=f"logs/log_{fecha_actual}.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    print("Se inicia el proceso de configuracion del ambiente")
    #Leer archivo de configuraciones
    try:
        print("Leyendo archivo de configuraciones...")
        logging.info("Leyendo archivo de configuracion")

        with open("config.json", "r") as archivo:
            config = json.load(archivo)

        limpieza =config["limpieza"]
        extensiones = limpieza["extensiones"]
        rutas = limpieza["rutas"]
        Dias = limpieza["DiasAEliminar"]
    
    except FileNotFoundError:
        logging.error("Error: Archivo de configuracion no encontrado")
        exit(1)

    except json.JSONDecodeError:
        logging.error("Error: El json de configuracion no tiene una estrcutura correcta")
        exit(1)

    # Eliminar logs segun dias configurados
    try:
        print(f"Elimina logs según rutas configuradas que tengan más de {Dias} días de antigüedad")
        for ruta in rutas:
            logging.info(f"Directorio a buscar: {ruta}")
            for root, dirs, files in os.walk(ruta):
                for filename in files:
                    file_extension = os.path.splitext(filename)[1].lower()
                    if file_extension not in extensiones:
                        continue
                    
                    file_path = os.path.join(root, filename)
                    
                    # Obtén el tiempo de modificación del archivo
                    file_mtime = os.path.getmtime(file_path)
                    # Calcula la antigüedad en días
                    file_age_days = (time.time() - file_mtime) / (24 * 3600)
                    
                    if file_age_days > int(Dias):
                        try:
                            os.remove(file_path)
                            logging.info(f"Archivo eliminado: {file_path}")
                        except Exception as e:
                            logging.error(f"No se pudo eliminar el archivo {file_path}: {e}")
    except Exception as e:
        logging.error(f"Error en la limpieza: {e}")