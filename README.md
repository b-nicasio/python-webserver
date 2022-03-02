# Python Webserver

This is a basic web server written in Python using Flask. The goal of this program is to populate a database with random names and display them in a basic web application.

This project has been dockerized and can now be launched using the command:

```bash
docker-compose up -d
```

This will set up the database as well as two webservers using the nginx loadbalancer. App will be available at http://localhost.

Installing python3.9 and all python dependencies is required to execute the projects without using Docker.
Note: All of the commands listed below must be run from within the webserver/ directory.

To install all python dependencies simply run:

```bash
pip install -r requirements.txt
```

Copy env file:

```bash
cp .env.example .env
```

Running the webserver:

```bash
python3 app.py
```

When you launch the program, it will assume that you have a database with all of your data stored in a MySQL database. Change the database credentials in de.env and run the migrations and seeders to run the database migrations and seeders:

```bash
python3 db_migration.py
python3 db_seed.py
```

## Using the webserver

If it’s a GET on /greeting, it shall respond with a simple text with the total number of
rows in the DB.
- Otherwise, if it’s a POST on /messages, it should add a new row, using some default
values and shall return the content of the newly added row.
- The / route should temporarily redirect to the /greeting route.
- All operations should return the appropriate HTTP status codes.

## Vagrant

Vagrant has been enable to use on this project! This will require the installation of Vagrant and Virtualbox in your local machine.

To spin everything up just run the following command:

```bash
cd ansible
vagrant up
```

This will install Ubuntu on a virtual machine and use ansible to provide the application. Vagrant will establish a port forwarding rule to http://localhost for you so that you may utilize the app from your browser.
