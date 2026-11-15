Veda-Technology-Internship
Build a Python REST API
1. Project Overview
The Python REST API is a basic backend application that manages a collection of records through HTTP endpoints. It allows users to create, retrieve, update, and delete records using standard REST API operations.

The application is developed using Python and Flask, with SQLite used to store records. It demonstrates CRUD functionality, HTTP methods, JSON data handling, input validation, database integration, and meaningful HTTP status codes.
2. Objectives
- Understand the fundamentals of REST API development.
- Develop a basic backend API using Python.
- Implement Create, Read, Update, and Delete (CRUD) operations.
- Use appropriate HTTP methods for different operations.
- Store and retrieve records using an SQLite database.
- Accept and return data in JSON format.
- Validate incoming request data.
- Return meaningful HTTP status codes.
- Handle errors such as missing records and invalid input.
3. Features
- Create records using POST.
- Retrieve all records using GET.
- Retrieve an individual record using its ID.
- Replace a record using PUT.
- Update selected fields using PATCH.
- Delete records using DELETE.
- Automatically create the SQLite database and table.
- Validate incoming JSON data.
- Return appropriate HTTP status codes and error messages.
- Provide a root endpoint listing the available API routes.
4. Technologies Used
- Programming Language: Python 3
- Framework: Flask
- Database: SQLite
- Database Module: sqlite3
- Data Format: JSON
- HTTP Methods: GET, POST, PUT, PATCH, DELETE
- IDE: Visual Studio Code
- API Testing: Postman, browser, or curl
- Version Control: Git and GitHub
5. Project Structure
Python-REST-API/
│
├── app.py
├── records.db       (created automatically)
└── README.md
6. Installation and Execution
1. Install Python 3.
2. Open a terminal in the project folder.
3. Install Flask:
python -m pip install flask
4. Run the application:
python app.py
5. Open the API at:
http://127.0.0.1:5000
The SQLite database and its table are created automatically when the application starts.
7. API Endpoints
HTTP Method	Endpoint	Purpose
GET	/	View API information
GET	/records	Retrieve all records
POST	/records	Create a new record
GET	/records/<id>	Retrieve a record by ID
PUT	/records/<id>	Replace an existing record
PATCH	/records/<id>	Update selected fields
DELETE	/records/<id>	Delete a record


8. Sample API Requests
Create a record
Method: POST
URL: http://127.0.0.1:5000/records

JSON body:
{
    "title": "First Record",
    "description": "This is a sample record."
}
Expected status: 201 Created
Retrieve all records
Method: GET
URL: http://127.0.0.1:5000/records

Expected status: 200 OK
Retrieve one record
Method: GET
URL: http://127.0.0.1:5000/records/1

Expected status: 200 OK if the record exists.
Replace a record
Method: PUT
URL: http://127.0.0.1:5000/records/1

JSON body:
{
    "title": "Updated Record",
    "description": "The record has been replaced."
}
Expected status: 200 OK
Partially update a record
Method: PATCH
URL: http://127.0.0.1:5000/records/1

JSON body:
{
    "description": "Only the description has been updated."
}
Expected status: 200 OK
Delete a record
Method: DELETE
URL: http://127.0.0.1:5000/records/1

Expected status: 200 OK if deletion succeeds.
9. HTTP Status Codes
Status Code	Meaning	Usage
200	OK	Successful retrieval, update, or deletion
201	Created	Record created successfully
400	Bad Request	Invalid or missing input
404	Not Found	Record or endpoint does not exist
405	Method Not Allowed	HTTP method is not supported


10. Input Validation
The API validates incoming JSON data before performing database operations.
- The request body must contain a JSON object.
- The title field is required when creating or replacing a record.
- The title must be a non-empty string.
- The description must be a string.
- Unknown fields are rejected.
- PATCH requests must contain at least one valid field.
- Invalid requests receive a 400 Bad Request response.
11. Testing
The API can be tested using Postman or another API testing tool.

The following operations should be tested:
- Creating a new record using POST.
- Retrieving all records using GET.
- Retrieving a specific record using its ID.
- Replacing a record using PUT.
- Updating selected fields using PATCH.
- Deleting a record using DELETE.
- Submitting an empty or invalid request body.
- Attempting to retrieve a record that does not exist.
- Attempting to delete a record that does not exist.
- Checking whether the API returns the correct HTTP status codes.
12. Advantages
- Provides a simple introduction to backend development.
- Demonstrates REST API principles.
- Supports all basic CRUD operations.
- Uses SQLite for lightweight database storage.
- Separates API operations into individual endpoints.
- Validates incoming data.
- Returns meaningful HTTP status codes.
- Uses JSON for communication between clients and the server.
- Requires minimal setup.
- Uses a lightweight framework and database.
13. Future Enhancements
- Implement user authentication and authorization.
- Add pagination and search functionality.
- Introduce advanced request validation.
- Add automated API tests using pytest.
- Implement API documentation using Swagger or OpenAPI.
- Add database migration support.
- Introduce logging and monitoring.
- Deploy the API to a cloud hosting platform.
- Add rate limiting and additional security measures.
- Connect the API to a frontend application.
14. Real-World Applications
- Backend services for web applications.
- Data management systems.
- Inventory management applications.
- Student and employee record management.
- Task management applications.
- Mobile application backends.
- Database-driven applications.
- Communication between frontend and backend systems.
15. Conclusion
The Python REST API project demonstrates how Python and Flask can be used to develop a basic backend application that manages records through RESTful endpoints. By implementing CRUD operations, SQLite database integration, JSON data handling, input validation, and appropriate HTTP status codes, the project introduces the fundamental concepts of REST API development.

It provides practical experience in building backend services and establishes a foundation for developing more advanced web APIs and database-driven applications.
