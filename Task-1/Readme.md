# Data Redundancy Removal System

This project focuses on detecting and preventing duplicate entries in a cloud database. Incoming data is checked against existing records, and only unique entries are stored.

## Key Features

* Detects and blocks duplicate data
* Ensures only unique information is saved
* Cloud-based database support
* Simple REST API for inserting and verifying entries

## Technologies Used

* Node.js
* Express.js
* MongoDB Atlas
* Mongoose
* Postman

## How It Works

1. User submits data such as email, text, or ID
2. System checks if a matching entry already exists
3. Duplicate entries are rejected
4. Unique entries are stored successfully

## Running the Project

```
npm install
node index.js
```

Add your MongoDB connection string in a `.env` file.

## API Example

POST /add
Sample request:

```json
{
  "email": "user@example.com",
  "data": "sample entry"
}
```

## Output

* “Data added successfully” (unique entry)
* “Data already exists” (duplicate found)
