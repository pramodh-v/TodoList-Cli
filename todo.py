import os
import sys
import datetime

def Help():
	DispText="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
	sys.stdout.buffer.write(DispText.encode('utf8'))

def Ls():
	if(os.path.isfile("todo.txt")):
		with open("todo.txt",'r') as Traverse:
			TodoFile = Traverse.readlines()
		NoLines = len(TodoFile)
		List = ""
		for Line in TodoFile:
			List+= '[{}] {}'.format(NoLines,Line)
			NoLines-=1
		sys.stdout.buffer.write(List.encode('utf8'))
	else:
		print("There are no pending todos!")

def Add(NewToDo):
	if(os.path.isfile("todo.txt")):
		with open("todo.txt",'r') as OldFile:
			exist = OldFile.read()
		with open("todo.txt",'w') as OnTop:
			OnTop.write(NewToDo+'\n')
			OnTop.write(exist)
	else:
		with open("todo.txt",'w') as WriteNew:
			WriteNew.write(NewToDo+'\n')
	print('Added todo: "{}"'.format(NewToDo))

def Del(DelNum):
	if(DelNum<=0):
		print("Error: todo #{} does not exist. Nothing deleted.".format(DelNum))
	if(os.path.isfile("todo.txt")):
		with open("todo.txt",'r') as Traverse:
			TodoFile = Traverse.readlines()
		NoLines = len(TodoFile)
		if(DelNum>NoLines):
			print("Error: todo #{} does not exist. Nothing deleted.".format(DelNum))
		else:
			with open("todo.txt",'w') as Modify:
				for Lines in TodoFile:
					if(NoLines!=DelNum):
						Modify.write(Lines)
					NoLines-=1
			print("Deleted todo #{}".format(DelNum))
	else:
		print("Error: todo #{} does not exist. Nothing deleted.".format(DelNum))

def Done(DoneNum):
	if(DoneNum<=0):
		print("Error: todo #{} does not exist. Nothing deleted.".format(DoneNum))
	if(os.path.isfile("todo.txt")):
		with open("todo.txt",'r') as Traverse:
			TodoFile = Traverse.readlines()
		NoLines = len(TodoFile)
		if(DoneNum>NoLines):
			print("Error: todo #{} does not exist. Nothing deleted.".format(DoneNum))
		else:
			with open("todo.txt",'w') as WriteToDo:
				if(os.path.isfile("done.txt")):
					with open("done.txt",'r') as ReadDone:
						DoneToDo = ReadDone.read()

					with open("done.txt",'w') as WriteDone:
						for Line in TodoFile:
							if(NoLines==DoneNum):
								WriteDone.write("x "+datetime.datetime.today().strftime('%Y-%m-%d')+" "+Line)
							else:
								WriteToDo.write(Line)
							NoLines-=1
						WriteDone.write(DoneToDo)
				else:
					with open("done.txt",'w') as WriteDone:
						for Line in TodoFile:
							if(NoLines==DoneNum):
								WriteDone.write("x "+datetime.datetime.today().strftime('%Y-%m-%d')+" "+Line)
							else:
								WriteToDo.write(Line)
								NoLines-=1
			print("Marked todo #{} as done.".format(DoneNum))
	else:
	    print("Error: todo #{} does not exist.".format(DoneNum))

def Report():
	Incom,Com = 0,0
	if os.path.isfile("todo.txt"):
		with open("todo.txt",'r') as Traversal:
			ReadToDo = Traversal.readlines()
	Incom = len(ReadToDo)

	if os.path.isfile("done.txt"):
		with open("done.txt",'r') as Traversal:
			DoneToDo = Traversal.readlines()
	Com = len(DoneToDo)

	DispText = datetime.datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(Incom,Com)
	sys.stdout.buffer.write(DispText.encode('utf8'))

def main():
	if len(sys.argv)==1:
		Help()
	elif sys.argv[1]=='help':
		Help()
	elif sys.argv[1]=='ls':
		Ls()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			Add(sys.argv[2])
		else:
			print("Error: Missing todo string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			Del(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting todo.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			Done(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking todo as done.")
	elif sys.argv[1]=='report':
		Report()
	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__": 
    main() 