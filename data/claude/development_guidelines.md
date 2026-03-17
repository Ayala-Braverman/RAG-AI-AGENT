# Development Guidelines

This document defines coding standards and development practices for the project.

---

## Code Structure

The backend must follow clean architecture principles.

Main folders:

- API
- Application
- Domain
- Infrastructure

Responsibilities:

API  
Handles HTTP requests and responses.

Application  
Contains business logic and use cases.

Domain  
Contains entities and domain rules.

Infrastructure  
Handles database, file storage, and integrations.

---

## Naming Conventions

Classes:
PascalCase

Methods:
PascalCase

Variables:
camelCase

Database tables:
snake_case

Examples:

UserService  
TaskRepository  
createTask()

---

## Error Handling

All API endpoints must return structured error responses.

Example format:

{
  "error": "Invalid request",
  "code": 400,
  "message": "Missing required field"
}

All exceptions must be logged.

---

## Logging

Logging should be implemented using a centralized logging system.

Log levels:

- Debug
- Information
- Warning
- Error

Sensitive data must never be logged.

---

## Testing

Unit tests must cover:

- services
- business logic
- validation

Integration tests should verify:

- database interactions
- API endpoints

Coverage target: 70%.