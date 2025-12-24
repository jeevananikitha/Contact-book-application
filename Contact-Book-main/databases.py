
from objects import *
from sqlite3 import *

'''
Wrapper function for functions which modify the database
- Handles opening and closing the database
- Passes the cursor to the function
'''
def database_operation(function):
    def wrapper(self, *args):
        conn = connect(self.filepath)
        cursor = conn.cursor()

        result = function(self, cursor, *args)
        conn.commit()
        conn.close()

        return result

    return wrapper

'''
DatabaseHelper Class
- Provides functions which access a database 
'''
class DatabaseHelper:
    def __init__(self, filepath: str):
        self.filepath = filepath

    '''
    Create the tables necessery for the database
    '''
    @database_operation
    def create_tables(self, cursor: Cursor):
        command = """
CREATE TABLE IF NOT EXISTS ContactTbl (
    UserID          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name            TEXT,
    Email           TEXT,
    PhoneNumber     TEXT
)
                  """

        cursor.execute(command)

    '''
    Insert a contact to the database
    '''
    @database_operation
    def insert_contact(self, cursor: Cursor, contact: Contact):
        command = """
INSERT INTO ContactTbl
VALUES (?, ?, ?, ?)
                  """

        cursor.execute(command, (None, contact.name, contact.email, contact.phone_number))
        
    '''
    Delete a contact from the database
    '''
    @database_operation
    def delete_contact(self, cursor: Cursor, contact: Contact):
        command = """
DELETE FROM ContactTbl WHERE UserID = ?
                  """

        cursor.execute(command, (contact.id,))

    '''
    Read all of the contacts in the database into a list
    '''
    @database_operation
    def get_all_contacts(self, cursor: Cursor):
        command = """
SELECT * FROM ContactTbl
                  """

        cursor.execute(command)     
        rows = cursor.fetchall()
        contacts = []

        for row in rows:
            contact = Contact(row[0], row[1], row[2], row[3])
            contacts.append(contact)

        return contacts
