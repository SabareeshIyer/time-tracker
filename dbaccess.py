import time
from tinydb import TinyDB, Query

db = TinyDB('db.json')
Task = Query()
db.insert({'currenttask': '', 'name' : 'meta'})

def starttask(tname):
	res = db.get(Task.name == tname)
	if(res == None):
		db.insert({'name' : tname, 'starttime': time.time(), 'endtime' : ''})
	else:
		db.update({'starttime': time.time()}, Task.name == tname )

	db.update({'currenttask': tname}, Task.name == 'meta')
	print("You've started working on %s " % tname)

def getstatus():
	res = db.get(Task.name == 'meta')
	nm = res['currenttask']
	cur = db.get(Task.name == nm)
	curStartTime = cur['starttime']

	print('You\'ve been working on',nm,'for',int((time.time()-curStartTime)/60),"minute(s)")

def endtask():
	res = db.get(Task.name == 'meta')
	nm = res['currenttask']
	cur = db.get(Task.name == nm)
	curStartTime = cur['starttime']

	db.update({'endtime': time.time()},Task.name == nm)
	print('Task',nm,'ended. You worked on',nm,'for',int((time.time()-curStartTime)/60),'minute(s).')

def note(notetext):
	print('Note added to notes file/current task.')

