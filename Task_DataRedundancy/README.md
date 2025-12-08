# Task 1: Data Redundancy Removal System ☁️

## Overview

This project prevents **duplicate data** from being stored in a **cloud database (MongoDB Atlas)**.
It reads entries from a CSV file and inserts only **unique records**.

---

## How to Run

1. Install dependencies:

```bash
pip install pymongo python-dotenv
```

2. Create a `.env` file with your MongoDB credentials:

```
MONGO_USER=yourUsername
MONGO_PASSWORD=yourPassword
MONGO_CLUSTER=cluster0.abcde.mongodb.net
DATABASE_NAME=RedundancyDB
```

3. Make sure `.env` is in `.gitignore`.
4. Run the script:

```bash
python main.py
```

* Adds only unique entries from `sample_data.csv`
* Skips duplicates automatically

---

## Cloud Computing Role

* **Centralized Storage:** Data is stored in the cloud and accessible from anywhere.
* **Data Reliability:** Automatic backups ensure data is safe.
* **Scalability:** Handles large datasets or multiple users without slowing down.
* **Collaboration:** Multiple users/scripts can access the same database simultaneously.
* **Real-Time Validation:** Duplicate checks happen instantly before insertion.

---

## Files

* `main.py` – Reads CSV & inserts data
* `database.py` – Connects to MongoDB and checks duplicates
* `sample_data.csv` – Example data
* `.env` – Local credentials (ignored by Git)
* `README.md` – Project description
