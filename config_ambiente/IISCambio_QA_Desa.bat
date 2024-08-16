set OldHost=fe-qa-admin.cl.dbnetcorp.com
set NewHost=fe-desa-admin.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=cf-qa.cl.dbnetcorp.com
set NewHost=cf-desa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-qa.cl.dbnetcorp.com
set NewHost=fe-desa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-qa-wss.cl.dbnetcorp.com
set NewHost=fe-desa-wss.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&


set OldHost=lce-qa.cl.dbnetcorp.com
set NewHost=lce-desa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
exit&
exit