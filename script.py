import nmap 
import subprocess
import time
import datetime


network="192.168.88.0/24"

def scan():
	p = subprocess.Popen("sudo nmap -sn 192.168.88.0/24 | grep 'MAC Address:' | awk '{print $3}'" ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	#print("Command output : ")
	print(output.decode('utf-8').strip())
	x = datetime.datetime.now()
	print(x)

def main():
	scan()

main()
# nm = nmap.PortScanner()
# nm.scan(hosts='192.168.88.0/24', arguments='-sn')
# nm.command_line()
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host, status in hosts_list:
# 	print('{0}:{1}'.host)