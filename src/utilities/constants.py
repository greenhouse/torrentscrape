
print('GO constants.py -> starting IMPORTs')

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

# constants
cStrSpace = '   '
cStrDivider = '#----------------------------------------------------------------------------------------------------#'
cStrDivider01 = cStrDivider
cStrDivider02 = '%s\n%s' % (cStrDivider,cStrDivider)

cStrExtSpace13 = '%s%s%s%s%s%s%s%s%s%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace10 = '%s%s%s%s%s%s%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace08 = '%s%s%s%s%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace06 = '%s%s%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace05 = '%s%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace04 = '%s%s%s%s'%(cStrSpace,cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace03 = '%s%s%s'%(cStrSpace,cStrSpace,cStrSpace)
cStrExtSpace02 = '%s%s'%(cStrSpace,cStrSpace)
cStrExtSpace01 = '%s'%(cStrSpace,)
cStrExtSpace00 = ''

# DISCORD
#cDiscordTOKEN = <sites/__init__.py>

# str guild / server names
cStrServerThaDevs = 'Tha Devs'

# str channel names
cStrChanWelcome = 'welcome'

# str DB tables / columns
cCol_player_id = 'player_id'
cCol_sell_all = '*'
cCol_sell_all_pass = '2012mayan'

cTblePlayer = 'player'
cColPlayerId = 'id'
cColPlayerDiscIdFull = 'discord_id_full'
cColPlayerDiscIdName = 'discord_id_name'
cColPlayerDiscIdTag = 'discord_id_tag'
cColPlayerFirstIpAddr = 'first_ip_addr'
cColPlayerBalance = 'dht_balance'
cColPlayerEmail = 'email'

cTblEventLog = 'player_event_log'
cColEventTypeId = 'event_type_id'
cColEventDiscId = 'discord_id_full'
cColEventDiscIdTag = 'discord_id_tag'
cColEventDescr = 'event_description'
cColEventIpAddr = 'ip_addr'

cTblPlayTransCurr = 'player_transaction_currency'
cColCurrTypeId = 'currency_type_id'
cColCurrValue = 'currency_value'
cColDhtValue = 'dht_value'
cColDepositAddr = 'deposit_address'
cColOutPTCID = 'ptcid'

# DB type IDs
cEventType_MsgReceived = 1
cEventType_MemJoin = 2
cEventType_MemRemove = 3
cCurrencyType_DHT = 1
cCurrencyType_BTC = 2
cCurrencyType_ETH = 3
cCurrencyType_TRX = 4

# CMD email
cCmdEmailExample = 'example@email.com'

# CMD deposit
cCmdDepositAmnt1 = '$5'
cCmdDepositAmnt2 = '$10'
cCmdDepositAmnt3 = '$15'
cCmdDepositAmnt4 = '$20'
cCmd_list_deposit_amnts = [cCmdDepositAmnt1,
                           cCmdDepositAmnt2,
                           cCmdDepositAmnt3,
                           cCmdDepositAmnt4]

cCmdDepositCC = 'CreditCard'
cCmdDepositVenmo = 'Venmo'
cCmdDepositPatreon = 'Patreon'
cCmdDepositBTC = 'BTC'
cCmdDepositETH = 'ETH'
cCmdDepositTRX = 'TRX'
cCmdDepositBTT = 'BTT'
cCmdDepositDHT = 'DHT'
cCurreny_dict_types = {cCmdDepositDHT:cCurrencyType_DHT,
    cCmdDepositBTC:cCurrencyType_BTC,
        cCmdDepositETH:cCurrencyType_ETH,
            cCmdDepositTRX:cCurrencyType_TRX}
cCmd_lst_deposit_types = [cCmdDepositVenmo,
                          cCmdDepositPatreon,
                          cCmdDepositBTC,
                          cCmdDepositETH,
                          cCmdDepositTRX]
cCmd_lst_deposit_usd = [cCmdDepositVenmo,
                        cCmdDepositPatreon]
cCmd_lst_deposit_cryptos = [cCmdDepositBTC,
                            cCmdDepositETH,
                            cCmdDepositTRX]

# BINANCE symbols
cSymbFullBTC = 'BTCUSDT'
cSymbFullETH = 'ETHUSDT'
cSymbFullTRX = 'TRXBTC'
cSymbFullBTT = 'BTTBTC'
cSymb_lst_binance = [cSymbFullBTC,
                     cSymbFullETH,
                     cSymbFullTRX]

# WALLET addresses
cWallBTC = 'BTC'
cWallETH = 'ETH'
cWallTRX = 'TRX'
cWallBTT = 'BTT'
cWallAddrBTC = '<test-btc-address>'
cWallAddrETH = '<test-eth-address>'
cWallAddrTRX = '<test-trx-address>'
cWallAddrBTT = '<test-btt-address>'
cWallet_dict_addr = {cWallBTC:cWallAddrBTC,
    cWallETH:cWallAddrETH,
        cWallTRX:cWallAddrTRX}

# CASH addresses
cCashVenmo = 'VENMO'
cCashPatreon = 'PATREON'
cCashAddrVenmo = '@fivemDHT'
cCashAddrPatreon = '<test-patreon-address>'
cCash_dict_addr = {cCashVenmo:cCashAddrVenmo,
    cCashPatreon:cCashAddrPatreon}







