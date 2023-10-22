
$ docker compose -f local.yml configs 

"""
$ run make makemigrations before creating superuser
"""
$ make superuser 




  nginx:
    restart: always
    depends_on:
      - api
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/mediafiles
    build:
      context: ./docker/local/nginx
      dockerfile: Dockerfile
    ports:
      - "8080:80"
    networks:
      - nerd_api




installing docker, docker-desktop and logging in


dockerinstall.sh - 
#!/bin/bash
$for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

chmod +u dockerinstall.sh 
./dockerinstall.sh







#### installing docker, docker-desktop and confirm login:


- $ touch dockerinstall.sh -> 

#!/bin/bash
$for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

- $ chmod +x dockerinstall.sh 
- $ ./dockerinstall.sh

install docker-cd 

$ docker volume list 

$ docker volume inspect xyz 



$ docker compose -f local.yml exec postgres backup

python3 -c "import secrets; print(secrets.token_urlsafe(38))"

--------------------------------------------------------------------------------------------------
(venv) user@pop-os:~/.../src/py-api$ make superuser
docker compose -f local.yml run --rm api python3 manage.py createsuperuser 
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
[+] Creating 3/0
 ✔ Container mailhog   Running                                                                  0.0s 
 ✔ Container postgres  Running                                                                  0.0s 
 ✔ Container redis     Running                                                                  0.0s 
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
PostgreSQL is available
Email address: jpnamausa@gmail.com
First name: Jason
Last name: Preneveau
Password: 
Password (again): 
Superuser created successfully.
(venv) user@pop-os:~/.../src/py-api$ make makemigrations
docker compose -f local.yml run --rm api python3 manage.py makemigrations
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
[+] Creating 3/0
 ✔ Container mailhog   Running                                                                  0.0s 
 ✔ Container redis     Running                                                                  0.0s 
 ✔ Container postgres  Running                                                                  0.0s 
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
PostgreSQL is available
Migrations for 'profiles':
  core_apps/profiles/migrations/0001_initial.py
    - Create model Profile
(venv) user@pop-os:~/.../src/py-api$ make migrate
docker compose -f local.yml run --rm api python manage.py migrate 
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
[+] Creating 3/0
 ✔ Container mailhog   Running                                                                  0.0s 
 ✔ Container postgres  Running                                                                  0.0s 
 ✔ Container redis     Running                                                                  0.0s 
[+] Building 0.0s (0/0)                                                         docker:desktop-linux
PostgreSQL is available
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, profiles, sessions, sites, users
Running migrations:
  Applying profiles.0001_initial... OK
(venv) user@pop-os:~/.../src/py-api$ 
 0:bash*                                                                                                                                                                              "pop-os" 14:30 20-Oct-23



JWT auth tokens:
from venv:

used to sign JWT:
python secrets package
 -c executes python satements from command line as a script
$ python3 -c "import secrets; print(secrets.token_urlsafe(38)) 

copy and paste key into .envs/.local/.django in SIGNING_KEY env variable

SIGNING_KEY=<key>