#!/usr/bin/env python

import nmap 
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


network="192.168.88.0/24"

def scan():
	nm = nmap.PortScanner() 
	cidr2='192.168.88.0/24'
	date=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	a=nm.scan(hosts=cidr2, arguments='-sP') 

	macs = []
	for k,v in a['scan'].items(): 
		if str(v['status']['state']) == 'up':
			try:    
				macs.append(str(v['addresses']['mac']))
			except: print(str(v['addresses']['ipv4']))
	
	logSpreadsheet(macs,date)

def logSpreadsheet(macs,date):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/tota77/Developer/client_secret.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open("Monitoreo-Casa").sheet1

	for mac in macs:
		row = [date,str(mac),"DeLorear"]
		index = 1
		sheet.append_row(row)
	print("done")

def main():
	scan()

main() 