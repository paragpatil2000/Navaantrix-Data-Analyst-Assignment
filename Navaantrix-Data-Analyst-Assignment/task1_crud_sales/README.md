# Task 1: CRUD Operations on Superstore Sales Dataset

This task demonstrates CRUD (Create, Read, Update, Delete) operations on the **SampleSuperstore.csv** dataset using Python and Pandas.  
A unique identifier column named **Record_ID** was added to support row-level operations.

---
## 📁 Folder Structure
task1_crud_sales/
│
├── SampleSuperstore.csv
├── crud.py
└── README.md


---

## 📌 Overview

- The dataset originally had **13 columns** and **9915 rows**.
- It did **not** have a unique key, so a new column **Record_ID** was created.
- CRUD operations are performed using **Pandas**, without any SQL database.
- All changes are directly saved back into the CSV file.

---

## 🛠 Technologies Used

- **Python 3**
- **Pandas library**

Install pandas:
pip install pandas


---

## ✨ Features Implemented

### ✔ 1. Create (Insert New Record)
- User enters new record fields.
- `Record_ID` is auto-generated.
- New data is appended to the CSV.

### ✔ 2. Read (Search Record)
- User enters `Record_ID`.
- Matching row is displayed.

### ✔ 3. Update (Modify Record)
- User enters `Record_ID`.
- Allowed to update:
  - Sales  
  - Quantity  
- Blank input means "no change".

### ✔ 4. Delete (Remove Record)
- User enters `Record_ID`.
- The record is removed from the dataset.

---

## ▶️ Running the Program

Open terminal inside the folder:
 python crud.py
 
You will see:

===== CRUD MENU =====

1.Create Record
2.Read Record
3.Update Record
4.Delete Record
5.Exit


Enter choice: 1
Enter new record details:
Ship Mode: Standard Class
Segment: Consumer
Country: India
City: Pune
State: Maharashtra
Postal Code: 410057
Region: South
Category: Technology
Sub-Category: Phones
Sales: 1000
Quantity: 2
Discount: 0.1
Profit: 200

File saved successfully!

Enter choice: 2
Enter Record_ID to search: 1

Ship Mode   Segment        Country       City     State  ...   Sales Quantity Discount   Profit  Record_ID
0  Second Class  Consumer  United States  Henderson  Kentucky  ...  261.96        2      0.0  41.9136          1    


Enter choice: 3
Enter Record_ID to update: 3

New Sales: 999
New Quantity: 10

File saved successfully!

Enter choice: 4
Enter Record_ID to delete: 2

File saved successfully!
Record deleted.



---

## ⚙️ How It Works (In Simple Terms)

1. **load_data()** → reads CSV  
2. **save_data(df)** → saves updates to CSV  
3. **create_record()** → adds new row  
4. **read_record()** → searches by Record_ID  
5. **update_record()** → modifies sales/quantity  
6. **delete_record()** → removes row  
7. **menu()** → handles user input

---

##  Challenges Faced

- Dataset had **no unique ID** → solved by adding `Record_ID`.
- Updating CSV without corrupting index required careful saving.
- User-input error handling added while updating numeric fields.

