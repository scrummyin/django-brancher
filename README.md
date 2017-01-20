# brancherer
This is a django app to help manage branches that contain migrations. This is not intended for production use.

## Example

### Requirements for now
  * git
  * postgres
  * your postgres user has createdb permission (alter role <user> createdb;)
  * django-brancherer installed via pip
  * brancherer added to your installed apps

### Sample workflow
This is an example work flow to create a new branch, run migrations on it, start runserver, and finally delete it.
```
git checkout -b funtime
<code up some migrations and run makemigrations>
python manage.py branch_mk
python manage.py branch_it migrate
python manage.py branch_it runserver
python manage.py branch_rm
```

## Commands

### Run command
List all branches based off DATABASES['default']['NAME']
```
python manage.py branch_ls
```

### List
List all branches based off DATABASES['default']['NAME']
```
python manage.py branch_ls
```

### Create
Makes a database based of the result of `$ git rev-prse --abbrev-ref HEAD`
```
$ python manage.py branch_mk
```

### Delete
Deletes a database based of the result of `$ git rev-prse --abbrev-ref HEAD`
```
$ python manage.py branch_rm
```
