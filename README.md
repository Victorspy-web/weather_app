# Weather App

This project is used to check the current weather in any city

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

**Prerequisites**

```
Check requirements.txt for packages to install
```

**Installations for mac and linux users**

```
First clone the repository from Github and switch to the project directory
```

* git clone git@github.com/USERNAME/{{ project_name }}.git
* cd {{ project_name }}


```
Open terminal and install pipenv for your project
```

`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* sudo apt install pipenv

```
Install Django, activate and migrate project
```

* pipenv install django==3.1.4 . `Dont forget the space and dot at the end!`
* pip install requests
* pipenv shell
* python manage.py makemigrations
* python manage.py migrate


```
Create django superuser
```

* python manage.py createsuperuser
    * Fill in the fields to create a superuser `Passwords are invisble`


```
You can now run the development server
```

* python manage.py runserver
    * `Paste this link in your browser to run local server` http://127.0.0.1:8000
