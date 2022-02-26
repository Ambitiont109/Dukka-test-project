## Run the project on the local machine
-run script
```
sudo docker-compose up -d
```
- Navgiate http://127.0.0.1:8000/swagger-ui/

## API DETAIL
- Receipt API
1. /api/receipt/create/ <br/> 
Generate the celery  task and returns the task_id. We will use this in task detail API.
It is using Token Authentication of Django Rest Framework and only Admin User can call this api
3. /api/receipt/detail/<task_id> <br/>
Get the state of certain task.
if task state is "PROGRESS", it returns the current id of PDF.
It is using Token Authentication of Django Rest Framework and only Admin User can call this api
- User API
1. GET /api/users/
    List the Users
2. POST /api/users
   Create the User

## Swagger UI 
- You can browse API with swagger UI on http://<domain_name>/swagger-ui/