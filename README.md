# Python Webserver

This is a basic web server written in Python using Flask. The goal of this program is to populate a database with random names and display them in a basic web application.

This project has been dockerized and can now be launched using the command:

```bash
docker-compose up -d
```

This will set up the database as well as two webservers using the nginx loadbalancer. App will be available at http://localhost.

Installing [python3.9](https://www.python.org/downloads/) and all python dependencies is required to execute the projects without using Docker. All of the commands listed below must be run from within the webserver/ directory.

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

When you use the app, it will automatically send you to the /greetings page, where you can see the number of rows in the database, as well as the most recent 10 names added to the database.

A POST method to the /messages location will insert a random name into the database. Return to the greetings page to see the updated information.

## Vagrant

Vagrant has been enable to use on this project! This will require the installation of Vagrant and Virtualbox in your local machine.

To spin everything up just run the following command:

```bash
cd ansible
vagrant up
```

This will install Ubuntu on a virtual machine and use Ansible to deploy the application. Vagrant will establish a port forwarding rule to http://localhost:8080 so that you may utilize the app from your browser.
