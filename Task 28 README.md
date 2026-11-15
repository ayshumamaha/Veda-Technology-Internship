# Veda-Technology-Internship

---

# Build a Python REST API

---

## 1. Project Overview

The Python REST API is a basic backend application that manages a collection of records through HTTP endpoints. It allows users to create, retrieve, update, and delete records using standard REST API operations.

The application is developed using Python and Flask, with SQLite used to store the records.

The project demonstrates CRUD functionality, HTTP methods, JSON data handling, input validation, database integration, and meaningful HTTP status codes.

## 2. Objectives

- Understand the fundamentals of REST API development.
- Develop a basic backend API using Python.
- Implement Create, Read, Update, and Delete (CRUD) operations.
- Use appropriate HTTP methods for different operations.
- Store and retrieve records using an SQLite database.
- Accept and return data in JSON format.
- Validate incoming request data.
- Return meaningful HTTP status codes.
- Handle errors such as missing records and invalid input.

## 3. Features

- **Create Records:** Add new records using POST requests.
- **Retrieve Records:** View all records or retrieve an individual record using GET requests.
- **Update Records:** Replace existing records using PUT requests.
- **Partial Updates:** Modify selected record fields using PATCH requests.
- **Delete Records:** Remove records using DELETE requests.
- **Database Integration:** Automatically creates an SQLite database and records table.
- **Input Validation:** Validates incoming JSON data before processing.
- **Error Handling:** Returns appropriate error messages for invalid requests.
- **HTTP Status Codes:** Uses meaningful status codes to indicate API responses.

## 4. Technologies Used

- **Programming Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite
- **Database Module:** sqlite3
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, PATCH, DELETE
- **IDE:** Visual Studio Code
- **API Testing:** Postman / Browser / curl
- **Version Control:** Git and GitHub

## 5. Project Structure

```text
Python-REST-API/
│
├── app.py
├── records.db
└── README.md
```

*Note: The records.db file is generated automatically when the application runs.*

## 6. Installation and Execution

**Step 1: Install Flask**

```bash
python -m pip install flask
```

**Step 2: Run the application**

```bash
python app.py
```

**Step 3: Open the API**

```text
http://127.0.0.1:5000
```

The application starts the Flask development server and automatically creates the SQLite database and required table.

## 7. API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display API information |
| GET | `/records` | Retrieve all records |
| POST | `/records` | Create a new record |
| GET | `/records/<id>` | Retrieve a specific record |
| PUT | `/records/<id>` | Replace an existing record |
| PATCH | `/records/<id>` | Update selected fields |
| DELETE | `/records/<id>` | Delete a record |

## 8. Sample API Requests

**1. Create a Record (POST)**

URL: `http://127.0.0.1:5000/records`

Request Body:

```json
{
    "title": "First Record",
    "description": "This is a sample record."
}
```

Expected Status Code: `201 Created`

**2. Retrieve All Records (GET)**

URL: `http://127.0.0.1:5000/records`

Expected Status Code: `200 OK`

**3. Retrieve a Specific Record (GET)**

URL: `http://127.0.0.1:5000/records/1`

Expected Status Code: `200 OK`

**4. Update a Record (PUT)**

URL: `http://127.0.0.1:5000/records/1`

Request Body:

```json
{
    "title": "Updated Record",
    "description": "The record has been replaced."
}
```

Expected Status Code: `200 OK`

**5. Partially Update a Record (PATCH)**

URL: `http://127.0.0.1:5000/records/1`

Request Body:

```json
{
    "description": "Updated description."
}
```

Expected Status Code: `200 OK`

**6. Delete a Record (DELETE)**

URL: `http://127.0.0.1:5000/records/1`

Expected Status Code: `200 OK`

## 9. HTTP Status Codes

| Status Code | Meaning | Purpose |
|---|---|---|
| 200 | OK | Successful request |
| 201 | Created | Record created successfully |
| 400 | Bad Request | Invalid input data |
| 404 | Not Found | Requested record or endpoint does not exist |
| 405 | Method Not Allowed | Unsupported HTTP method |

## 10. Input Validation

The application validates incoming JSON data before performing database operations.

- The request body must contain a valid JSON object.
- The title field is mandatory when creating or replacing a record.
- The title must be a non-empty string.
- The description must contain a string value.
- Unknown fields are rejected.
- PATCH requests must contain at least one valid field.
- Invalid requests return a `400 Bad Request` response.

## 11. Testing

The API can be tested using Postman or other API testing tools.

The following test scenarios are included:

- Creating a new record using POST.
- Retrieving all records using GET.
- Retrieving a specific record using its ID.
- Replacing a record using PUT.
- Updating selected fields using PATCH.
- Deleting a record using DELETE.
- Submitting an empty or invalid request body.
- Retrieving a non-existent record.
- Deleting a non-existent record.
- Verifying appropriate HTTP status codes.

## 12. Advantages

- Provides practical experience in backend development.
- Demonstrates REST API principles.
- Supports all basic CRUD operations.
- Uses SQLite for lightweight database storage.
- Validates incoming data.
- Returns meaningful HTTP status codes.
- Uses JSON for data exchange.
- Requires minimal installation and configuration.
- Uses a lightweight Python framework.

## 13. Future Enhancements

- Implement user authentication and authorization.
- Add pagination and search functionality.
- Introduce advanced request validation.
- Implement automated testing using pytest.
- Add API documentation using Swagger or OpenAPI.
- Introduce logging and monitoring.
- Deploy the API to a cloud hosting platform.
- Add additional security mechanisms.
- Integrate the API with a frontend application.

## 14. Real-World Applications

- Backend services for web applications.
- Inventory management systems.
- Student and employee record management.
- Task management applications.
- Mobile application backends.
- Database-driven applications.
- Communication between frontend and backend systems.

## 15. Conclusion

The Python REST API project demonstrates how Python and Flask can be used to develop a basic backend application that manages records through RESTful endpoints.

By implementing CRUD operations, SQLite database integration, JSON data handling, input validation, and appropriate HTTP status codes, the project introduces the fundamental concepts of REST API development.

It provides practical experience in building backend services and establishes a foundation for developing more advanced web APIs and database-driven applications.

## Author
M. Ayshwarya
