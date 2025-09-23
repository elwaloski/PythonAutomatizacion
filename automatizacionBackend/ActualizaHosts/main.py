import os
import logging
from socket import gethostbyname, gaierror
from datetime import datetime
import json
import time

def setup_logging():
    log_path = get_log_file_path()
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("Servicio Activo")

def get_log_file_path():
    log_path = os.getenv('LOG_PATH', 'Logs')
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    return os.path.join(log_path, f"Log-{datetime.today().strftime('%d-%m-%Y')}.txt")

def update_hosts_file(host_name_or_address, url_variable_local):
    try:
        logging.info("Iniciando proceso de validación")        
        # Obtén la unidad del sistema (C: por defecto)
        system_drive = os.getenv('SystemDrive', 'C:')
        
        # Construye la ruta al archivo hosts
        path = os.path.join(system_drive, '\\Windows', 'System32', 'drivers', 'etc', 'hosts')
        
        # Lee el archivo hosts
        with open(path, 'r') as file:
            lines = file.readlines()
        
        # Busca la línea con la entrada específica
        host_addresss = gethostbyname(host_name_or_address)
        LineaConsultar = f"{host_addresss} {url_variable_local}"
        str1 = ''
        for line in lines:
            if LineaConsultar in line:
                str1 = line.strip()
        if  str1== LineaConsultar:
            logging.info(f"No se actualizara {LineaConsultar} por que no a cambiado IP")
        else:
            # Filtra todas las líneas que contengan la URL específica
            filtered_lines = []
            for line in lines:
                # Verifica si la línea contiene exactamente la variable en un formato específico
                if url_variable_local in line:
                    # Comprueba si la línea contiene exactamente la variable (considerando espacios)
                    if not line.strip().startswith(url_variable_local) and not line.strip().endswith(url_variable_local):
                        filtered_lines.append(line)
                    else:
                        logging.info(f"Eliminada línea: {line.strip()}")
                else:
                    filtered_lines.append(line)
            
            try:
                # Obtén la dirección IP del nombre de host
                host_address = gethostbyname(host_name_or_address)
                str2 = f"\n{host_address} {url_variable_local}"                
                # Añade la nueva entrada a las líneas filtradas
                filtered_lines.append(str2)
                
                # Escribe el archivo actualizado
                with open(path, 'w') as file:
                    file.writelines(filtered_lines)
                    
                    logging.info(f"Cambio de IP: {host_address} {url_variable_local}")
                    logging.info(f"Archivo de host actualizado: {host_address} {url_variable_local}")
                
                with open(path, 'r') as infile:
                    lines = infile.readlines()
                non_empty_lines = [line for line in lines if line.strip()]
                with open(path, 'w') as outfile:
                    outfile.writelines(non_empty_lines)
                    
            except gaierror as e:
                logging.error(f"DNS Error: {e}")
            
            logging.info("Fin del proceso de validación")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    setup_logging()
    with open("config.json", "r") as archivo:
        config = json.load(archivo)
        Configuracion1 = config["Configuracion1"]
        PING1=Configuracion1["PING1"]
        NombreVariable1 = Configuracion1["NombreVariable1"]
        Configuracion2 = config["Configuracion2"]
        PING2=Configuracion2["PING2"]
        NombreVariable2 = Configuracion2["NombreVariable2"]
        
    while True:  # Bucle infinito 
        if  PING1 !="" and NombreVariable1!="":
            update_hosts_file(PING1,NombreVariable1)
        else:
            logging.info("Configuracion1 incompleta no se ejecutara")

        if  PING2 !="" and NombreVariable2!="":
            update_hosts_file(PING2,NombreVariable2)
        else:
            logging.info("Configuracion2 incompleta no se ejecutara")
        time.sleep(180)  # Esperar 3 minutos (180 segundos)
