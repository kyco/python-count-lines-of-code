#Count Lines of Code

Small python script that counts lines of code in a project.

This was written in Python 2.7 and was tested in Linux.

##Running
You can call it by running

	cloc.py /path/of/your/project /path/to/excludelist.csv

It has an array with the extensions that will be excluded, if you have certain extensions that you need excluded from the count, add them to the array

	exclude = ['sample','exclude','description','png','jpg','config','HEAD','packed-refs','idx','master','pack','txt','index','gitignore']

##Info
 - Python version: 2.7
 - Operating System: Linux
 - Accepts arguments from a command line
 - If no arguments are found from the command line, ask the user for an input inside of the application.
 - There is a version for Python 3.4+ in a separate branch called python3
 - Has been tested and works in Windows 10. There is a bug where it picks up random file types by searching through what is probably the .git folder.
 - Include a csv to define excluded file types

##To Do
 - If a .gitignore file is found, ask the user if they would like to use that to append to their current ignore list