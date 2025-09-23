set OldHost=fe-qa-admin.cl.xxxxxx.com
set NewHost=fe-desa-admin.cl.xxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=cf-qa.cl.xxxxx.com
set NewHost=cf-desa.cl.xxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-qa.cl.xxxxxx.com
set NewHost=fe-desa.cl.xxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&

set OldHost=fe-qa-wss.cl.xxxxxxx.com
set NewHost=fe-desa-wss.cl.xxxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&


set OldHost=lce-qa.cl.xxxxxxx.com
set NewHost=lce-desa.cl.xxxxxxx.com
powershell -Command "& {Import-Module WebAdministration; Rename-Item "IIS:\Sites\%OldHost%" %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:80:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
powershell -Command "& {Import-Module WebAdministration; Set-WebBinding -Name %NewHost% -BindingInformation '*:443:%OldHost%' -PropertyName HostHeader -Value %NewHost%}"&
exit&
exit