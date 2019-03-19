## Vanessa Nascimento Log Analysis Project

## About
This project contains a Python Code that print a report about articles, authors and events related to views.
The queries for extract the report are built to access a Postgree database called news.

## Download and Installation
For access the project you will need to download the following files:
1. Vagrantfile 
2. log_analysis.py
3. newdata.sql

You also will need the following softwares in your computer:
1. Python 3
2. Virtualbox (To run a Linux System)
3. Vagrant
4. Command Line (Git Bash - Windows System Users)

## How to run the Application
1. Download Vagrantfile, log_analysis.py and newdata.sql files and put in a directory
2. From the command line, navigate until the directory and run `vagrant up`
3. Run `vagrant ssh` to login in the Linux System
4. Load the database with the command `psql -d news -f newsdata.sql`. The database contains three tables (articles, author and log)
5. Run `python log_analysis.py` to starts this application

