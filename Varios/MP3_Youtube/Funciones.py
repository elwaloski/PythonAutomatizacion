import logging
import os
from moviepy.editor import *
import datetime
from pytube import YouTube

contador=0

def inicia_proceso_descargaMP3(link):
    
    try:
        yt = YouTube(link)   
        try:            
            nombre_completo = f"{yt.title} - {yt.author}.mp4"
            Nuevo_nombre=nombre_completo.replace('|', '').replace('"', '').replace("'", '').replace("*", '').replace("/", '').replace("\\", '').replace("#", '').replace("$", '').replace("%", '').replace("?", '').replace("¿", '').replace("+", '')
            
            print('')
            print('-------------------------------------------------------')
            print('Título: {0}'.format(yt.title))
            print('Autor: {0}'.format(yt.author))
            print('')    
            
            ruta_fin = yt.streams.get_audio_only().download('Descargas\\', filename=Nuevo_nombre)
            audioclip = AudioFileClip(ruta_fin)
            audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
            
            os.remove(audioclip.filename)
            print_proceso_terminado()
            Numero=funcion_incrementa_contador()
            logINFO(f"Descarga Exitosa numero {Numero} link de Youtube {link}", "INFO")
        except:
            Numero=funcion_incrementa_contador()
            print(f'Error en la descarga numero {Numero} link de Youtube {link}')
            logINFO(f"Error en la descarga numero {Numero} link de Youtube {link}", "ERROR")
    except:
        Numero=funcion_incrementa_contador()
        print('Error en el link: {0}'.format(link))
        logINFO(f"Error en la descarga numero {Numero} link no es de Youtube {link}", "ERROR")
        return         
    
def inicia_proceso_descargaVIDEO(link):
    parent_dir='Descargas\\'
    try:
        yt = YouTube(link)   
        try:            
            nombre_completo = f"{yt.title} - {yt.author}.mp4"
            Nuevo_nombre=nombre_completo.replace('|', '').replace('"', '').replace("'", '').replace("*", '').replace("/", '').replace("\\", '').replace("#", '').replace("$", '').replace("%", '').replace("?", '').replace("¿", '').replace("+", '')
            
            print('')
            print('-------------------------------------------------------')
            print('Título: {0}'.format(yt.title))
            print('Autor: {0}'.format(yt.author))
            print('')    
            vids = yt.streams.filter(mime_type="video/mp4").order_by('resolution').desc()

            nombre_video = vids[0].default_filename
            vids[0].download(parent_dir + '/video')

            yt.streams.get_audio_only().download(parent_dir + '/audio')

            audioclip = AudioFileClip(parent_dir + '/audio/' + nombre_video)

            videoclip2 = VideoFileClip(parent_dir + '/video/' + nombre_video)
            videoclip2 = videoclip2.set_audio(audioclip)

            videoclip2.write_videofile(parent_dir + '/video/' + Nuevo_nombre)

            os.remove(videoclip2.filename)
            os.remove(audioclip.filename)
            
            logINFO(f"Descarga Exitosa video numero {Numero} link de Youtube {link}", "INFO")
        except:
            Numero=funcion_incrementa_contador()
            print(f'Error en la descarga de video numero {Numero} link de Youtube {link}')
            logINFO(f"Error en la descarga de video numero {Numero} link de Youtube {link}", "ERROR")
    except:
        Numero=funcion_incrementa_contador()
        print('Error en el link: {0}'.format(link))
        logINFO(f"Error en la descarga de video  numero {Numero} link no es de Youtube {link}", "ERROR")
        return         

fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_archivo_log = f'DescargaYoutube_{fecha_hora_actual}.log'
logging.basicConfig(filename=nombre_archivo_log, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def logINFO(message, tipodelog):
    # Utiliza getLogger para obtener un objeto de registro específico
    logger = logging.getLogger(tipodelog.lower() + '_logger')

    # Utiliza el manejador para registrar el mensaje
    logger.info(message)

    
# Windows
def clear(): os.system('cls')

def print_proceso_terminado():
    print('Descarga completada')
    print('-------------------------------------------------------')

def procesa_fichero(ruta) -> list:
    list_enlaces = []
    file_object = open(ruta, 'r')
    [list_enlaces.append(linea) for linea in file_object]
    file_object.close()
    return list_enlaces

# Define una función que incrementa el contador
def funcion_incrementa_contador():
    global contador  # Indica que se usará la variable global
    contador += 1
    return contador

def CrearCompenentesPrincipales():
    dir_name="Descargas"
    file_name = "Enlances.txt"
    Config_name="Config.txt"
    try:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)  
    except:
        print('No se puede crear Carpeta Descargas Puede que sea por que no tiene !!!')
    
    try:
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write("https://www.youtube.com/watch?v=_YVGUj2bnWo&list=RDCqKV2iMHIDw&index=27")
            print(f"Archivo '{file_name}' creado.")
    except:
        print('No se puede crear Archivo Enlances.txt Puede que sea por que no tiene permisos!!!')
        
    try:
        if not os.path.exists(Config_name):
            with open(Config_name, 'w') as file:
                file.write("SoloAudio 1\n")
                file.write("SoloVideo 0\n")
                file.write("Audio&Video 0\n")
            print(f"Archivo '{Config_name}' creado.")
    except:
        print('No se puede crear Archivo Enlances.txt Puede que sea por que no tiene permisos!!!')
        
def LeerArchivo():
    global SoloAudio
    global SoloVideo
    global AudioVideo

    ruta_archivo = "Config.txt"
    try:
        if os.path.exists(ruta_archivo):
            try:
                with open(ruta_archivo, "r") as archivo:
                    for linea in archivo:
                        if linea.startswith("SoloAudio"):
                            mp3 = linea.split()[1]
                            SoloAudio=mp3
                        elif linea.startswith("SoloVideo"):
                            video = linea.split()[1]
                            SoloVideo=video
                        elif linea.startswith("Audio&Video"):
                            ambos = linea.split()[1]
                            AudioVideo=ambos             
                            
                return "ArchivoLeido"
            except:
                print('Archivo Config.txt mal configurado ingrese el formato correcto a las variables SoloAudio, SoloVideo y Audio&Video ejemplo de configuracion\n SoloAudio 1\n SoloVideo 0\n Audio&Video 0\n\n Solo se aceptan valores  entre 0 o 1 Donde\n\n 1= a descargar\n 0= no descargar!!!')
        else:
            print("El archivo Config.txt no existe .")
            return "Error"
    except:
        print('Error en leer archivo Config.txt!!!')