use cf_cl_cert
DROP USER cf_uat_app
DROP USER fe_uat_app
DROP USER lce_uat_app
use cert_prod
DROP USER cf_uat_app
DROP USER fe_uat_app
DROP USER lce_uat_app
use lce_cl_cert
DROP USER cf_uat_app
DROP USER fe_uat_app
DROP USER lce_uat_app

USE [master]
GO
CREATE LOGIN [lce_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
CREATE LOGIN [fe_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
CREATE LOGIN [cf_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [cert_prod]
GO
CREATE USER [lce_uat_app] FOR LOGIN [lce_uat_app]
GO
USE [cert_prod]
GO
ALTER ROLE [db_owner] ADD MEMBER [lce_uat_app]
GO
CREATE USER [fe_uat_app] FOR LOGIN [fe_uat_app]
GO
USE [cert_prod]
GO
ALTER ROLE [db_owner] ADD MEMBER [fe_uat_app]
GO
USE [cf_cl_cert]
GO
CREATE USER [cf_uat_app] FOR LOGIN [cf_uat_app]
GO
ALTER ROLE [db_owner] ADD MEMBER [cf_uat_app]
GO
USE [cf_cl_cert]
GO
CREATE USER [lce_uat_app] FOR LOGIN [lce_uat_app]
GO
USE [cf_cl_cert]
GO
ALTER ROLE [db_owner] ADD MEMBER [lce_uat_app]
GO
USE [LCE_CL_Cert]
GO
CREATE USER [lce_uat_app] FOR LOGIN [lce_uat_app]
GO
USE [LCE_CL_Cert]
GO
ALTER ROLE [db_owner] ADD MEMBER [lce_uat_app]
GO