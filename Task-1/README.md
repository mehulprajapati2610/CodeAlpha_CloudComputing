# Task 1: Data Redundancy Removal System

## Overview

Prevents duplicate data in **MongoDB Atlas** by reading from a CSV and storing only **unique entries**.

## Features

* Detects duplicates by email
* Imports data from CSV
* Stores only unique records in cloud

## Tech

* Python 3.13
* MongoDB Atlas
* `pymongo` library

## Setup & Run

1. Install dependencies:

```bash
pip install pymongo
```

2. Create MongoDB Atlas cluster & database (`RedundancyDB`) with collection `entries`.
3. Add a database user and allow your IP.
4. Update `database.py` with connection string.
5. Prepare `sample_data.csv` with data.
6. Run:

```bash
python main.py
```

## How It Works

CSV → Python → MongoDB

* Adds unique entries
* Skips duplicates

## Cloud Benefits

* Accessible anywhere
* Scalable & reliable
