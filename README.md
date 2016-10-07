# poll_app

This is a basic app used to learn django.


#Installation of Requiremets

1) Apache2

Run the following command in terminal to install
    
     $ sudo apt-get install apache2
     
2) mysql-server

Run the following commands in terminal
    
    $ sudo apt-get install mysql-server
    
3) python2.7

Run the following commands in terminal
    
    $ sudo apt-get install python
    
4) python-pip

Run the following commands in terminal
    
    $ sudo apt-get install python-pip

5) python-mysqldb

Run the following commands in terminal
    
    $ sudo apt-get install python-mysqldb

6) django

Run the following commands in terminal
    
    $ sudo pip install django==1.7


##Steps for Installation -:

1) Fork this repository and clone the forked repository
    
    $ git clone 'link to your forked repository'

2) Create a database for LibreHatti.
    
    $ mysql -u root -p
    $ create database mysite;
    $ quit
    
3) Edit settings.py file in mysite/polls directory. Things to be edited are:

Line No 60 : DATABASES
    
    NAME : mysite
    USER : Your MySQL username
    PASSWORD : Your MySQl password
        
4) Go to the project directory and run the following commands.
    
    $ cd mysite
    $ python manage.py migrate
    $ python manage.py runserver 127.0.0.1:8090
    
5) Open 'localhost:8090' in your browser.
