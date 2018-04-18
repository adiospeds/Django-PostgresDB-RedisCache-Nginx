# Django-PostgresDB-RedisCache-Nginx
A Hello world Django project that shows how redis can be used as a caching system for Django.

Clone the project from below github link onto your machine: 
Ensure docker version 17.03+ and docker-compose is installed.
Steps to deploy the project:
1. Enter the Project directory where you will find the docker compose file.
2. Run "docker-compose build" to create the images from Dockerfiles.
3. Run "docker-compose up -d" to start the stack
  - This will spawn 4 instances of Docker.
    - The Django Web instance which contains the actual code.
    - The Postgres instance which acts as a database for Django.
    - The Redis Instance which acts as a caching layer.
    - The Nginx instance which acts as a reverse proxy for the Django Web instance.
  - Access http://localhost:80 on your browser to access the project and it should display "Hello World"
  - Steps to check if caching works:
    - Run "docker inspect \<container-id\>" on the redis instance and copy it's ip.
    - Then telnet to the redis instance using "telent <redis-container-ip> 6379".
    - Run "FLUSHALL" command inside telnet shell to flush the redis cache.
    - Then run "MONITOR" command to start monitoring the redis instance for any set-get events. (If monitor displays "OK" rerun       the "MONITOR" command until it waits for events.)
    - Now goto your browser and access http://localhost
      - As soon as you access the Hello-World app, you see a lot of SET requests in the telnet session under monitor.
      - You may see a few SET requests in the couple of intial requests, however if you continue to refresh your browser(http://localhost), you will only see the only GET requests under the telnet session.
      - WHAT HAPPENDED HERE:
        - During the first few requests, the django app goes to the redis cache, and since it doens't find relevant cache, it               pull the data from respective filesystem/postgres DB and before serving the data makes a cache entryfor the data in             redis. This is where you will see the SET events in telnet session.
        - Later when you refresh your browser multiple times, most of the responses are cached in redis and django will simply            make GET calls to redis and serve the data from Memory, instead of quering the filesystem/DB. This is where you will            start seeing a lot of GET events inside the telnet session

