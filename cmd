#dokcer cmd
    docker-compose build
    docker-compose run --rm app sh -c "python manage.py runserver"
    docker-compose up
    