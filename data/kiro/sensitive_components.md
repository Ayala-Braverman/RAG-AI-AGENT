# Sensitive Components

This document lists system areas that require special attention.

Changes to these components must be reviewed carefully.

---

## Authentication Module

The authentication system handles login, token generation, and session validation.

Main components:

- login endpoint
- JWT validation middleware
- refresh token system

Warning:

Do not modify the JWT validation middleware without full testing.

Changes here can break authentication for the entire system.

---

## Database Schema

Schema migrations must be reviewed before deployment.

Risk areas:

- tasks table
- users table

Dropping columns may cause data loss.

Migration scripts must be tested on staging before production.

---

## Background Notification Job

A background job sends notifications to users.

Schedule:

Every 5 minutes.

Risks:

- incorrect scheduling may cause duplicate notifications
- long-running jobs may overload the system

---

## File Storage System

User uploads are stored in cloud storage.

Rules:

- files must be scanned before upload
- file size limit: 10MB
- only allowed formats should be accepted

---

## Rate Limiting

API endpoints must include rate limiting.

Purpose:

- prevent abuse
- protect authentication endpoints

Default limit:

100 requests per minute per user.