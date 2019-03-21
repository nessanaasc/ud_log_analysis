## Vanessa Nascimento Log Analysis Project

## About
This project contains a Python Code that print a report about articles, authors and events related to views.
The queries for extract the report are built to access a Postgree database called news.

## Project Files
For run the project you will need to download the following files:
1. Vagrantfile 
2. log_analysis.py
3. newdata.zip

## Softwares Requirements
You also will need the following softwares in your computer to run the application:
1. Python 3 - For download and install: https://www.python.org/downloads/
2. Git Bash - For all commands line. You will need have Git install. Download in https://git-scm.com/downloads
3. Virtualbox 5.1.38 e Vagrant 2.2.4 - If you have a Mac or Windows system, you will need have a Virtual Machine to run a Linux System. This project was created using a Virtual Box (You don't need a extension package or SDK) and Vagrant. For download e install acess: https://www.virtualbox.org/wiki/Downloads and https://www.vagrantup.com/downloads.html.
For check the Vagrant install, you can run `vagrant --version` in your prompt
For VM configuration, you can download and unzip https://github.com/udacity/fullstack-nanodegree-vm in a directory

## How to run the Application
1. Download Vagrantfile, log_analysis.py and newdata.zip files and put in a directory. 
2. You will need unzip the file newdata.zip for access the PostgreSQL database news. You can use the file newdata.zip in my github ou access https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. From the command line, navigate until the directory where are the files and run `vagrant up`
3. Run `vagrant ssh` to login in the Linux System
4. Load the database with the command `psql -d news -f newsdata.sql`. The database contains three tables (articles, author and log). You can use \dt \d table_name for explore your database (Example: \d articles)
5. Run `python log_analysis.py` to starts this application

## Contribution
You can edit log_analysis.py to create your own PostgreSQL queries and extract more data and information
