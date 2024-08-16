import pyodbc
import os
import subprocess
import re
import logging
import datetime
import time
import shutil 
import ctypes
import sys

def Configurar_Alias_Rds(servidor,Directorio):
    try:
        respaldo_archivo = Directorio + ".bak"
        logging.info(f"Respaldo Directorio : {Directorio} .bak")
        contador = 1
        while os.path.exists(respaldo_archivo):
            respaldo_archivo = f"{Directorio}.bak_{contador}"            
            contador += 1
        logging.info(f"Respaldo Directorio : {Directorio} .bak{contador}")
        shutil.copy(Directorio, respaldo_archivo)

        with open(Directorio, 'r') as archivo:
            lineas = archivo.readlines()

        with open(Directorio, 'w') as archivo:
            for linea in lineas:
                if '<add key="nombrePing"' in linea:
                    logging.info(f"Valor antes del cambio: {linea.lstrip()}")
                    linea = f'		<add key="nombrePing" value="{servidor}"/>\n'
                    logging.info(f"Nuevo Valor :{linea.lstrip()}")
                archivo.write(linea)
        print("Modificación de ALIAS BD RDS completada.")

        #reiniciar los servicios windows
        nombre_servicio = "UpdateHostService"
        comando_detener = f"net stop {nombre_servicio}"
        proceso = subprocess.run(comando_detener, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(f"servicio: {nombre_servicio} - detenido")

        
        comando_iniciar = "net start UpdateHostService"
        proceso = subprocess.run(comando_iniciar, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(f"servicio: UpdateHostService - iniciado")
    except Exception as e:
        logging.error(f"Error en cambiar Alias por no encontrar la ruta o por algun problemas de permisos : {e}")

def EliminarLogs(RutasLimpieza,ExtensionesLimpieza,Dias):
    try:
        print(f"Elimina logs según rutas configuradas que tengan más de {Dias} días de antigüedad")
        for rutax in RutasLimpieza:
            logging.info(f"Directorio a buscar: {rutax}")
            for root, dirs, files in os.walk(rutax):
                for filename in files:
                    file_extension = os.path.splitext(filename)[1].lower()
                    if file_extension not in ExtensionesLimpieza:
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

def Configurar_Sitios_Webs_Wss_Apis_Etc(rutas,extensiones,Entrada,Salida,EntradaWss,SalidaWss):
    #configurar sitios webs, wss, apis, etc
    try:
        print("Modificando archivos de configuracion de webs, wss y apis")
        for ruta in rutas:
            logging.info(f"Directorio a buscar: {ruta}")
            for root, dirs, files in os.walk(ruta):
                for filename in files:
                    file_extension = os.path.splitext(filename)[1].lower()
                    if file_extension not in extensiones:
                        continue
                    if filename == "dbnetkeystore":
                        continue

                    file_path = os.path.join(root, filename)
                    logging.info(f"Leyendo archivo: {file_path}" )
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()

                    new_content = content.replace(f"{Entrada}", f"{Salida}").replace(f"{EntradaWss}", f"{SalidaWss}") 
                    
                    if new_content != content:
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(new_content)
                        logging.info(f"Se ha modificado el siguiente archivo: {file_path}")
        #reiniciar iis
        print("Reiniciando iis...")
        logging.info("Reiniciando iis...")
        subprocess.run("iisreset", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Se reinicia el iis de manera correcta")
        logging.info("Se reinicia el iis de manera correcta")

    except Exception as e:
        logging.error(f"Error: {e}")

#configurar servicios windows
def Configurar_Servicios_Windows(serviciosWindows):
    try:
        print("Configurando bats de servicios windows")
        logging.info("Se inicia la configuracion de los Servicios Windows")
        ip_mta = serviciosWindows["IpMTA"]
        ip_local = serviciosWindows["IpLocal"]
        ruta = serviciosWindows["Ruta"]
        servicios = serviciosWindows["Servicios"]

        #leer archivo bat
        for servicio in servicios:
            bat = servicio["Bat"]
            with open(f"{ruta}\\{bat}", "r") as file:
                lines = file.readlines()
        
            #reemplazar valores de archivo
            with open(f"{ruta}\\{bat}", "w", encoding='utf-8') as file:
                for line in lines:
                    if line.startswith("set IP="):
                        file.write(f'set IP={ip_local}\n')
                    elif line.startswith("set URL_OUTBOX_NOTIFIY="):
                        file.write(f"set URL_OUTBOX_NOTIFIY=http://{ip_mta}:4015/json/message/")
                    else:
                        file.write(line)
            logging.info(f"BAT: {bat} modificada")

            #reiniciar los servicios windows
            nombre_servicio = servicio["Nombre"]
            comando_detener = f"net stop {nombre_servicio}"
            proceso = subprocess.run(comando_detener, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"servicio: {nombre_servicio} - detenido")

            comando_iniciar = f"net start {nombre_servicio}"
            proceso = subprocess.run(comando_iniciar, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"servicio: {nombre_servicio} - iniciado")

    except Exception as e:
        logging.error(f"Error Servicios Windows: {e}")


def OtrasConfig(serviciosWindows):
    try:
        ip_local = serviciosWindows["IpLocal"]
        logging.info("Se comienza con la modificacion del archivo sendJson.bat")
        path = os.path.join(os.environ.get("homedir"), "bin\\sendJson.bat")
        with open(path, "r") as file:
            lines = file.readlines()

        with open(path, "w") as file:
            for line in lines:
                new_content = re.sub(r'http://\d+\.\d+\.\d+\.\d+:\d+', f'http://{ip_local}:4012', line)
                file.write(new_content)
        logging.info("Se ha modificado el arhivo sendJson.bat de manera correcta")     
    except Exception as e:
        logging.info(f"Error otras config {e}")
    
    logging.info("CONFIGURACIONES TERMINADAS")
    print("CONFIGURACIONES TERMINADAS")


    #configuracion de bd
def Configuracion_De_Bd(servidor,usuario,contrasena,bd):
    conexion = None
    cursor = None
    try:
        print("Ejecutando script de usuarios en BD")
        logging.info("Comienza con la conexion y configuracion de la BD")
        logging.info(f"servidor: {servidor}")
        logging.info(f"usuario: {usuario}")
        logging.info(f"contraseña: {contrasena}")
        logging.info(f"base de datos: {bd}")

        conexion = pyodbc.connect(f'DRIVER=SQL Server;SERVER={servidor};DATABASE={bd};UID={usuario};PWD={contrasena}')
        cursor = conexion.cursor()
        logging.info("Conexion a BD realizada correctamente")

        #ejectuar script usuarios
        logging.info("Se comienza con la lectura y ejecucion del script")
        with open("script_usuarios.sql", "r") as file:
            sql_script = file.read()
        
        comandos = sql_script.split('GO')

        for comando in comandos:
            if comando.strip():
                cursor.execute(comando)
                conexion.commit()
        # cursor.execute(sql_script)
        # conexion.commit()
        logging.info("Se ejecuta el script correctamente en BD")

    except pyodbc.DatabaseError as e:
        logging.error(f"Error en BD: {e}")
    except pyodbc.InterfaceError as e:
        logging.error(f"Error en BD: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()
        logging.info("La conexion a BD se ha cerrado de manera correcta")

def CrearLogs():
    if not os.path.exists("logs"):
        try:
            os.makedirs("logs")
        except OSError as e:
            print(f"Se producto al crear un el directorio: 'logs' - {e}")
    #Configuracion log
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    logging.basicConfig(
        filename=f"logs/log_{fecha_actual}.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
def ejecutar_bat_como_administrador(ruta_bat):
    # Verificar si el script está siendo ejecutado como administrador
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Si no es administrador, solicitar elevación
        print("Solicitando privilegios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{__file__}"', None, 1)
    else:
        # Ejecutar el archivo .bat como administrador
        try:
            subprocess.run(['cmd', '/c', ruta_bat], check=True)
            print("Script .bat ejecutado exitosamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script .bat: {e}")