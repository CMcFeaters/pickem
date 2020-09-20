'''
builds the score sheet
'''

import gspread
from gspread_formatting import *
import pandas as pd
import sys
import time
import common_functions


def main():	
	'''
		given the week number will create a spreadsheet of opponents
	'''
	week=int(sys.argv[1])
	gc=gspread.oauth()
	standings=gc.open('The Standings')
	(teams,opponents)=common_functions.get_teams_opponents()
	users=common_functions.get_users()
	#for user in users:
	#	write_sheet(standings,gc.open(user[0]+'_NFL_Pickem'),week)
	
def write_test():

	spreadsheetId=''
	sheetId=''

	sht = gc.open_by_key(spreadsheetId)

	requests = []

	requests.append({
		  "insertDimension": {
			"range": {
			  "sheetId": sheetId,
			  "dimension": "COLUMNS",
			  "startIndex": 2,
			  "endIndex": 4
			},
			"inheritFromBefore": True
		  }
		})

	body = {
		'requests': requests
	}

	sht.batch_update(body)

def write_sheet(standings,user,week):
	'''
		for each user we need to go to their picks for the week and copy them to 
		our standings sheet
	'''
	st_sheet=standings.get_worksheet("Week_%d"%week)
	user_sheet=user.get_worksheet("Week_%d"%week)
	
	selections=user_sheet.batch_get['C1:C32']
	
	
if __name__ == "__main__":
	if len(sys.argv)<2:
		print("please provide the week number")
	else:
		main()
		
	
