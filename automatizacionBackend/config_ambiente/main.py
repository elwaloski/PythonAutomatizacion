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
        AliasHost = config["AliasHost"]
        Directorio=AliasHost["Directorio"]
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
        ServiciosWindows = config["ServiciosWindows"]
        Limpieza =config["Limpieza"]
        ExtensionesLimpieza = Limpieza["ExtensionesLimpieza"]
        RutasLimpieza = Limpieza["RutasLimpieza"]
        Dias = Limpieza["DiasAEliminar"]
        Activar=config["Activar"]
        CopiarArchivos=Activar["CopiarArchivos"] 
        ConfigurarAliasRDS=Activar["ConfigurarAliasRDS"]
        EjecutarScriptsBD=Activar["EjecutarScriptsBD"]
        ActualizarRutas=Activar["ActualizarRutas"]
        ActualizarSitios=Activar["ActualizarSitios"]
        CambiosIP=Activar["CambiosIP"]
        LimpiezaLogs=Activar["LimpiezaLogs"]

        if CopiarArchivos.upper() =="SI":
            Funciones.copiar_archivo('ArchivosActualizados\egate_config.cfg', 'D:\\facture_homes\\PROD_0277\\config\\par')
        elif CopiarArchivos == "NO" or not ConfigurarAliasRDS:
            print("No se Realizara copaido de Archivos  porque la opción es 'NO' o está vacía.")
        if ConfigurarAliasRDS.upper() =="SI":
            Funciones.Configurar_Alias_Rds(Servidor,Directorio)
        elif ConfigurarAliasRDS == "NO" or not ConfigurarAliasRDS:
            print("No se configurará el Alias RDS porque la opción es 'NO' o está vacía.")

        if EjecutarScriptsBD.upper() =="SI":
            Funciones.Configuracion_De_Bd(Servidor,Usuario,Contrasena,Bd)
        elif EjecutarScriptsBD == "NO" or not EjecutarScriptsBD:
            print("No se ejecutara Scripts de BD porque la opción es 'NO' o está vacía.")
        
        if ActualizarRutas.upper() =="SI": 
            Funciones.Configurar_Sitios_Webs_Wss_Apis_Etc(Rutas,Extensiones,Entrada,Salida,EntradaWss,SalidaWss)        
        elif ActualizarRutas == "NO" or not ActualizarRutas:
            print("No se Actualizan Rutas los  Sitios porque la opción es 'NO' o está vacía.")

        if ActualizarSitios.upper() =="SI":       
            Funciones.ejecutar_bat_como_administrador(Entrada,Salida,EntradaWss,SalidaWss)
        elif ActualizarSitios == "NO" or not ActualizarSitios:
            print("No se Actualizaran los  Sitios porque la opción es 'NO' o está vacía.")

        if CambiosIP.upper() =="SI":       
            Funciones.Configurar_Servicios_Windows(ServiciosWindows)
            Funciones.OtrasConfig()
        elif CambiosIP == "NO" or not CambiosIP:
            print("No se Cambiaran las  IP porque la opción es 'NO' o está vacía.")

        if LimpiezaLogs.upper() =="SI":   
            Funciones.EliminarLogs(RutasLimpieza,ExtensionesLimpieza,Dias)
        elif LimpiezaLogs == "NO" or not LimpiezaLogs:
            print("No se Limpiezan Logs porque la opción es 'NO' o está vacía.")
    
    except FileNotFoundError:
        logging.error("Error: Archivo de configuracion no encontrado")
        exit(1)

    except json.JSONDecodeError:
        logging.error("Error: El json de configuracion no tiene una estrcutura correcta")
        exit(1)
