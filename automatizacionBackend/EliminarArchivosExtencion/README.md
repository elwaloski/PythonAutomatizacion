Programa python para Eliminar archivos por extencion segun los dias de vigencia de este mismo <br>
para pasar de .py a exe pyinstaller --onefile EliminaLogs.py <br>

{ <br>
    "limpieza":<br>
    {<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "extensiones": [".mp3"],  ** |.extencion ejemplo .log este puede tener N variables que se separan por coma ejemplo [".mp3",".log",".txt"]**<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "rutas": ["D:\\\prueba\\\prueba"], **| Rutas de donde buscara los archivos con esas extenciones esta igual pueden ser N ["C:\\\","D:\\\"]**<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "DiasAEliminar":"7" **| Dias de eliminacion ejemplo fecha de hoy menos 7 dias si estos son mas viejo que 7 dias se eliminaran**<br>
    }<br>
}<br>
