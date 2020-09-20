import gspread
import pandas as pd

gc=gspread.oauth()
sh=gc.open("test")

schedule={}
dataset = pd.read_csv('schedule.csv',encoding='utf-16')
teams = dataset.iloc[:, 0].values
opponents=dataset.iloc[:, 1:].values

for i in range(0,len(teams)):
	schedule[teams[i]]=opponents[i]

print(sh.sheet1.get('A1'))