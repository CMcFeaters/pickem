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
	
	gc=gspread.oauth()
	sh=gc.open("TEMPS2")
	
	worksheet=sh.get_worksheet(0)
	
	'''
	cell_list = worksheet.range('A1:A7')
	cell_values = [1,2,3,4,5,6,7]
	
	for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
		cell_list[i].value = val    #use the index on cell_list and the val from cell_values

	worksheet.update_cells(cell_list)
	'''
	temp=[[1,8],[2,9],[3,10],[4,11],[5,12],[6,13],[7,14]]
	worksheet.batch_update([{'range':'B1:C7','values':temp}])
	vlist=worksheet.batch_get(['B1:B7'])
	print(vlist)
	
if __name__ == "__main__":
	main()
		
	
