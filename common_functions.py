'''
A bunch of common functions
'''

import gspread
from gspread_formatting import *
import pandas as pd
import sys
import time

def create_sheet(title):
	'''
		funciton intiatates the file 
	'''
	gc=gspread.oauth()
	try:
		#if it exists, delete it
		sh=gc.open(title)
		gc.del_spreadsheet(sh.id)
		#then create a new one
		sh=gc.create(title)
	except:
		#or just create a new one
		sh=gc.create(title)
	return sh


def get_teams_opponents():
	'''
		reads the master schedule csf and creates a dictionary.
		and returns for use in master function
		two lists is propbably fine and easy for our iteration
	'''
	dataset = pd.read_csv('schedule.csv',encoding='utf-16')
	teams = dataset.iloc[:, 0].values
	opponents=dataset.iloc[:, 1:].values
	
	return (teams,opponents)
	
def get_users():
	'''
		get users
	'''
	dataset = pd.read_csv('users.csv',encoding='utf-16')
	users= dataset.iloc[:, :].values
	#print(users)
	
	return users


