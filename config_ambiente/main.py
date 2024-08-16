import json
import logging
import Funciones

class Main():

    Funciones.CrearLogs()

    print("Se inicia el proceso de configuracion del ambiente")
    #Leer archivo de configuraciones
    try:
        print("Leyendo archivo de configuraciones...")
        logging.info("Leyendo archivo de configuracion")

        with open("config.json", "r") as archivo:
            config = json.load(archivo)
        AliasHots = config["AliasHots"]
        Directorio=AliasHots["Directorio"]
        Config_bd = config["ConexionBD"]
        Servidor = Config_bd["Servidor"]
        Usuario = Config_bd["Usuario"]
        Contrasena = Config_bd["Contrasena"]
        Bd = Config_bd["BaseDatos"]
        Sitios = config["Sitios"]
        Entrada=Sitios["Entrada"]
        Salida=Sitios["Salida"]
        EntradaWss=Sitios["EntradaWss"]
        SalidaWss=Sitios["SalidaWss"]
        Extensiones = Sitios["Extensiones"]
        Rutas = Sitios["Rutas"]
        NombreBat = Sitios["NombreBat"]
        ServiciosWindows = config["ServiciosWindows"]
        Limpieza =config["Limpieza"]
        ExtensionesLimpieza = Limpieza["ExtensionesLimpieza"]
        RutasLimpieza = Limpieza["RutasLimpieza"]
        Dias = Limpieza["DiasAEliminar"]
        
        Funciones.Configurar_Alias_Rds(Servidor,Directorio)        
        Funciones.Configuracion_De_Bd(Servidor,Usuario,Contrasena,Bd)
        Funciones.EliminarLogs(RutasLimpieza,ExtensionesLimpieza,Dias)
        Funciones.ejecutar_bat_como_administrador(NombreBat)
        Funciones.Configurar_Sitios_Webs_Wss_Apis_Etc(Rutas,Extensiones,Entrada,Salida,EntradaWss,SalidaWss)
        Funciones.Configurar_Servicios_Windows(ServiciosWindows)
        Funciones.OtrasConfig(ServiciosWindows)
    
    except FileNotFoundError:
        logging.error("Error: Archivo de configuracion no encontrado")
        exit(1)

    except json.JSONDecodeError:
        logging.error("Error: El json de configuracion no tiene una estrcutura correcta")
        exit(1)
