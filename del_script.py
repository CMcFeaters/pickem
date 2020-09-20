import gspread
gc=gspread.oauth()

sh=gc.open("NFL_Pickem")

gc.del_spreadsheet(sh.id)