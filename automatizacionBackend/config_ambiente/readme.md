# configAmbiente

## Descripción
Es un programa que automatiza la configuración del ambiente de QA entregado por el equipo de infraestructura

## Compilar
1. Para compilar debemos abrir una terminal en nuestro IDE o editor de texto
2. Nos ubicamos en el directorio del proyecto
3. Ejecutamos el comando pip install -r requirements.txt
4. Ejecutamos el comando python main.py

## Generar archivo .exe
1. Verificar que la libreria pyinstaller este instalada correctamente 
2. Ejecutar el comando: pyinstaller --name ConfgiAmbiente --onefile main.py
   
### Importante!!!
Debido a permisos de la empresa puede que no se nos permita agregar la path de la libreria por lo cual el comando seria el siguiente(recuerda cambiar usuario): 
C:\Users\{usuario}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe --name ConfgiAmbiente --onefile main.py

## Instalación
1. Generar una carpeta que contenga la siguiente estructura
   -ConfigAmbiente.exe
   -config.json
   -script_usuarios.sql
   -logs (esta es una carpeta)
2. Dejar esta carpeta dentro del ambienteQA en una ubicación a gusto que te permita ejectuar con comodidad el archivo .exe

## Configuraciones:
Para el correcto funcionamiento del ConfigAmbiente.exe se debe configurar el archivo config.json

## Ejecucion
De momento lo recomendable es realizar ejecutar el arhivo.exe en como Administrador


