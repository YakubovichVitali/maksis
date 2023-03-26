WITHOUT DOCKER

 - python3 -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser


TO UPLOAD DATA TO DATABASE FROM DATA.JSON

in python console:

    from imports import import_referral_users
    import_referral_users.execute()


TO COUNT REMUNERATION

in python console:

    from remuneration_enrollment import remuneration_enrollment
    remuneration_enrollment.execute()


USEFUL LINKS

    http://127.0.0.1:8000/admin/user/maksisuser/
    http://127.0.0.1:8000/api/ref_users/
