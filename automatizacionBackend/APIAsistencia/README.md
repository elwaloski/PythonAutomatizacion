Componente de asistencia automatica para la aplicacion BUK <br>
Se adjuntar archivo <br>

config.CFG donde tenermos <br>
-RUT <br>
-URLEntrada<br>
-URLSalida <br>
-EnvioMail <br>
-MailDestino <br><br>

donde su ejemplo de llenado es <br>
-RUT 55555555-9<br>
-URLEntrada https://app.ctrlit.cl/ctrl/dial/registrarweb/cEwcXjodiX?i=1&lat=&lng=&r=<br>
-URLSalida https://app.ctrlit.cl/ctrl/dial/registrarweb/cEwcXjodiX?i=0&lat=&lng=&r=<br>
-EnvioMail SI<br>
-MailDestino aaaaaaa@hotmail.com<br>
el mail destino es para que nos llegue otro mail a otro correo para verificar si se realizo la accion o no el cual es opcional<br><br>

Para crear ejecutable .exe se debe ocupar <br>
pyinstaller<br>
instalacion<br>
pip install pyinstaller<br><br>

crear ejecutable<br>
pyinstaller --onefile MetedoGETEntrada.py<br>
pyinstaller --onefile MetodoGETSalida.py<br><br>

Se agregan Tareas programadas para su ejecucion en windows las cuales es solo importar y modificar hora de entrada,salida y direccion de donde se debe ejecutar los Ejecutables<br>

