# Technical Decisions Log

This document tracks important technical decisions made during the project.

---

## Decision 001 – Database Choice

Chosen database: PostgreSQL

Alternatives considered:

- MySQL
- MongoDB

Reasons for choosing PostgreSQL:

- strong relational capabilities
- mature ecosystem
- good performance with joins
- strong community support

Date: 2026-01-12

---

## Decision 002 – Backend Framework

Chosen framework: .NET Web API

Alternatives considered:

- Node.js + Express
- Django

Reasons:

- team familiarity with C#
- strong type safety
- good tooling in Visual Studio

Date: 2026-01-15

---

## Decision 003 – Hosting Platform

Chosen platform: AWS

Main services:

- EC2
- RDS
- S3

Reasons:

- scalability
- mature cloud ecosystem
- integration with monitoring tools

Date: 2026-01-20

---

## Decision 004 – Background Jobs

Background jobs will be implemented using Hangfire.

Main use cases:

- sending notifications
- cleaning expired sessions
- scheduled reports

Date: 2026-01-28

---

## Decision 005 – Caching Strategy

Redis will be used for caching.

Data to cache:

- user profiles
- class lists
- frequently requested tasks

Cache expiration time: 5 minutes.

Date: 2026-02-02