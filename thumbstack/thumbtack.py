import sys

database = {}
#{key:{value: int}

transactions = []
#Create a stack to keep track of transactions

def compile_data():
	"""compiles data to see current state of all non committed transactions without changing current database"""
	temp_data_base = database.copy()
	for dictionary in transactions:
		temp_data_base.update(dictionary)
	return temp_data_base


def SET(key,value):
	"""Adds key and value to the database.  No spaces will be passed."""
	if transactions:
		current_transaction = transactions.pop()
		current_transaction[key]={"value": value}
		transactions.append(current_transaction)
	else:
		database[key] = {"value":value}


def GET(key): 
	"""Given the name/key. Print out the value of the variable name, 
	or NULL if that variable is not set."""
	if transactions:
		current_state_of_data = compile_data()
		if current_state_of_data.get(key) != None:
			print current_state_of_data[key]["value"]
			return 
		else:
			print "NULL"
			return
	else:
		if database.get(key) != None:
			print database[key]["value"]
			return 
		else:
			print "NULL"
			return


def UNSET(key):
	"""Given the name/key. Unset the variable name, making it just 
	like that variable was never set."""
	
	if transactions:
		current_state_of_data = compile_data()
		if current_state_of_data.get(key)!= None:
			current_transaction = transactions.pop()
			current_transaction[key] = None
			transactions.append(current_transaction)
		else:
			print "NULL"
			return
	else:
		if database.get(key)!= None:
			del database[key]
		else:
			print "NULL"
			return

def NUMEQUALTO(value):
	"""Given a value. Print out the number of variables that are 
	currently set to value. If no variables equal that value, print 0."""
	count = 0
	if transactions:
		current_state_of_data = compile_data()
		for k, v in current_state_of_data.items():
			if v != None:
				if v.get("value") == value:
					count = count + 1
		print count
		return 

	else:
		for k ,v in database.items():
			if v != None:
				if v.get("value") == value:
					count = count + 1
		print count
		return 

def END():
	 """Exit the program. Your program will always receive this as its 
	 last command."""
	 sys.exit()

def BEGIN():
	"""Open a new transaction block. Transaction blocks can be nested; a BEGIN can be issued inside 
	of an existing block."""

	new_transaction = {}
	transactions.append(new_transaction)


def ROLLBACK():
	"""Undo all of the commands issued in the most recent transaction block, and close the block. 
	Print nothing if successful, or print NO TRANSACTION if no transaction is in progress."""
	try:
		transactions.pop()

	except IndexError:
		print "NO TRANSACTION"


def COMMIT():
	"""Close all open transaction blocks, permanently applying the changes made in them. Print 
	nothing if successful, or print NO TRANSACTION if no transaction is in progress."""
	if transactions:
		while transactions:
			database.update(transactions.pop(0))
	else:
		print "NO TRANSACTION"

def process_command(command_list):
	"""Given an array where the first item is the command, it searches the function command_list
	to find the appropriate command and execute that function."""

	command = command_list[0]

	if command == "SET":
		SET(command_list[1], command_list[2])

	if command == "GET":
		GET(command_list[1])

	if command == "UNSET":
		UNSET(command_list[1])

	if command == "NUMEQUALTO":
		NUMEQUALTO(command_list[1])

	if command == "END":
		END()

	if command == "BEGIN":
		BEGIN()

	if command == "ROLLBACK":
		ROLLBACK()

	if command == "COMMIT":
		COMMIT()


def main():
	command_input = sys.stdin.readlines()
	while command_input:
		clean_data = command_input.pop(0).strip()
		command_list = clean_data.split(" ")
		process_command(command_list)
		

if __name__ == '__main__':
	main()