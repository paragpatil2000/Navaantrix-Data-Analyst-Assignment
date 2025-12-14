import pandas as pd

FILE = "SampleSuperstore.csv"

# Load CSV file
def load_data():
    return pd.read_csv(FILE)

# Save updated CSV
def save_data(df):
    df.to_csv(FILE, index=False)
    print("\nFile saved successfully!\n")

# CREATE
def create_record():
    df = load_data()

    print("\nEnter new record details:")
    ship = input("Ship Mode: ")
    segment = input("Segment: ")
    country = input("Country: ")
    city = input("City: ")
    state = input("State: ")
    postal = input("Postal Code: ")
    region = input("Region: ")
    category = input("Category: ")
    subcat = input("Sub-Category: ")
    sales = float(input("Sales: "))
    quantity = int(input("Quantity: "))
    discount = float(input("Discount: "))
    profit = float(input("Profit: "))

    new_id = df["Record_ID"].max() + 1

    new_row = {
        "Ship Mode": ship,
        "Segment": segment,
        "Country": country,
        "City": city,
        "State": state,
        "Postal Code": postal,
        "Region": region,
        "Category": category,
        "Sub-Category": subcat,
        "Sales": sales,
        "Quantity": quantity,
        "Discount": discount,
        "Profit": profit,
        "Record_ID": new_id
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)

# READ
def read_record():
    df = load_data()
    rid = int(input("Enter Record_ID to search: "))

    result = df[df["Record_ID"] == rid]

    if result.empty:
        print("Record not found!\n")
    else:
        print("\n", result)

# UPDATE
def update_record():
    df = load_data()
    rid = int(input("Enter Record_ID to update: "))

    idx = df[df["Record_ID"] == rid].index

    if len(idx) == 0:
        print("Record not found!\n")
        return

    print("\nLeave blank if you do not want to change value.")
    new_sales = input("New Sales: ")
    new_qty = input("New Quantity: ")

    if new_sales:
        df.loc[idx, "Sales"] = float(new_sales)
    if new_qty:
        df.loc[idx, "Quantity"] = int(new_qty)

    save_data(df)

# DELETE
def delete_record():
    df = load_data()
    rid = int(input("Enter Record_ID to delete: "))

    new_df = df[df["Record_ID"] != rid]

    if len(new_df) == len(df):
        print("Record not found!\n")
    else:
        save_data(new_df)
        print("Record deleted.\n")

# MENU
def menu():
    while True:
        print("\n===== CRUD MENU =====")
        print("1. Create Record")
        print("2. Read Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        c = input("Enter choice: ")

        if c == "1":
            create_record()
        elif c == "2":
            read_record()
        elif c == "3":
            update_record()
        elif c == "4":
            delete_record()
        elif c == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()
