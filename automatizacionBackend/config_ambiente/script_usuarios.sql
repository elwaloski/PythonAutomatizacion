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
CREATE LOGIN [lce_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
CREATE LOGIN [fe_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
CREATE LOGIN [cf_uat_app] WITH PASSWORD=N'UREPKw95I8', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF

USE [cert_prod]
CREATE USER [fe_uat_app] FOR LOGIN [fe_uat_app]
USE [cert_prod]
ALTER ROLE [db_owner] ADD MEMBER [fe_uat_app]


USE [cf_cl_cert]
CREATE USER [cf_uat_app] FOR LOGIN [cf_uat_app]
ALTER ROLE [db_owner] ADD MEMBER [cf_uat_app]

USE [LCE_CL_Cert]
CREATE USER [lce_uat_app] FOR LOGIN [lce_uat_app]
ALTER ROLE [db_owner] ADD MEMBER [lce_uat_app]

USE [master]
GRANT ALTER TRACE TO [lce_uat_app]
GRANT ALTER TRACE TO [cf_uat_app]
GRANT ALTER TRACE TO [fe_uat_app]

use cert_prod
declare
@serv_serv varchar(20),
@ruta_home varchar (80);

begin
  set @serv_serv = 'W-FECUAT-QA'
  set @ruta_home = 'D:\DBNeTSE'

insert into dbn_servidor values (@serv_serv,'Servidor FE QA AWS');    
  
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dbn_control','OFF',2,'S',8,'S',@ruta_home+'\BIN\dbn_control.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_gen_xml','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_gen_xml.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_envi_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_envi_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_upld_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_upld_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_resp_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_resp_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dbq_read_mail','ON',2,'S',8,'S',@ruta_home+'\Readmail\Readmail.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dbq_scan_arch','ON',2,'S',8,'S',@ruta_home+'\BIN\dbq_scan_arch.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_resp_tec','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_resp_tec.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_carg_dto','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_carg_dto.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dto_resp_tec','ON',2,'S',8,'S',@ruta_home+'\BIN\dto_resp_tec.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dbq_envi_mail','ON',2,'S',8,'S',@ruta_home+'\SendMail\SendMail.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dto_resp_come','ON',2,'S',8,'S',@ruta_home+'\BIN\dto_resp_come.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_envi_clie','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_envi_clie.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'lcv_resp_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\lcv_resp_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_command','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_command.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_reen_clie','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_reen_clie.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_revi_docu','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_revi_docu.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_carg_dte','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_carg_dte.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_gen_pdf','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_gen_pdf.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_impr_dte','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_impr_dte.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dte_resp_reci','ON',2,'S',8,'S',@ruta_home+'\BIN\dte_resp_reci.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dto_resp_reci','ON',2,'S',8,'S',@ruta_home+'\BIN\dto_resp_reci.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'dbn_envi_paide','ON',2,'S',8,'S',@ruta_home+'\BIN\dbn_envi_paide.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_cons_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_cons_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_gen_xml','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_gen_xml.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_gen_xml_lote','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_gen_xml_lote.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_envi_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_envi_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_envi_sii_lote','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_envi_sii_lote.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_upld_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_upld_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_upld_sii_lote','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_upld_sii_lote.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_resp_sii','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_resp_sii.exe')
insert into dbn_serv_srvd (serv_serv,codi_serv,esta_serv,slee_serv,debu_serv,hvid_serv,modo_serv,coma_serv) Values (@serv_serv,'bel_resp_sii_lote','ON',2,'S',8,'S',@ruta_home+'\BIN\bel_resp_sii_lote.exe')


insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dbn_control',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_gen_xml',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_envi_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_upld_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_resp_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dbq_read_mail',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dbq_scan_arch',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_resp_tec',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_carg_dto',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dto_resp_tec',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dbq_envi_mail',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dto_resp_come',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_envi_clie',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('lcv_resp_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_command',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_reen_clie',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_revi_docu',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_carg_dte',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_gen_pdf',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_impr_dte',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dte_resp_reci',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dto_resp_reci',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('dbn_envi_paide',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_cons_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_gen_xml',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_envi_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_upld_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_resp_sii',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_gen_xml_lote',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_envi_sii_lote',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_upld_sii_lote',@serv_serv,0,24,12,1,1,50)
insert into dbn_sesr_rang_oper(codi_serv, codi_srvd, desd_sero,hast_sero,pcti_sero,mini_sero,maxi_sero,qsiz_sero)Values ('bel_resp_sii_lote',@serv_serv,0,24,12,1,1,50)

end 

update wss_empr_auth set egat_home='PROD_0277_HOME', path_home='D:\esuite_wss', codi_usua='WSS_CERTIFICACION', pass_usua='Admin1' where codi_emex='prod_0277'
insert wss_empr_serv values ('WSSCONSDOCUASP','78079790')
insert wss_empr_serv values ('WSSVERIFSUCSUI','78079790')
