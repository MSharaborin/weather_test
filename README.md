# Getting started
****

### Requirements
****
    django-ninja==0.16.1
    pytest==6.2.5
    httpx==0.21.0

### How start
****
1. Start docker

   family_doctor.settings => uncomment => Databases: docker host and port 

         
         docker-compose up -d

2. Start in console

   family_doctor.settings => uncomment => Databases: localhost host and port 
   

         uvicorn family_doctor.asgi:application