# Stage 3

# Query Optimization

## Common Queries

Retrieve unread notifications:

```sql
SELECT *
FROM User_Notifications
WHERE user_id = ?
AND is_read = FALSE;
```

Retrieve notifications by category:

```sql
SELECT *
FROM Notifications
WHERE category = 'Placement';
```

## Indexes

- INDEX(user_id)
- INDEX(is_read)
- INDEX(category)
- INDEX(created_at)

## Optimization Techniques

- Pagination using LIMIT and OFFSET.
- Composite indexes for frequently used filters.
- Avoid SELECT * when unnecessary.
- Cache frequently accessed notifications.