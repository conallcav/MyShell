#!/usr/bin/python3
#Conall Caverly - 17336471

import os, subprocess

def change_dir(user_input):
	if len(user_input) == 1:
		# change nothing if only cd is entered
		return
	else:
		# get current working directory using the os command
		cwd = os.getcwd()
		# get the list of files and directories in the cwd
		list_dir = os.listdir(cwd)
		path = user_input[1]
		# check if the path is a valid directory
		if path in list_dir or path == "..":
			# if it is change the directory
			os.chdir(path)
		else:
			print("Directory does not exist")
		# change the PWD in the environment
		os.environ["PWD"] = os.getcwd()

def list_directory(user_input):
	cwd = os.getcwd()
	list_dir = os.listdir(cwd)
	if len(user_input) == 1:
		# if only dir is input, output directories from the cwd
		for file in list_dir:
			print(file)
		print("\n")
	try:
		# check to see if a specific dir was given
		for file in os.listdir(user_input[1]):
			# if so output directories from the given dir
			print(file)
		print("\n")
	except:
		return("Invalid syntax used")

def environment_info(user_input):
	# split the environ items
	for k, v in os.environ.items():
		# output them in a formatted way
		print(str(k) + " : " + str(v))

def echo_comment(user_input):
	# join all input after echo, eliminate all whitespace using strip()
	comment = " ".join(user_input[1:]).strip().split()
	print(" ".join(comment) + "\n")

def clear_screen(user_input):
	# \033c will clear the terminal
	# end = "" leaves the prompt at the top of the terminal
	print("\033c", end = "")

def pause(user_input):
	# disable echo so no input can be seen
	os.system("stty -echo")
	inp = " "
	# keep taking input until enter is hit
	while inp != "":
		inp = input()
		# enable echo again and exit the function
		return(os.system("stty echo"))

def man_file(user_input):
	# output the help page by running the manfile
	subprocess.run(["man","./manfile.groff"])