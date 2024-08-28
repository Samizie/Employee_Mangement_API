
# Employee Management API

This is a RESTful API built with Django and Django REST Framework for managing employee data within an organization. The API allows users to retrieve a list of all employees, get details of a specific employee, add new employees, update existing employee details, record performance reviews, and deactivate an employee's profile.

## Features

- **Employee Management**: Create, retrieve, update, and delete employee records.
- **Department Management**: Assign employees to departments and retrieve department details.
- **Performance Reviews**: Record and manage performance reviews for employees.
- **Employee Deactivation**: Deactivate an employee's profile when necessary.

## Technologies Used

- **Django**: Web framework for building the backend.
- **Django REST Framework**: Framework for building REST APIs in Django.
- **SQLite**: Database used for storing employee and department data.

## Prerequisites

- Python 3.x
- SQLite
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/employee-management-api.git
   cd employee-management-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database settings**:
   - In `settings.py`, update the `DATABASES` setting with your PostgreSQL credentials.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'yourdbname',
           'USER': 'yourdbuser',
           'PASSWORD': 'yourdbpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run migrations** to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** for accessing the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the API** at `http://127.0.0.1:8000/`.

## API Endpoints

Below are the main endpoints available in the Employee Management API:

### 1. Get All Employees

- **Endpoint**: `/employees/`
- **Method**: GET
- **Description**: Retrieves a list of all employees.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "position": "Developer",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "is_active": true,
            "department": {
                "id": 1,
                "name": "Engineering",
                "description": "Handles all engineering tasks."
            }
        }
    ]
    ```

### 2. Get a Specific Employee

- **Endpoint**: `/employees/{id}/`
- **Method**: GET
- **Description**: Retrieves details of a specific employee by ID.

### 3. Create a New Employee

- **Endpoint**: `/employees/`
- **Method**: POST
- **Description**: Adds a new employee to the system.
- **Request Body**:
    ```json
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "position": "Manager",
        "email": "jane.doe@example.com",
        "phone": "0987654321",
        "is_active": true,
        "department_id": 2
    }
    ```

### 4. Update an Existing Employee

- **Endpoint**: `/employees/{id}/`
- **Method**: PUT
- **Description**: Updates details of an existing employee by ID.

### 5. Delete (Deactivate) an Employee

- **Endpoint**: `/employees/{id}/`
- **Method**: DELETE
- **Description**: Deactivates an employee's profile.

## Running Tests

To run the unit tests for the API, use the following command:

```bash
python manage.py test
```

## Postman Documentation

For detailed API usage and examples, refer to the [Postman documentation](#) for this project.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Customization

- **Update Links**: Replace placeholder links, such as `https://github.com/yourusername/employee-management-api.git` and `https://documenter.getpostman.com/view/24624449/2sAXjJ5Cjv#4f4eed9a-d24b-448b-b061-bd24f209d8f7` with the actual links to your repository and documentation.

