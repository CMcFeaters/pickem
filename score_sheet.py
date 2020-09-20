'''
builds the score sheet
'''

import gspread
from gspread_formatting import *
import pandas as pd
import sys
import time
import common_functions

def make_backup(sh,week):
	#create a backup each time you modify a week.  will delete old backup
	gc=gspread.oauth()
	try:
		shb=gc.open("The Standings_Backup_Week%d"%week)
		gc.del_spreadsheet(shb.id)
	except:
		pass
	gc.copy(sh.id,title="The Standings_Backup_Week%d"%week)

def main():	
	'''
		given the week number will create a spreadsheet of opponents
	'''
	week=int(sys.argv[1])
	gc=gspread.oauth()
	standings=gc.open('The Standings')
	#make  backup
	make_backup(standings,week)
	
	users=common_functions.get_users()
	
	for i in range (0,len(users)):
		user_sheet=gc.open(users[i][0]+"_NFL_Pickem")
		write_sheet(standings,user_sheet,week,i)
	#setup_sheet(standings,users)
	#for user in users:
	#	write_sheet(standings,gc.open(user[0]+'_NFL_Pickem'),week)

'''
def setup_sheet(sh,users):
	for i in range(2,18):
		worksheet=sh.worksheet("Week_%d"%i)
		titles=['team 1','team 2','Actual']
		for i in range(0,len(users)):
			titles.append(users[i][0])
			titles.append(users[i][0]+"_Score")
		worksheet.add_cols(len(users)*2)
		worksheet.insert_row(titles)
	'''
def write_sheet(standings,user,week,usernum):
	'''
		for each user we need to go to their picks for the week and copy them to 
		our standings sheet
	'''
	st_sheet=standings.worksheet("Week_%d"%week)
	user_sheet=user.worksheet("Week_%d"%week)
	ngames=user_sheet.row_count
	#print(ngames)
	
	#get this users selections
	selections=user_sheet.batch_get(['C1:C%d'%ngames])[0]
	#print(selections)
	#find the "write" location
	cols={0:'D',1:'F',2:'H',3:'J',4:'L'}
	startcol=cols[usernum]
	stop_row=1+ngames
	#print('%s2:%s%d'%(startcol,startcol,stop_row))
	
	#batch update teh worksheet
	st_sheet.batch_update([{'range':'%s2:%s%d'%(startcol,startcol,stop_row),'values':selections}])
	
	
if __name__ == "__main__":
	if len(sys.argv)<2:
		print("please provide the week number")
	else:
		main()
		
	
