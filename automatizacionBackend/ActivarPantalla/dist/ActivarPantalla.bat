@echo off
::
SET pwd=%~dp0
SET MyPathApp=%pwd:~,-1%
CD /D %MyPathApp%
::
echo MyPathApp=%MyPathApp%

set SERVICE=ActivarPantalla
set MyExe=ActivarPantalla.exe
::
nssm install %SERVICE% %MyPathApp%\%MyExe%
::::
:::: Application tab
nssm set %SERVICE% Application %MyPathApp%\%MyExe%
nssm set %SERVICE% AppDirectory %MyPathApp%
::::
:::: Details tab
nssm set %SERVICE% DisplayName ActivarPantalla
nssm set %SERVICE% Description ActivarPantalla: Activar Pantalla para no suspender Equipo.
nssm set %SERVICE% Start SERVICE_AUTO_START
::::
:::: I/O tab
nssm set %SERVICE% AppStdout %MyPathApp%\logs\ActivarPantallat_output.log
nssm set %SERVICE% AppStderr %MyPathApp%\logs\ActivarPantalla_error.log
echo Servicio %SERVICE% instalado con exito.
pause

