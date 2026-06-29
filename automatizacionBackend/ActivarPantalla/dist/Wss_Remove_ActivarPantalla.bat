@echo off
::
set SERVICE=ActivarPantalla
nssm stop %SERVICE%
nssm remove %SERVICE% confirm
