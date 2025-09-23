@echo off
::
SET pwd=%~dp0
SET MyPathApp=%pwd:~,-1%
CD /D %MyPathApp%
::
echo MyPathApp=%MyPathApp%

set SERVICE=EliminaLogs
set MyExe=EliminaLogs.exe
::
nssm install %SERVICE% %MyPathApp%\%MyExe%
::::
:::: Application tab
nssm set %SERVICE% Application %MyPathApp%\%MyExe%
nssm set %SERVICE% AppDirectory %MyPathApp%
::::
:::: Details tab
nssm set %SERVICE% DisplayName EliminaLogs
nssm set %SERVICE% Description EliminaLogs: Eliminar logs cada N dias.
nssm set %SERVICE% Start SERVICE_AUTO_START
::::
:::: I/O tab
nssm set %SERVICE% AppStdout %MyPathApp%\logs\EliminaLogs_output.log
nssm set %SERVICE% AppStderr %MyPathApp%\logs\EliminaLogs_error.log
echo Servicio %SERVICE% instalado con exito.
pause

