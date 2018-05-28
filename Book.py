from Tkinter import *
import datetime
import time
import re

class Book(object):

    def __init__(self):
        pass

    def checkName(self, string):
        match = re.match("""^[a-zA-Z., ]+$""", string)
        if match:
            contactFile = open(".contacts.csv", "a+")
            contacts = contactFile.read()
            contactsSplit=contacts.split(';')
            i=0
            name="\n"+string
            while i<len(contactsSplit):
                if contactsSplit[i]==name:
                   return False
                i=i+3
            contactFile.close()
        return bool(match)

    def checkPhone(self, string):
        match = re.match("""^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$""", string)
        return bool(match)

    def checkBirthday(self, string):
        match = re.match("""^(0?[1-9]|([12][0-9]|3[01]))\.(0?[1-9]|1[012])$""", string)
        return bool(match)

    def reminder(self):
        contactFile = open(".contacts.csv", "a+")
        contacts = contactFile.read()
        contactsSplit=contacts.split(';')
        i=2
        k=0
        listName=[]
        now = datetime.datetime.now()
        today=str(now.day)+"."+str(now.month)
        while not i>len(contactsSplit):
            if contactsSplit[i]==today:
                k=k+1
                listName.append(contactsSplit[i-2].replace("\n", "").replace("'", ""))
            i=i+3
        text1=str(listName).strip("'[\n]'")
        fullText="Today is a birthday of " + text1
        if not k==0:
            self.labelBirthday=Label(text=str(fullText), font=("Courier", 9))
            self.labelBirthday.place(x=140, y=90)
        contactFile.close()

    
    def seeAll(self):
        try: 
            self.buttonSave.destroy()
            self.labelName.destroy()
            self.labelPhone.destroy()
            self.labelDay.destroy()
            self.entryName.destroy()
            self.entryPhone.destroy()
            self.entryDay.destroy()
        except:
            pass
        try:
            self.labelSuccess.destroy()
        except:
            pass
        try:
            self.labelError.destroy()
        except:
            pass
        try:
            self.labelBirthday.destroy()
        except:
            pass
        contactsFile = open(".contacts.csv", "a+")
        self.labelHead = Label(text="Name \t \t|\t  Phone \t \t\t|\t  Birthday \n _")
        self.labelHead.place(x=10, y=35)
        self.labelMain = Label("")
        self.labelMain.place(x=10, y=65)
        contacts = contactsFile.read()
        allNames=""
        self.labelMain.config(text=contacts.replace(";", "\t \t|\t ").replace(" ", ""))
        contactsFile.close()

    def saveContact(self, name, phone, birtdayForm):
        contactsFile = open(".contacts.csv", "a+")
        contactsFile.write(name+";"+phone+";"+birtdayForm+";"+"\n")
        contactsFile.close()

    
    def addContact(self):
        try:
            self.labelBirthday.destroy()
        except:
            pass
        try:
            self.labelHead.destroy()
            self.labelMain.destroy()
        except:
            pass
        try:
            self.labelSuccess.destroy()
            self.labelError.destroy()
        except:
            pass
        self.labelName = Label(text="Name: ")
        self.labelName.place(x=100, y=35)
        self.entryName = Entry()
        self.entryName.place(x=200, y=35)
        self.labelPhone = Label(text="Phone: ")
        self.labelPhone.place(x=100, y=65)
        self.entryPhone = Entry( )
        self.entryPhone.place(x=200, y=65)
        self.labelDay = Label(text="Birthday(dd.mm):  ")
        self.labelDay.place(x=100, y=95)
        self.entryDay = Entry()
        self.entryDay.place(x=200, y=95)
        def callback():
            self.labelError = Label(text="", fg="red")
            self.labelError.place(x=180, y=135)
            self.labelSuccess = Label(text="", fg="blue")
            self.labelSuccess.place(x=180, y=220)
            name = self.entryName.get()
            phone = self.entryPhone.get()
            birthday = self.entryDay.get()
            if not self.checkName(name):
                self.labelError.config(text="Incorrect name")
                return
            if not self.checkPhone(phone):
                self.labelError.config(text="Incorrect phone ")
                return
            if not self.checkBirthday(birthday):
                self.labelError.config(text="Incorrect date ")
                return
            birtdayForm=birthday
            try:
                if  birthday[3]=="0":
                    birtdayForm=birthday.replace(birthday[3], "")
                elif birthday[2]=="0":
                    birtdayForm=birthday.replace(birthday[2], "")
                elif birthday[0]=="0":
                    birtdayForm=birthday.replace(birthday[0], "")
            except:
                pass
            self.saveContact(name, phone, birtdayForm)
            self.labelError.destroy()
            self.labelSuccess.config(text="Contact was saved")
        
        self.buttonSave=Button( text="Save contact", command=callback )
        self.buttonSave.place(x=180, y=165) 






    
