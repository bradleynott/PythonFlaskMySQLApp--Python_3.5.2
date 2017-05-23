# PythonFlaskMySQLApp--Python_3.5.2
Python Flask App tutorial updated for Python 3.5.2

Brad Nott
bradley.nott@gmail.com

Hello! This repository contains my modifications to the Python Flask App tutorial created by Jay that you can find here:

https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

The original tutorial needed some modifications in order to function correctly with Python 3.5.2,
so hopefully if you are stuck you will find my files helpful.

List of Changes:

1. app.py

  - The app.py file is mostly modeled after the file that Jay includes in his repository
    https://github.com/jay3dec/PythonFlaskMySQLApp---Part-1
    
  - My import statement includes "import pymysql" because you cannot establish a MySQL connection in
    Python 3 using flask-mysql
  
  - In the signUp function I started with assignment statements for the SQL connection and cursor.
    If you do not do this the logic will call the finally statement and try to call the close methods
    on cursor and conn. If cursor and conn haven't been assigned then you will get an error.
    
  - I was getting the error {"error": "(1406, \"Data too long for column 'user_password' at row 1\")"}
    This error occurs because the SQL stored procedure created in the "Creating a Signup Page" section
    limits the size of p_password to 20. The information that the program tries to add to this table column
    is the output from the hashing function. I added a print statement to see the length of the hashed password
    text string. The value I received was 66, so I then modified the stored procedure p_password size to 66, and 
    modified the database table column data type size to 66 as well.
    
      - NOTE: If you have already created the stored procedure, I suggest using the MySQL Workbench to make the
              needed changes. The graphical interface is easier to navigate and you can quickly modify both the
              stored procedure and the table column.
              
  2. signup.html
  
    - I added the following references to the jquery files in the signup.html file
    
        	<script src="../static/js/jquery-3.2.1.js"></script>
	        <script src="../static/js/signUp.js"></script>
          
When I run the files provided in this repository I can successfully log the user-provided data to a MySQL database.

Thanks to Jay for putting in the time to draft up the original tutorial, as well as the troubleshooting ideas
provided by the programmers in the tutorial comments section. I had a lot of fun learning how to integrate
these programming pieces to form a functioning web interface.

If you can't get my files to work for you in Python 3, send me your questions and I will help you troubleshoot.
Happy programming everyone!

-Brad
