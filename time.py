import sys
import logging
from dbaccess import *

logging.basicConfig(filename='time-tracker.log',level=logging.INFO)

initialize()

if (sys.argv[1] == 'start'):
	logging.info("__Task start__")
	starttask(sys.argv[2])
	
elif (sys.argv[1] == 'status'):
	logging.info("__Status query__")
	getstatus()

elif (sys.argv[1] == 'stop' or sys.argv[1] == 'end' or sys.argv[1] == 'fin'):
	logging.info("__Task stop__")
	endtask()

elif(sys.argv[1] == 'note'):
	logging.info("__Note addition__")
	pep = " ".join(sys.argv[2:])
	print (pep)
	note(pep)