# Task 2 – Detecting Data Leaks Using SQL Injection

This project demonstrates a simple cloud-based system to **secure user data against SQL injection attacks**. It uses **AES-256 encryption** to protect sensitive information and a **capability code mechanism** to control access. The system implements **double-layer security** by combining encryption with safe SQL queries.

---

## Technologies Used

- **FastAPI** – lightweight Python framework for APIs  
- **Supabase (PostgreSQL)** – cloud database to store user data  
- **AES-256 Encryption** – secure storage of secrets  
- **Python-dotenv** – manage environment variables  

---

## Cloud Role

The database is hosted on **Supabase**, a cloud Postgres service. This makes the system:

- Accessible from anywhere via the internet  
- Secure, as the cloud handles storage and backups  
- Scalable, allowing multiple users to interact with the API  

FastAPI can run locally or be deployed on any cloud platform, connecting securely to the Supabase database. AES encryption ensures sensitive data is safe even in cloud storage, and parameterized SQL prevents injection attacks.

---

## Security Features

- **AES-256 encryption** – secrets are stored securely  
- **Parameterized SQL queries** – prevents SQL injection  
- **Capability code mechanism** – restricts access to SQL testing routes  

---

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
