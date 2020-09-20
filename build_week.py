'''
This function will build a bunch of spreadsheets for each week
the input is the week number, the file reads the master schedule 
develops a generic gsheet for the week a separate file will copy it 
share it with users
'''

import gspread
from gspread_formatting import *
import pandas as pd
import sys
import time
import common_functions

	
def build_schedule():
	'''
		reads the master schedule csf and creates a dictionary.
		and returns for use in master function
		two lists is propbably fine and easy for our iteration
	'''
	dataset = pd.read_csv('schedule.csv',encoding='utf-16')
	teams = dataset.iloc[:, 0].values
	opponents=dataset.iloc[:, 1:].values
	#now divide into touples of games per week.
	#each week shoudl have at most 16 touples
	games_list=[]
	for week in range(0,17):
		#this value contains the list of opponents for each week
		w_oppo=[opponents[i][week] for i in range(0,len(teams))]
		games_list.append([])
		
		#build a list of away teams
		away_teams=[]
		for i in range(0,len(w_oppo)):
			if len(w_oppo[i].split("@"))>1:
				#print(w_oppo[i])
				away_teams.append(w_oppo[i].split("@")[1])
		
		#go through the teams list, if a team is not in the away teams, schedule the games
		for i in range (0,len(teams)):
			#if the team is not in the away list, add that game
			if (away_teams.count(teams[i])==0) and (w_oppo[i]!="BYE"):
				#print(teams[i],w_oppo[i])
				games_list[week].append([teams[i],w_oppo[i].split("@")[1],"FUCK YOU"])
		#print(week,": ",len(games_list[week]))
		
	return (games_list)

def write_sheet(sh, games_list):
	'''
		filsl in teh worksheet iwht the opponents and teh dropdown
	'''
	#time.sleep(200)
	for week in range(1,2):
		print("Starting week %d"%week)
		n_games=len(games_list[week])
		try:
			worksheet=sh.worksheet("Week_%d"%week)
		except:
			worksheet=sh.add_worksheet(title="Week_%d"%week, rows="%d"%n_games,cols="3")
		
		
			#fill in teh opponents and teams
			#print(games_list[week])
		worksheet.batch_update([{'range':'A1:C%d'%(n_games+1),'values':games_list[week]}])
		
		for i in range(0,n_games):
			select_list=games_list[week][i]
			validation_rule=DataValidationRule(
			BooleanCondition('ONE_OF_LIST',select_list),
			showCustomUi=True)
			
			#add teh data validation
			set_data_validation_for_cell_range(worksheet,'C%d'%(i+1),validation_rule)
			
	

def main():	
	'''
		given the week number will create a spreadsheet of opponents
	'''
	gc=gspread.oauth()
	sh=gc.open("NFL_Pickem")
	games_list=build_schedule()
	write_sheet(sh,games_list)
	

if __name__ == "__main__":
		main()
	
