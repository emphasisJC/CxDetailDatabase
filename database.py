from tkinter import *
import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Create the main window
root = Tk()
root.title('emphasisJC Customer Database')
root.geometry("800x800")

# Create text boxes
cxID = Entry(root, width=30)
cxID.grid(row=0, column=0, padx=20)
f_name = Entry(root, width=30)
f_name.grid(row=1, column=0, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=2, column=0, padx=20)
phone = Entry(root, width=30)
phone.grid(row=3, column=0, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=0, padx=20)
dob = Entry(root, width=30)
dob.grid(row=5, column=0, padx=20)
address = Entry(root, width=30)
address.grid(row=6, column=0, padx=20)
city = Entry(root, width=30)
city.grid(row=7, column=0, padx=20)
postcode = Entry(root, width=30)
postcode.grid(row=8, column=0, padx=20)

# Create text box labels 
cxID_label = Label(root, text="Customer ID")
cxID_label.grid(row=0, column=1)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=1)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=1)

phone_label = Label(root, text="Phone Number")
phone_label.grid(row=3, column=1)

email_label = Label(root, text="Email Address")
email_label.grid(row=4, column=1)

dob_label = Label(root, text="DD/MM/YYY")
dob_label.grid(row=5, column=1)

address_label = Label(root, text="Street Address")
address_label.grid(row=6, column=1)

city_label = Label(root, text="City/Suburb")
city_label.grid(row=7, column=1)

postcode_label = Label(root, text="Postcode")
postcode_label.grid(row=8, column=1)

# Create submit function
def submit():

# Defined submit button
    submit_button = Button(root, text="Submit", command=submit)
    submit_button.grid(row=9, column=0, padx=20, pady=10, columnspan=2)

# Clear text boxes
cxID.delete(0, END)
f_name.delete(0, END)
l_name.delete(0, END)
phone.delete(0, END)
email.delete(0, END)   
dob.delete(0, END)    
address.delete(0, END)    
city.delete(0, END)  
postcode.delete(0, END)  
print ('Data Submitted Successfully!')

    # Insert into table
cur.execute("""
        INSERT INTO customers (cxID, first_name, last_name, phone, email, dob, address, city, postcode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        cxID.get(),
        f_name.get(),
        l_name.get(),
        phone.get(),
        email.get(),
        dob.get(),
        address.get(),
        city.get(),
        postcode.get()
    ))

    # Commit changes
conn.commit()

#Create query function
def query():

    # Create a database or connect to one
    conn = sqlite3.connect('database.db')

    # Create cursor
    c = conn.cursor()

    #Query the database 
    c.execute("SELECT *, oid FROM customers")
    records = c.fetchall()

    #Format results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records) 
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create table 
create_table_query = '''
CREATE TABLE IF NOT EXISTS customers (
           cxID INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name TEXT NOT NULL, 
           last_name TEXT NOT NULL, 
           phone INTEGER, 
           email TEXT,
           dob TEXT,
           address TEXT NOT NULL,
           city TEXT NOT NULL, 
           postcode INTEGER
           );
               '''

# Execute sql query to create table 
cur.execute(create_table_query)

root.mainloop()