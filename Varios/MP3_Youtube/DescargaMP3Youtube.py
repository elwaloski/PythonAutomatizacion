import os
import Funciones

if __name__ == "__main__":
    
    Funciones.CrearCompenentesPrincipales()
    Respuesta=Funciones.LeerArchivo()
    
    if Respuesta=='ArchivoLeido':
        try:
            SoloAudio=int(Funciones.SoloAudio)
            SoloVideo=int(Funciones.SoloVideo)
            AudioVideo=int(Funciones.AudioVideo)
            
            enlaces = []
            enlaces.clear()

            Funciones.clear()
            enlaces = Funciones.procesa_fichero('Enlances.txt')
            if SoloAudio==1 and SoloVideo==0 and AudioVideo==0:
                [Funciones.inicia_proceso_descargaMP3(x) for x in enlaces]
                os.startfile('Descargas\\')
            elif  SoloAudio==0 and SoloVideo==1 and AudioVideo==0:
                [Funciones.inicia_proceso_descargaVIDEO(x) for x in enlaces]
                os.startfile('Descargas\\video\\')
            elif  SoloAudio==0 and SoloVideo==0 and AudioVideo==1:
                [Funciones.inicia_proceso_descargaMP3(x) for x in enlaces]
                [Funciones.inicia_proceso_descargaVIDEO(x) for x in enlaces]
                os.startfile('Descargas\\')
                os.startfile('Descargas\\video\\')
            elif  SoloAudio==1 and SoloVideo==1 and AudioVideo==1:
                [Funciones.inicia_proceso_descargaMP3(x) for x in enlaces]
                [Funciones.inicia_proceso_descargaVIDEO(x) for x in enlaces]
                os.startfile('Descargas\\')
                os.startfile('Descargas\\video\\')
            elif  SoloAudio==1 and SoloVideo==1 and AudioVideo==0:
                [Funciones.inicia_proceso_descargaMP3(x) for x in enlaces]
                [Funciones.inicia_proceso_descargaVIDEO(x) for x in enlaces]
                os.startfile('Descargas\\')
                os.startfile('Descargas\\video\\')
            elif  SoloAudio==1 and SoloVideo==0 and AudioVideo==1:
                [Funciones.inicia_proceso_descargaMP3(x) for x in enlaces]
                [Funciones.inicia_proceso_descargaVIDEO(x) for x in enlaces]
                os.startfile('Descargas\\')
                os.startfile('Descargas\\video\\')
            elif  SoloAudio==0 and SoloVideo==0 and AudioVideo==0:
                input("Toda la Configuracion es 0 no se descargara nada...")
            elif  SoloAudio!=0 or SoloVideo!=0 or AudioVideo!=0 or SoloAudio!=1 or SoloVideo!=1 or AudioVideo!=1 :
                input("Error Config.txt ingrese el formato correcto a las variables SoloAudio, SoloVideo y Audio&Video ejemplo de configuracion\n SoloAudio 1\n SoloVideo 0\n Audio&Video 0\n\n Solo se aceptan valores  entre 0 o 1 Donde\n\n 1= a descargar\n 0= no descargar")
            input("Proceso Terminado Presiona Enter para salir...")
        
        except :
            print("Error Config.txt ingrese el formato correcto a las variables SoloAudio, SoloVideo y Audio&Video ejemplo de configuracion\n SoloAudio 1\n SoloVideo 0\n Audio&Video 0\n\n  Solo se aceptan valores entre 0 o 1 Donde\n\n 1 = a descargar 0 = no descargar")
    else:
        input("Archivo Config.txt no existe o no se puede leer")