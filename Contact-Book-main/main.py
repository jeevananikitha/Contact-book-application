
from tkinter.ttk import *
from tkinter import *
from databases import *
from add_contact import *

'''
ContactBook Class
- Accesses a contact book database and provides a user interface for the user to control
'''
class ContactBook(Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("750x500")
        self.resizable(False, False)
        self.configure(background = "#303030")
        self.draw_widgets()

        self.selected_contact = None

        self.db_helper = DatabaseHelper("database/database.db")
        self.load_from_database()

    '''
    Loads data from the database and inserts it to the table
    '''
    def load_from_database(self):
        self.contacts = self.db_helper.get_all_contacts()
        self.table.delete(*self.table.get_children())
        idx = 0

        for contact in self.contacts:
            self.table.insert(
                parent = "",
                index = idx,
                iid = idx, 
                text = "", 
                values = (contact.name, contact.email, contact.phone_number)
            )
            idx += 1

    '''
    Runs when the table is left-clicked
    '''
    def table_left_click(self,  event: Event):
        row_id = self.table.identify("item", event.x, event.y)

        try:
            self.selected_contact = self.contacts[int(row_id)]
        except:
            pass

    '''
    Runs when the Add Contact button is pressed
    '''
    def add_contact_pressed(self):
        def contact_added(contact: Contact):
            self.db_helper.insert_contact(contact)
            self.load_from_database()

        add_contact = AddContact()
        add_contact.set_completion_callback(contact_added)

    '''
    Runs when the Delete Contact button is pressed
    '''
    def delete_contact_pressed(self):
        if self.selected_contact:
            self.db_helper.delete_contact(self.selected_contact)
            self.load_from_database()
        else:
            messagebox.showwarning("Nothing Selected", "No contact has been selected for deletion")

    '''
    Draws the widgets to the window
    '''
    def draw_widgets(self):
        # Table

        self.table = Treeview(self)
        self.table["columns"] = ("Name", "Email", "Phone Number")

        self.table.column("#0", width = 0, stretch = NO)
        self.table.column("Name", anchor = CENTER, width = 80)
        self.table.column("Email", anchor = CENTER, width = 80)
        self.table.column("Phone Number", anchor = CENTER, width = 80)

        self.table.heading("#0", text = "", anchor = CENTER)
        self.table.heading("Name", text = "Name", anchor = CENTER)
        self.table.heading("Email", text = "Email", anchor = CENTER)
        self.table.heading("Phone Number", text = "Phone Number", anchor = CENTER)

        self.table.bind("<Button-1>", self.table_left_click)
        self.table.place(x = 10, y = 10, width = 625, height = 475)

        # Buttons

        self.add_contact = Button(self, text = "Add Contact")
        self.add_contact.configure(command = self.add_contact_pressed)
        self.add_contact.place(x = 650, y = 10, height = 50, width = 90)

        self.delete_contact = Button(self, text = "Delete Contact")
        self.delete_contact.configure(command = self.delete_contact_pressed)
        self.delete_contact.place(x = 650, y = 75, height = 50, width = 90)


if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
