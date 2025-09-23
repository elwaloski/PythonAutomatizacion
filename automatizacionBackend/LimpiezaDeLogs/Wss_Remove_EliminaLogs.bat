@echo off
::
set SERVICE=EliminaLogs
nssm stop %SERVICE%
nssm remove %SERVICE% confirm
