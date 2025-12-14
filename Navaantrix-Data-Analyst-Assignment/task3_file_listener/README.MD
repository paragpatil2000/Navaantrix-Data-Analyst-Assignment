# Task 3: File Listener and Database Upload

# Task 3: File Listener and Database Upload

This module continuously monitors a folder for newly added CSV files.  
Whenever a new CSV file is detected, the script automatically reads the file and uploads its content into an SQLite database.  
Each CSV file is stored in a separate table (auto-created), ensuring there are no column conflicts.


## 📁 Folder Structure

task3_file_listener/  
│  
├── listener.py  
├── database.db  
└── data/               ← Drop/upload CSV files here  

---

## 🎯 Objective

- Monitor a folder continuously
- Detect new CSV files automatically  
- Read the file and upload its content into a database  
- Create a new table for each file without column conflicts  
- Provide proper logs and error handling  
- Ensure the script runs continuously  


## 🛠 Technologies Used

- **Python 3**
- **Watchdog** (for folder monitoring)
- **Pandas** (for CSV reading)
- **SQLite** (lightweight database, no setup required)

Install dependencies:
pip install watchdog pandas

.▶️ How to Run the Program
Step 1 — Navigate to folder
     cd task3_file_listener

Step 2 — Start the listener
     python listener.py


You will see:

📌 File Listener Started!
📂 Monitoring folder: data
⏳ Waiting for new CSV files...

Step 3 — Upload CSV files
 Copy any .csv file into the data folder:
    task3_file_listener/data/your_file.csv


The program automatically detects it:

[DETECTED] New file → data\your_file.csv
[INFO] Reading file: data\your_file.csv
[SUCCESS] Uploaded into table → uploaded_your_file


🗄 Database Output

A new SQLite file is created:
    database.db

Inside this, a dedicated table is created for each CSV file:

Example:
CSV File	    Database Table Name
creditcard.csv	uploaded_creditcard
Train.csv	    uploaded_train
Sales2024.csv	uploaded_sales2024

This ensures:
No conflicts
Different schemas supported
Any dataset accepted

🔧 How It Works (Behind the Scenes)
1. watchdog
   Listens for new files in the data/ folder.

2. pandas
   Reads the CSV into a DataFrame.

3. Auto Table Creation
   Table name is generated based on filename:
   uploaded_<filename>

4. Database Upload
 Data is inserted using:
   df.to_sql(table_name, conn, if_exists="replace", index=False)

5. Continuous Monitoring
Runs a loop until the user presses CTRL + C.

