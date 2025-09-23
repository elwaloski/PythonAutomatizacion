set OldHost=fe-uat-admin.cl.xxxxxx.com
set NewHost=fe-qa-admin.cl.xxxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=cf-uat.cl.xxxxxx.com
set NewHost=cf-qa.cl.xxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-uat.cl.xxxxxxx.com
set NewHost=fe-qa.cl.xxxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-uatwss.cl.xxxxxx.com
set NewHost=fe-qa-wss.cl.xxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&


set OldHost=lce-uat.cl.xxxxxxx.com
set NewHost=lce-qa.cl.xxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
exit&
exit