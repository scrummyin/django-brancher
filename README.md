# brancherer
This is a django app to help manage branches that contain migrations.

## Example:
Requirements for now:
  - git
  - postgres
  - postgres user has createdb permission (This is one of the many reasons you should not use this on production)

`
git checkout -b funtime
<code up some migrations and run makemigrations>
python manage.py branch_mk
python manage.py branch_it migrate
python manage.py branch_it runserver
python manage.py branch_rm
`

###List :
python manage.py branch_ls

###Create :
python manage.py branch_mk

###Delete :
python manage.py branch_rm
