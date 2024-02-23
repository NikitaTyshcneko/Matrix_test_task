**Copy code**
```
git clone https://github.com/NikitaTyshcneko/Matrix_test_task.git
cd Matrix
```

**Install dependencies:**
```
pip install -r requirements.txt
```
**Apply migrations:**
```
python manage.py makemigrations
python manage.py migrate
```

**Run the Django development server:**
```
python manage.py runserver
```

**API Endpoints**

GET api/v1/matrix/traverse/{matrix_id} - Print traverse matrix by id

POST api/v1/matrix/add - add new matrix

GET /api/v1/docs/ - Ninja documentation.

**Testing**
```
pytest
```

**Dockerization**
The application is containerized using Docker for easy deployment and scalability. Use the provided Dockerfile to build the Docker image.
```
docker-compose up --build 
```