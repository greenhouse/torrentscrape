


#=======================================================================#
                # json error key/values #
kErrArgs = "err_args"
kErrDb = "err_db"
kErrDbUsrExists = "err_db user exists"
kErrDbUsrNotExists = "err_db user not exists"
kErrS3 = "err_storage"

vErrNone = 0
vErrArgs = 1
vErrDb = 2
vErrS3 = 3
#=======================================================================#

#=======================================================================#
                # json error response variables #

err_resp_args = {'ERROR':vErrArgs, 'MSG':kErrArgs, 'PAYLOAD':{'error':vErrArgs}}
err_resp_db = {'ERROR':vErrDb, 'MSG':kErrDb, 'PAYLOAD':{'error':vErrDb}}
err_resp_db_usr_exist = {'ERROR':vErrDb, 'MSG':kErrDbUsrExists, 'PAYLOAD':{'error':vErrDb}}
err_resp_db_usr_not_exist = {'ERROR':vErrDb, 'MSG':kErrDbUsrNotExists, 'PAYLOAD':{'error':vErrDb}}
err_resp_s3 = {'ERROR':vErrS3, 'MSG':kErrS3, 'PAYLOAD':{'error':vErrS3}}
#=======================================================================#

#=======================================================================#
                # Common request keys #
#=======================================================================#

#=======================================================================#
                # Common request values #
#=======================================================================#

#=======================================================================#
                # Common database columns #
#=======================================================================#
#=======================================================================#

#=======================================================================#
                # Common database query keys #
# psql return columns getInitSettings #
sel_keys_tbl_settings = ['id','dt_created','dt_updated','min_ios_ver','min_droid_ver','url_img_splash']

#=======================================================================#
#=======================================================================#



