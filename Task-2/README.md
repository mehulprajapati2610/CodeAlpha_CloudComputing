# Task 2 – Detecting Data Leaks Using SQL Injection

This project is a **cloud-based system** designed to secure user data against SQL injection attacks. It demonstrates a **complete workflow** using FastAPI, AES-256 encryption, and a cloud-hosted database. The system implements **double-layer security** by combining encryption with parameterized SQL queries and a **capability code mechanism** to control access.

---

## What This Project Does

- Stores user credentials and sensitive information **securely using AES-256 encryption**  
- Protects against **SQL injection attacks** using parameterized queries  
- Restricts access to SQL testing routes using a **capability code**  
- Combines multiple security layers for **data leak prevention**  

---

## Technologies Used

- **FastAPI** – Python framework for building APIs  
- **Supabase (PostgreSQL)** – cloud-hosted database storing encrypted data  
- **AES-256 Encryption** – secures sensitive information  
- **Python-dotenv** – loads environment variables  
- **psycopg2** – connects Python to PostgreSQL  

---

## How the Cloud is Involved

- **Database hosting**: Supabase hosts the Postgres database in the cloud  
- **Accessibility**: Makes the system reachable from anywhere over the internet  
- **Security & backup**: Supabase ensures data is stored safely and backed up  
- **Scalability**: Supports multiple users accessing the API simultaneously  

FastAPI runs locally or on a cloud platform, connecting securely to the Supabase database. This setup demonstrates how cloud services integrate into a secure system to manage and protect user data.

---

## How the Cloud Performs Its Role

1. **Stores encrypted data** from the application securely  
2. **Handles requests** from the API without exposing sensitive data  
3. **Provides network access** so users and developers can interact with the system remotely  
4. **Maintains reliability and backups**, ensuring the database is safe even in case of local failures  

---

## How to Use

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create your `.env` file:
    - Copy `.env.example` and rename it to `.env`
    - Fill in your credentials

3. Initialize the database:
    ```bash
    python db_init.py
    ```

4. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

5. Open Swagger UI:
    ```
    http://127.0.0.1:8000/docs
    ```

6. Test endpoints:
    - `/user/` → add users with AES-encrypted secrets
    - `/sql-test/` → test capability code access for SQL
