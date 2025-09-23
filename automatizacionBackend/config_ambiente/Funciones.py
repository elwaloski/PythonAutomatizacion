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
import socket
import chardet
import shutil
import os

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

                    #detectando el encoding del archivo
                    with open(file_path, 'rb') as file:
                        resultado = chardet.detect(file.read())
                        encoding_detectado = resultado['encoding']

                    with open(file_path, "r", encoding=encoding_detectado) as file:
                        content = file.read()

                    new_content = content.replace(f"{Entrada}", f"{Salida}").replace(f"{EntradaWss}", f"{SalidaWss}") 
                    
                    if new_content != content:
                        with open(file_path, "w", encoding=encoding_detectado) as file:
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

def Configurar_Servicios_Windows(serviciosWindows):
    try:
        print("Configurando bats de servicios windows")
        logging.info("Se inicia la configuracion de los Servicios Windows")
        ip_mta = serviciosWindows["IpMTA"]
        servicios = serviciosWindows["Servicios"]
        ip_local = socket.gethostbyname(socket.gethostname()) 
        ruta = os.path.join(os.environ.get("Homedir"), "bin")
        logging.info(f"Ip del MTA: {ip_mta}")
        logging.info(f"Ip local: {ip_local}")
        logging.info(f"Path servicios: {ruta}")

        #recorrer servicios configurados
        for servicio in servicios:
            #leer archivo bat
            bat = servicio["Bat"]
            with open(f"{ruta}\\{bat}", "r") as file:
                lines = file.readlines()
        
            #reemplazar valores de archivo bat
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
            subprocess.run(comando_detener, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"servicio: {nombre_servicio} - detenido")

            comando_iniciar = f"net start {nombre_servicio}"
            subprocess.run(comando_iniciar, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"servicio: {nombre_servicio} - iniciado")

    except Exception as e:
        logging.error(f"Error Servicios Windows: {e}")

def OtrasConfig():
    try:
        logging.info("Se comienza con la modificacion del archivo sendJson.bat")
        ip_local = socket.gethostbyname(socket.gethostname()) 
        path = os.path.join(os.environ.get("homedir"), "bin\\sendJson.bat")
        logging.info(f"Ip local: {ip_local}")
        logging.info(f"Path sendJson: {path}")
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

def Configuracion_De_Bd(servidor, usuario, contrasena, bd):
    conexion = None
    cursor = None
    try:
        logging.info("Ejecutando script de usuarios en BD")
        logging.info("Comienza con la conexion y configuracion de la BD")
        logging.info(f"servidor: {servidor}")
        logging.info(f"usuario: {usuario}")
        logging.info(f"base de datos: {bd}")

        # Conexión a la base de datos
        conexion = pyodbc.connect(f'DRIVER=SQL Server;SERVER={servidor};DATABASE={bd};UID={usuario};PWD={contrasena}')
        cursor = conexion.cursor()
        logging.info("Conexión a BD realizada correctamente")
        print ("Conexión a BD realizada correctamente")

        # Leer y ejecutar el script SQL
        logging.info("Se comienza con la lectura y ejecución del script")
        with open("script_usuarios.sql", "r") as file:
            sql_script = file.read()
        
        comandos = sql_script.split('GO')  # Dividir el script en comandos por 'GO'

        for comando in comandos:
            if comando.strip():
                cursor.execute(comando)
                conexion.commit()
        
        logging.info("Se ejecutó el script correctamente en la BD")

    except pyodbc.DatabaseError as e:
        logging.error(f"Error en la base de datos: {e}")
    except pyodbc.InterfaceError as e:
        logging.error(f"Error en la interfaz de la base de datos: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
        logging.info("La conexión a la base de datos se ha cerrado de manera correcta")

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
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def ejecutar_bat_como_administrador(old_host, new_host,old_hostWSS, new_hostWSS):
    # Crear un archivo .bat temporal con las instrucciones adicionales
    bat_content = f"""
    set OldHost=fe{old_host.rstrip(".")}-admin.cl.dbnetcorp.com
    set NewHost=fe{new_host.rstrip(".")}-admin.cl.dbnetcorp.com
    powershell -Command "& {{Import-Module WebAdministration; Rename-Item 'IIS:\\Sites\\%OldHost%' %NewHost%}}"
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"
        
    set OldHost=cf{old_host}cl.dbnetcorp.com
    set NewHost=cf{new_host}cl.dbnetcorp.com
    powershell -Command "& {{Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&

    set OldHost=fe{old_host}cl.dbnetcorp.com
    set NewHost=fe{new_host}cl.dbnetcorp.com
    powershell -Command "& {{Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&

    set OldHost=fe{old_hostWSS}cl.dbnetcorp.com
    set NewHost=fe{new_hostWSS}cl.dbnetcorp.com
    powershell -Command "& {{Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&

    set OldHost=lce{old_host}cl.dbnetcorp.com
    set NewHost=lce{new_host}cl.dbnetcorp.com
    powershell -Command "& {{Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&
    powershell -Command "& {{Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}}"&
    exit&
    exit
    """
    logging.info("Se crea Archivo de Cambio de sitios y Binding")
    # Crea un archivo .bat temporal si no se proporciona ruta_bat
    ruta_bat = os.path.join(os.path.dirname(__file__), "temp_script.bat")
    with open(ruta_bat, 'w') as archivo_bat:
        archivo_bat.write(bat_content)

    # Verificar si el script está siendo ejecutado como administrador
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Si no es administrador, solicitar elevación
        print("Solicitando privilegios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{__file__}" "{ruta_bat}"', None, 1)
    else:
        # Ejecutar el archivo .bat como administrador
        try:
            subprocess.run(['cmd', '/c', ruta_bat], check=True)
            print("Script .bat ejecutado exitosamente.")
            logging.info("Script .bat ejecutado exitosamente. Cambio de sitios y Binding")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script .bat: {e}")
            logging.info(f"Error al ejecutar el script .bat: {e}")

def copiar_archivo(ruta_origen, ruta_destino):
    try:
        # Verifica si el archivo origen existe
        if not os.path.isfile(ruta_origen):
            raise FileNotFoundError(f"El archivo origen no existe: {ruta_origen}")
        # Copia el archivo
        shutil.copy(ruta_origen, ruta_destino)
        print(f"Archivo copiado de {ruta_origen} a {ruta_destino}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: Permiso denegado para copiar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

