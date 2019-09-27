# MyShell
A simple Linux shell made for my Operating Systems module.
This Command Line Interpreter is a fundamental interface to an Operating System.
It can be run by typing python3 myshell.py once the relevant files are in the cwd. Below you can find a list of executable commands and different functions the shell provides.

COMMANDS
     
     The shells commands can be executed by typing them after the command line prompt provided. The syntax must follow the syntax shown below or else the
     commands will not work.
     Here is a list of the shells commands along with descriptions:

     cd <directory> -  Changes the current directory to the <directory> supplied, or if ".." is provided it will change to the previous directory. 
                       If it does not exist it returns the current directory. Also changes the PWD environment variable.

     clr - clears the terminal.

     dir <directory> - Lists the contents of the current working directory. Also if supplied with a valid <directory> it will list the contents of that directory.

     echo <comment> - Takes as an argument a comment which it displays on the terminal followed by a newline. Multiple spaces and tabs are reduced to a single space.

     environ - Lists all the environment strings in a formatted output.

     help - displays the shells help manual. Press q to return to the shell.

     pause - pause operation of the shell until the Enter key is pressed.

     quit - quits the shell.

OTHER
     
     The shell can run a batch file using python3 myshell.py <batchfile>.
     The batchfile should be formatted with a valid command on each line.
     The shell will run through each line, execute all the commands and then exit.
     
     The shell is also capable of running files and opening applications e.g. Firefox. 
     You can utilize background programme execution to execute these by adding the "&" symbol after typing the application or programme you want to run.
