# Getting started
****

### Requirements
****
      django-ninja==0.16.1
      pytest==6.2.5
      pytest-django==4.4.0
      pytest-asyncio==0.16.0
      httpx==0.21.0
      psycopg2-binary==2.9.2
      uvicorn==0.15.0

### How start
****
1. Start docker

   family_doctor.settings => uncomment => Databases: docker host and port 

         
         docker-compose up -d

2. Start in console

   family_doctor.settings => uncomment => Databases: localhost host and port 
   

         uvicorn family_doctor.asgi:application

3. Start Test
   
      For Unix system
   
         pytest -v tests/test_api.pi

      For Windows system
   
         pytest -v tests\test_api.pi