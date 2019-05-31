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
	for k,v in a['scan'].iteritems(): 
		if str(v['status']['state']) == 'up':
			try:    
				print str(v['addresses']['mac'])
				macs.append(str(v['addresses']['mac']))
			except: print str(v['addresses']['ipv4'])
	
	logSpreadsheet(macs,date)

def logSpreadsheet(macs,date):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/tota77/Developer/client_secret.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open("Monitoreo-Casa").sheet1

	for mac in macs:
		print date, mac
		row = [date,str(mac),"DeLorear"]
		print row
		index = 1
		sheet.append_row(row)


def main():
	scan()

main()
# nm = nmap.PortScanner()
# nm.scan(hosts='192.168.88.0/24', arguments='-sn')
# nm.command_line()
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host, status in hosts_list:
# 	print('{0}:{1}'.host)