# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that handles common web service tasks such as reading data, creating resources, and returning JSON responses. This assignment introduces students to routes, request validation, and API design patterns used in modern backend development.

## 📝 Tasks

### 🛠️ Create the API Foundation

#### Description
Set up a FastAPI application and define a basic welcome endpoint that returns a simple JSON response.

#### Requirements
Completed program should:

- Install and import `FastAPI`.
- Create an app instance and define a root route using `@app.get()`.
- Return a JSON payload such as a welcome message or a simple status response.
- Run the app locally and confirm the endpoint responds correctly.

### 🛠️ Build a Resource Endpoint

#### Description
Create an endpoint that returns a collection of sample data, such as books, students, or tasks.

#### Requirements
Completed program should:

- Define a route that returns a list of objects in JSON format.
- Use clear keys and values that describe each item.
- Return a structured response body instead of plain text.
- Test the endpoint in the browser or with a request client.

### 🛠️ Add a Create Endpoint

#### Description
Add a POST route that accepts input and creates a new resource in memory.

#### Requirements
Completed program should:

- Accept JSON data from a client request.
- Validate required fields using Pydantic models or equivalent FastAPI validation.
- Store or simulate storing the resource in memory.
- Return the created object with a success response.

### 🛠️ Stretch Goal: Add a Detail Endpoint

#### Description
Create an endpoint that reads one item by ID and returns its details.

#### Requirements
Completed program should:

- Define a route using a dynamic parameter such as `/items/{item_id}`.
- Return the matching item if it exists.
- Handle missing items with a meaningful 404-style response.
- Use clear JSON responses for success and error cases.
