--------------------------------WITH DOCKER----------------------------------

    docker compose build
    docker compose up
    docker ps
    docker exec -it <container_name> python manage.py makemigrations
    docker exec -it <container_name> python manage.py migrate
    docker exec -it <container_name> python manage.py createsuperuser

    docker exec -it <container_name> python imports.py
    docker exec -it <container_name> python remuneration_enrollment.py


-------------------------------USEFUL LINKS----------------------------------

    http://127.0.0.1:8000/admin/user/maksisuser/
    http://127.0.0.1:8000/api/ref_users/
