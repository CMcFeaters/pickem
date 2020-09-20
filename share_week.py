import gspread
import sys
import pandas as pd
import common_functions

def make_copy_and_share(users):
	gc=gspread.oauth()
	sh=gc.open('NFL_Pickem')
	
	for user in users:
		sh_copy=gc.copy(sh.id,user[0]+'_NFL_Pickem')
		#sh_copy=gc.open(user[0]+'week_%d'%week)
		sh_copy.share(user[1], perm_type='user', role='writer')
	
def main():	
	'''
		given the week number will create a spreadsheet of opponents
	'''
	users=common_functions.get_users()
	make_copy_and_share(users)

	

if __name__ == "__main__":
	main()
	
