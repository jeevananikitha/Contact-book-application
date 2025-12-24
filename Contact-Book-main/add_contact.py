
from tkinter import messagebox
from tkinter import *
from typing import Callable
from input_validator import *
from objects import *
from global_vars import *

'''
AddContact Class
- Lets a user create a contact and return the contact to the caller
'''
class AddContact(Tk):
    def __init__(self):
        super().__init__()
        self.title("Add Contact")
        self.geometry("300x300")
        self.resizable(False, False)
        self.configure(background = "#303030")
        self.draw_widgets()

        self.callback = None

    '''
    Set the function which runs when the contact is created
    '''
    def set_completion_callback(self, function: Callable):
        self.callback = function

    '''
    Checks if the text entered in the phone number entry is valid
    - Only accepts digit characters (0-9)
    '''
    def phone_number_validate(self, data: str):
        return data.isdigit()

    '''
    Runs when the confirm button is pressed
    - Validate Input
    - If input is invalid show an error and return
    - If input is valid call the callback function and destroy this window
    '''
    def confirm_pressed(self):
        name = self.name_var.get()
        email = self.email_var.get()
        phone_number = self.phone_number_var.get()

        if not name:
            messagebox.showerror("Invalid Name", "Name cannot be empty")
            return

        if not email:
            messagebox.showerror("Invalid Email", "Email cannot be empty")
            return
        elif not InputValidator.validate_email(email):
            messagebox.showerror("Invalid Email", "Not a valid email address")
            return
        
        if not phone_number:
            messagebox.showerror("Invalid Phone Number", "Phone number cannot be empty")
            return
        elif not InputValidator.validate_phone_number(phone_number):
            messagebox.showerror("Invalid Phone Number", "Not a valid phone number")
            return

        if self.callback:
            contact = Contact(UNDEFINED_ID, name, email, phone_number)
            self.callback(contact)
            
        self.destroy()

    '''
    Draws the widgets to the window
    '''
    def draw_widgets(self):
        phone_number_reg = self.register(self.phone_number_validate)

        # Name

        self.name_var = StringVar(self)

        self.name_lbl = Label(self, text = "Name")
        self.name_lbl.configure(justify = CENTER)
        self.name_lbl.configure(font = UI_FONT)
        self.name_lbl.configure(foreground = "#ffffff", background = "#303030")
        self.name_lbl.place(x = 10, y = 10, width = 125, height = 50)

        self.name_entry = Entry(self, textvariable = self.name_var)
        self.name_entry.configure(font = UI_FONT)
        self.name_entry.place(x = 150, y = 10, width = 125, height = 50)

        # Email

        self.email_var = StringVar(self)

        self.email_lbl = Label(self, text = "Email")
        self.email_lbl.configure(justify = CENTER)
        self.email_lbl.configure(font = UI_FONT)
        self.email_lbl.configure(foreground = "#ffffff", background = "#303030")
        self.email_lbl.place(x = 10, y = 75, width = 125, height = 50)

        self.email_entry = Entry(self, textvariable = self.email_var)
        self.email_entry.configure(font = UI_FONT)
        self.email_entry.place(x = 150, y = 75, width = 125, height = 50)

        # Phone

        self.phone_number_var = StringVar(self)
        
        self.phone_number_lbl = Label(self, text = "Phone Number")
        self.phone_number_lbl.configure(justify = CENTER)
        self.phone_number_lbl.configure(font = UI_FONT)
        self.phone_number_lbl.configure(foreground = "#ffffff", background = "#303030")
        self.phone_number_lbl.place(x = 10, y = 140, width = 125, height = 50)

        self.phone_number_entry = Entry(self, textvariable = self.phone_number_var)
        self.phone_number_entry.configure(font = UI_FONT)
        self.phone_number_entry.configure(validate = "key", validatecommand = (phone_number_reg, "%P"))
        self.phone_number_entry.place(x = 150, y = 140, width = 125, height = 50)

        # Buttons

        self.cancel_btn = Button(self, text = "Cancel")
        self.cancel_btn.configure(font = UI_FONT)
        self.cancel_btn.configure(command = self.destroy)
        self.cancel_btn.place(x = 60, y = 245, width = 100, height = 35)

        self.confirm_btn = Button(self, text = "Confirm")
        self.confirm_btn.configure(font = UI_FONT)
        self.confirm_btn.configure(command = self.confirm_pressed)
        self.confirm_btn.place(x = 175, y = 245, width = 100, height = 35)
