PROJECT NAME: 0x00. AirBnB clone - The console

INSTRUCTIONS TO FOLLOW WHILE WRITING THE PYTHON SCRIPTS

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


INSTRUCTIONS FOR TESTING PYTHON SCRIPTS

Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case


DESCRIPTION OF THE COMMAND INTERPRETER

The command interpreter, also known as a shell, is a program that allows users to interact with the operating system by entering commands. Here's a brief description of how to start and use the command interpreter, as well as some examples:

How to start the command interpreter:

To start the command interpreter, simply open a terminal or console window on your operating system. Depending on your system, you may have different options for accessing the command interpreter. For example, on Linux or macOS, you can usually access it by opening the Terminal application. On Windows, you can access it by opening the Command Prompt or PowerShell application.

How to use the command interpreter:

Once you have started the command interpreter, you can begin entering commands. The basic syntax for a command is:
command [options] [arguments]


Here, the command is the name of the program or function you want to run, options are flags that modify the behavior of the command, and arguments are values or variables that the command needs to run.

Examples:

Here are some examples of basic commands you can run in the command interpreter:

ls: lists the contents of the current directory.
cd: changes the current directory to the specified directory.
mkdir: creates a new directory.
rm: removes a file or directory.
echo: prints text to the console.
cat: displays the contents of a file.
Here are some examples of commands with options and arguments:

ls -l: lists the contents of the current directory in long format, showing details such as permissions, owner, size, and date.
cd /path/to/directory: changes the current directory to the specified directory.
mkdir newdirectory: creates a new directory called "newdirectory" in the current directory.
rm -r directory: removes the directory called "directory" and all its contents recursively.
echo "Hello, world!": prints the text "Hello, world!" to the console.
cat myfile.txt: displays the contents of the file "myfile.txt" in the console.
Overall, the command interpreter is a powerful tool for interacting with the operating system and running various tasks and commands. With some practice and familiarity, you can become proficient in using the command interpreter to accomplish your tasks efficiently.



TASK FOR AirBnb clone DEPLOYING STATUS
--------------------------------------
0. Prepare your web servers
---------------------------
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

Install Nginx if it not already installed
Create the folder /data/ if it doesn’t already exist
Create the folder /data/web_static/ if it doesn’t already exist
Create the folder /data/web_static/releases/ if it doesn’t already exist
Create the folder /data/web_static/shared/ if it doesn’t already exist
Create the folder /data/web_static/releases/test/ if it doesn’t already exist
Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
Use alias inside your Nginx configuration
Tip
Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

In optional, you will redo this task but by using Puppet


1. Compress before sending
--------------------------
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None



2. Deploy archive!
------------
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
All remote commands must be executed on your both web servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
Returns True if all operations have been done correctly, otherwise returns False
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function do_pack - like the mv command - depending of your implementation of it, you may don’t need it



3. Full deployment
-----------------
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:

Prototype: def deploy():
The script should take the following steps:
Call the do_pack() function and store the path of the created archive
Return False if no archive has been created
Call the do_deploy(archive_path) function, using the new path of the new archive
Return the return value of do_deploy
All remote commands must be executed on both of web your servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)




4. Keep it clean!
----------------------
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:

Prototype: def do_clean(number=0):
number is the number of the archives, including the most recent, to keep.
If number is 0 or 1, keep only the most recent version of your archive.
if number is 2, keep the most recent, and second most recent versions of your archive.
etc.
Your script should:
Delete all unnecessary archives (all archives minus the number to keep) in the versions folder
Delete all unnecessary archives (all archives minus the number to keep) in the /data/web_static/releases folder of both of your web servers
All remote commands must be executed on both of your web servers (using the env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)
