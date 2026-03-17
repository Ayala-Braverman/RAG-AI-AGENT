# System Specification

## Overview
The project is a task management platform designed for teachers and students.

The goal of the system is to allow teachers to create tasks, track student progress, and manage classroom activities in a structured way.

Main capabilities:
- task creation
- classroom management
- progress tracking
- notifications

The system should scale to support thousands of students and teachers.

---

## System Architecture

The system follows a layered architecture.

Layers:
- API layer
- Application layer
- Domain layer
- Infrastructure layer

Each layer must remain independent.

Rules:
- API cannot access Infrastructure directly
- Domain must not depend on external services
- Infrastructure contains database and integrations

---

## Backend Technology

Backend stack:

- .NET Web API
- PostgreSQL
- Redis (for caching)

Reasons:

.NET Web API was selected because:
- strong typing
- good performance
- strong ecosystem

PostgreSQL was selected because:
- reliable relational database
- strong support for complex queries
- easy integration with .NET

Redis will be used for:
- caching frequently requested data
- storing temporary session data

---

## Database Design

Main tables:

users  
tasks  
classes  
task_submissions  

Relationships:

- a teacher can manage multiple classes
- a class can contain many students
- a task belongs to a class
- students submit tasks

Example fields:

users
- id
- email
- role
- created_at

tasks
- id
- title
- description
- due_date
- class_id

---

## UI Design

Primary color: blue

Secondary color: light gray

Accent color: orange

Design principles:
- minimal interface
- large readable text
- clear hierarchy

All Hebrew screens must support RTL layout.

---

## Supported Languages

Current supported languages:

- Hebrew
- English

Future languages under consideration:

- Spanish
- French

All UI text should be stored in translation files.

---

## Authentication

Authentication will be handled using JWT tokens.

Token lifetime:
- access token: 1 hour
- refresh token: 7 days

Security rules:

- passwords must be hashed using bcrypt
- login attempts must be rate limited
- sensitive endpoints require authentication