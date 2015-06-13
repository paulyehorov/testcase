<h1>Vagrant + Flask + Ansible testcase repository</h1>

This repository contains ready-to-use set of Vagrantfile, web-application, described in task, tests to it
and two Ansible roles, that will install MongoDB to virtual machine and start an application.

There no crypted variables, so you don't need to use vault_pass file for using Ansible roles.

<h3>Ansible roles design overview</h3>

Each role has few directories:
 - tasks - Directory with main.yml file, which contains main installation tasks;
 - defaults - Directory contains .yml file with variables;
 - handlers - Directory contains file with handlers description;
 - files - Directory contains files that should be copied to virtual machine

If you need to use Ansible roles without Vagrantfile, move to "provsioning"
directory, set correct IP-address to inventory and use the following command:

`ansible-playbook playbook.yml -i inventory tags=mongodb, flaskapp`

If you need to run only one role - use appreciate tag.

NOTE. You must have pre-installed Ansible version 1.6 or later to use these roles

<h3>Flask application overview</h3>

This is a small Flask application, that listens port 8080, with two endpoints:
 - http://ip-address:8080/post - recieves only POST requests with JSON payload like 
 {'uid': '1', 'name': 'John Doe', 'date': '2015-05-12T14:36:00.451765', 'md5checksum': 'e8c83e232b64ce94fdd0e4539ad0d44f'}
 and checks MD5 checksum of uid, name and date fields. If checksum is correct - it saves data to MongoDB database.
 - http://ip-address:8080/get - recieves only GET request with the simillar JSON payload, but with only two fields - uid
 and data. For given parameters it will return number of occurences of a given UID (John Doe) for that day.

For using application you must have pre-installed Python version 2.7 or later, virtualenv, Flask and
Flask extension library - Flask-PyMongo.

NOTE. TCP port 8080 should be opened and free before starting application in order to allow it receiving requests.

To run application use the following commands:
```
cd "application_folder" 
virtualenv venv
python flaskapp.py
```
<h3> Application tests overview</h3>

There are 4 unit-test - 2 for each endpoint. For each endpoint there is one test with correct data and one with incorrect.
Tests are waiting for correct application responses.

To run tests use the following commands:
```
cd "application_folder" 
python app_tests.py
```

<h3>Author information</h3>
Created in 2015 by Paul Yehorov. email: paul.yehorov@gmail.com
