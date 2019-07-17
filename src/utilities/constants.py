


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
# mysql return columns get last torrent scrape  #
sel_keys_tbl_torrent  = ['id',
                         'fk_scrape_inst_id',
                         'scrape_idx',
                         'scrape_pg_num',
                         'info_hash',
                         'seed_cnt',
                         'leech_cnt',
                         'file_size',
                         'scrape_href_title',
                         'scrape_href',
                         'mag_link',
                         'dt_created',
                         'dt_updated']

#=======================================================================#
#=======================================================================#



