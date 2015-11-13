#Count Lines of Code

Small python script that counts lines of code in a project.

You can call it by running

	cloc.py /path/of/your/project

It has an array with the extensions that will be excluded, if you have certain extensions that you need excluded from the count, add them to the array

	exclude = ['sample','exclude','description','png','jpg','config','HEAD','packed-refs','idx','master','pack','txt','index','gitignore']