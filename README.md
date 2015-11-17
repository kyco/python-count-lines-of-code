#Count Lines of Code

Small python script that counts lines of code in a project.

This was written in Python 2.7 and was tested in Linux.

##Running
You can call it by running

	cloc.py /path/of/your/project

It has an array with the extensions that will be excluded, if you have certain extensions that you need excluded from the count, add them to the array

	exclude = ['sample','exclude','description','png','jpg','config','HEAD','packed-refs','idx','master','pack','txt','index','gitignore']

##Info
    - Python version: 2.7
    - Operating System: Linux
    - Accepts arguments from a command line


##To Do
    - If no arguments are found from the command line, ask the user for an input inside of the application.
    - Write a version for Python 3.4+
    - Test Windows compatibility and update code if problems arise during testing (perhaps create a separate branch as well)
    - Give the user the ability to upload a csv to define excluded file types
    - If a .gitignore file is found, ask the user if they would like to use that to append to their current ignore list