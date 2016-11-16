import sys
from dbaccess import *

initialize()

if (sys.argv[1] == 'start'):
	starttask(sys.argv[2])
	
elif (sys.argv[1] == 'status'):
	getstatus()

elif (sys.argv[1] == 'stop' or sys.argv[1] == 'end' or sys.argv[1] == 'fin'):
	endtask()

elif(sys.argv[1] == 'note'):
	pep = " ".join(sys.argv[2:])
	print (pep)
	note(pep)