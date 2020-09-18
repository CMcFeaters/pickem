import gspread
gc=gspread.oauth()
sh=gc.open("test")
print(sh.sheet1.get('A1'))