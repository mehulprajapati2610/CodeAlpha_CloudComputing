# SQL Injection Protection and Data Leak Prevention

This project demonstrates how to secure a cloud-based application from SQL injection attacks using encryption and prepared statements.

## Key Features

* AES-256 encryption for password storage
* SQL injection protection using parameterized queries
* Capability code for restricted admin access
* Demonstration of unsafe vs safe login attempts
* Works with cloud-hosted SQL database

## Technologies Used

* Node.js or PHP
* MySQL
* Crypto (AES-256)
* Railway or Render (optional)

## How the System Works

1. User credentials are encrypted before being stored
2. Login queries use prepared statements to block injections
3. SQL injection attempts are logged/blocked
4. Admin operations require a special capability code

## Running the Project

```
npm install
node server.js
```

Configure database credentials and encryption keys in `.env`.

## Output

* Password saved in encrypted form
* SQL injection attempt rejected
* Admin route works only with capability code
