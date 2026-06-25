# Stage 2

# Database Design for Campus Notifications Microservice

## Overview

The Campus Notifications Microservice stores notification details, user information, and notification delivery status. The database is normalized to reduce redundancy while providing efficient retrieval and update operations.

## Database Tables

### Users

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| user_id | UUID | Primary Key | Unique user identifier |
| full_name | VARCHAR(100) | NOT NULL | User name |
| email | VARCHAR(100) | UNIQUE | User email |
| role | VARCHAR(20) | NOT NULL | Student, Faculty, Admin |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation time |

### Notifications

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| notification_id | UUID | Primary Key | Notification ID |
| title | VARCHAR(150) | NOT NULL | Notification title |
| message | TEXT | NOT NULL | Notification content |
| category | VARCHAR(30) | NOT NULL | Placement, Event, Result |
| priority | VARCHAR(20) | NOT NULL | Low, Medium, High |
| created_by | UUID | Foreign Key | User who created notification |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Creation time |

### User_Notifications

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | Primary Key | Record ID |
| user_id | UUID | Foreign Key | User reference |
| notification_id | UUID | Foreign Key | Notification reference |
| is_read | BOOLEAN | DEFAULT FALSE | Read status |
| read_at | TIMESTAMP | NULL | Read timestamp |

## Relationships

- One User can create many Notifications.
- One Notification can be delivered to many Users.
- User_Notifications maintains delivery and read status.

## Indexes

- Index on email
- Index on category
- Index on created_at
- Composite Index on (user_id, is_read)

## Database Choice

PostgreSQL is chosen because it supports ACID transactions, indexing, scalability, JSON support, and strong concurrency handling.