# CEN4010-Team3

The project will be done in django and using postgresql.

Prerequisites:
- Have Python3 installed
- Have django installed
- Have a postgres server installd

Downloads: 
- django tutorial: https://docs.djangoproject.com/en/1.10/intro/tutorial01/
- postgres  download: https://www.postgresql.org/


Setting up the postgres server for use with the project:
- Download Postgresql and go through the process of setting it up. Leave the default user to postgres, have an easy to remember password,  and leave the default port to 5432.
- After it is downloaded and installed, you want to create the user we will all be using for it with the database.
- Open up a terminal and test to see if `psql` works. If it is not found by the bash, make sure to add it to your PATH. It should be under `Program Files/PostgresQL/10/bin/` for Windows.
- After you have a terminal open, type in these commands: 
- `psql -U postgres` This will prompt you for a password, use the same one you used when setting up postgresql. This will open up a seperate bash for psql.
- `CREATE USER team3 WITH PASSWORD 'password'; ` This will create the team3 user and password which we will all be using.
- `CREATE DATABASE bookstore_website_project WITH OWNER team3; ` This will create the database that we will be using and assign our user to it. 

If you receive this warning: `The file will have its original line endings in your working directory. warning: LF will be replaced by CRLF in <file>` then use this command in your git repo`git config core.autocrlf true` to surpess that warning.
