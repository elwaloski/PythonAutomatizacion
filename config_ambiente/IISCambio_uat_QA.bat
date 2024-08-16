set OldHost=fe-uat-admin.cl.dbnetcorp.com
set NewHost=fe-qa-admin.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=cf-uat.cl.dbnetcorp.com
set NewHost=cf-qa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-uat.cl.dbnetcorp.com
set NewHost=fe-qa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-uatwss.cl.dbnetcorp.com
set NewHost=fe-qa-wss.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&


set OldHost=lce-uat.cl.dbnetcorp.com
set NewHost=lce-qa.cl.dbnetcorp.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
exit&
exit