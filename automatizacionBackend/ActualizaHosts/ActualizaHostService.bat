@echo off
::
SET pwd=%~dp0
SET MyPathApp=%pwd:~,-1%
CD /D %MyPathApp%
::
echo MyPathApp=%MyPathApp%

set SERVICE=ActualizaHost
set MyExe=ActualizaHost.exe
::
nssm install %SERVICE% %MyPathApp%\%MyExe%
::::
:::: Application tab
nssm set %SERVICE% Application %MyPathApp%\%MyExe%
nssm set %SERVICE% AppDirectory %MyPathApp%
::::
:::: Details tab
nssm set %SERVICE% DisplayName ActualizaHost
nssm set %SERVICE% Description ActualizaHost: Actualiza archivo host.
nssm set %SERVICE% Start SERVICE_AUTO_START
::::
:::: I/O tab
nssm set %SERVICE% AppStdout %MyPathApp%\logs\ActualizaHost_output.log
nssm set %SERVICE% AppStderr %MyPathApp%\logs\ActualizaHost_error.log
echo Servicio %SERVICE% instalado con exito.
pause

