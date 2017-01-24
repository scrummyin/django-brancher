# django-brancher
This is a Django app to help manage branches that contain database migrations. It basically creates a new database from a template of the existing default database and then uses that new branch-specific database for `./manage.py migrate` and `./manage.py runserver` commands.

*This is not intended for production use.*

## Example

### Requirements
  * git
  * postgres
  * your postgres user has createdb permission (`alter role <user> createdb;`)
  * django-brancher installed via pip
  * brancher added to your Django installed apps

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
Run a command with DATABASES['default']['NAME'] set to DATABASES['default']['NAME']_`$ git rev-prse --abbrev-ref HEAD`

```
python manage.py branch_it diffsettings
```

### List
List all branched databases available
```
python manage.py branch_ls
```

### Create
Makes a database based off the current default database given a unique name based on the default database name plus the branch name (e.g. `$ git rev-prse --abbrev-ref HEAD`)
```
$ python manage.py branch_mk
```

### Delete
Deletes the branched database based off the result of `$ git rev-prse --abbrev-ref HEAD`
```
$ python manage.py branch_rm
```
