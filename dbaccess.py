import time
from tinydb import TinyDB, Query

db = TinyDB('db.json')
Task = Query()
def initialize():
	res = db.all()
	if(bool(res) == False):
		db.insert({'currenttask': '', 'name' : 'meta'})

def starttask(tname):
	res = db.search(Task.name == tname)
	if(bool(res) == False):
		db.insert({'name' : tname, 'starttime': time.time(), 'endtime' : ''})
	else:
		db.update({'starttime': time.time()}, Task.name == tname )

	db.update({'currenttask': tname}, Task.name == 'meta')
	print("You've started working on %s " % tname)

def getstatus():
	res = db.search(Task.name == 'meta')
	nm = res[0]['currenttask']
	cur = db.search(Task.name == nm)
	curStartTime = cur[0]['starttime']

	print('You\'ve been working on',nm,'for',int((time.time()-curStartTime)/60),"minute(s)")

def endtask():
	res = db.search(Task.name == 'meta')
	nm = res[0]['currenttask']
	cur = db.search(Task.name == nm)
	curStartTime = cur[0]['starttime']

	db.update({'endtime': time.time()},Task.name == nm)
	print('Task',nm,'ended. You worked on',nm,'for',int((time.time()-curStartTime)/60),'minute(s).')

def note(notetext):
	print('Note added to notes file/current task.')

