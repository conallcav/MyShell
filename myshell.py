#!/usr/bin/python3

import sys, readline, subprocess
from commands import *

operators = {
			"echo" : echo_comment,
		    "help" : man_file,
			"cd" : change_dir,
			"dir" : list_directory,
			"clr" : clear_screen,
			"environ" : environment_info,
		    "pause" : pause
		}

shell = os.getcwd()

def run(line):
	tokens = line.split()
	# split the input to access the command and possible arguments 
	command = tokens[0]

	if command in operators:
		# call the function that executes the operator
		operators[command](tokens)
	try:
		# check for command line input that is not an operator e.g. firefox
		if tokens[0] not in operators:
			subprocess.call(tokens)
	except:
		print("Command not found")

def main():
	if len(sys.argv) > 1:
		# check for a batch file
		with open(sys.argv[1], "r") as f:
			lines = f.readlines()
		for line in lines:
			# read in each line of the batchfile and run the command
			if line.split()[0] != "quit":
				run(line)
			else:
				break

	else:
		# set up a command line prompt and take in input
		user_input = input(os.getcwd() + " ")
		# split the input to acess the command and possible arguments
		user_input = user_input.split(" ")
		command = user_input[0]

		# take in input until the user enters quit
		while command != "quit":
			# call the function that executes the operator
			if command in operators:
				operators[command](user_input)
			try:
				# check for command line input that is not an operator e.g. firefox
				if command not in operators:
					# run it using background execution
					if user_input[-1] == "&":
						subprocess.Popen(user_input[:-1])
					# else run it normally
					else:
						subprocess.call(user_input)
			except:
				user_input = " ".join(user_input).strip()
				# if there is no input just pass to the next line
				if user_input == "":
					pass
				else:
					# finally output an error message alongside the users input
					print(user_input + " : command not found")

			user_input = input(os.getcwd() + " ")
			user_input = user_input.split(" ")
			command = user_input[0]

if __name__ == '__main__':
	main()
