Hello there !
if you want to lounch the app,
you need to follow this stepes:

Linux/MacOS (if you have Docker)
```
  docker-compose -f docker-compose.yaml up -d --build
```
Congrats you've lounched the app
If you want to create super user
```
  docker exec -it backend_menu-api-1 python3 manage.py createsuperuser
```
write your data
