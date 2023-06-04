# Overview

In order to log and manage cybersecurity incidents, I set out to develop a straightforward back-end solution that connects with a SQL Relational Database.

A Python-based cybersecurity log management system is the program I created. It stores and retrieves data using SQLite, a serverless and file-based SQL database engine. SQL utilizes insert, retrieve, update, and delete statements for logs from the database using the application, which offers the essential functionality needed to successfully handle security occurrences.

This software was created with the intention of gaining practical experience with databases, SQL, and cybersecurity-related ideas. I wanted to improve my knowledge of relational database integration, SQL commands, and database interfaces by creating this software.

[Software Demo Video](https://drive.google.com/file/d/11h3M2YlRABBIxdXxuCBhdq5YYL6rQbr4/view?usp=sharing)

# Relational Database

I utilized a SQLite Relational Database for this project. The application creates and immediately accesses the database, which is kept in a file called "cybersecurity.db."

'security_logs' is the name of a single table in the database. 'id' (an integer and the table's primary key), 'event' (a text column), and 'timestamp' (a date/time) are its three columns. The 'id' column acts as a special identifier for each log entry, the 'event' column contains the details of the security event, and the 'timestamp' column keeps track of the time and date of each log entry.

# Development Environment

I utilized the following resources to create this software:

* The primary programming language for creating code and interacting with databases is Python.
* The integrated development environment (IDE) where the code was written and run was Visual Studio Code.
* Using the sqlite3 package, the relational database engine SQLite is incorporated into Python.
* The Visual Studio Code SQLite addon made it simple to view and interact with the database inside the IDE.

# Useful Websites

During the creation of this project, the following websites offered useful resources and information:

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)

# Future Work

This project can be enhanced and improved in a number of ways in the future:

- Implementing the program to work with an SQL Server that is actively running.
- Putting in place access control and user authentication systems to secure the database and prevent unwanted access.
- The inclusion of new features, like the ability to filter logs using a set of criteria or create reports using certain log properties.
- Improving error handling and input verification to protect against SQL injection attacks and ensure data integrity.
putting in place data backup and recovery procedures to protect against corrupting or losing data.
- Making database searches and indexing techniques more efficient for larger data sets.

These are some of the possible directions the cybersecurity log management system could go in the future.
