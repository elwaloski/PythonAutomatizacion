@echo off
::
set SERVICE=ActualizaHost
nssm stop %SERVICE%
nssm remove %SERVICE% confirm
