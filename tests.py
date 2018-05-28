import unittest
from Book import *
import time
import os
import random
import string


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_checkBirthdayDate1(self):
        self.assertEqual(book.checkBirthday("23.12"), True)

    def test_checkBirthdayDate2(self):
        self.assertEqual(book.checkBirthday("5.6"), True)

    def test_checkBirthdayDate3(self):
        self.assertEqual(book.checkBirthday("05.06"), True)

    def test_checkBirthdayDate4(self):
        self.assertEqual(book.checkBirthday(""), False)

    def test_checkBirthdayDate5(self):
        self.assertEqual(book.checkBirthday("tanya"), False)

    def test_checkBirthdayDate6(self):
        self.assertEqual(book.checkBirthday("0506"), False)

    def test_checkName1(self):
        randName="".join([random.choice(string.ascii_letters) for n in range(7)])
        self.assertEqual(book.checkName(randName), True)

    def test_checkName2(self):
        self.assertEqual(book.checkName("1111"), False)

    def test_checkName3(self):
        self.assertEqual(book.checkName(""), False)

    def test_checkName4(self):
        self.assertEqual(book.checkName("Таня"), False)

    def test_checkName5(self):
        self.assertEqual(book.checkName("Tanya1"), False)

    def test_checkName6(self):
        randName="".join([random.choice(string.ascii_letters) for n in range(4)])
        self.assertEqual(book.checkName("Tanya, School"+randName), True)

    def test_checkName7(self):
        book.saveContact("Tanya", "892143837", "12.12")
        self.assertEqual(book.checkName("Tanya"), False)

    def test_checkPhone1(self):
        self.assertEqual(book.checkPhone("89214383799"), True)

    def test_checkPhone2(self):
        self.assertEqual(book.checkPhone("+79214383799"), True)

    def test_checkPhone3(self):
        self.assertEqual(book.checkPhone("8(921)4383799"), True)

    def test_checkPhone4(self):
        self.assertEqual(book.checkPhone("+7(921)4383799"), True)

    def test_checkPhone5(self):
        self.assertEqual(book.checkPhone("8921d"), False)

    def test_checkPhone6(self):
        self.assertEqual(book.checkPhone("3717459"), True)

    def test_checkPhone7(self):
        self.assertEqual(book.checkPhone(""), False)

    def test_checkPhone8(self):
        self.assertEqual(book.checkPhone("w"), False)

    def test_saveContact(self):
        contactFile = open(".contacts.csv", "a+")
        contacts = contactFile.read()
        countRow=contacts.count("\n")
        book.saveContact("Tanya", "892143837", "12.12")
        contactFile.seek(0)
        contactsNew=contactFile.read()
        countRowNew=contactsNew.count("\n")
        difference=int(countRowNew)-int(countRow)
        self.assertEqual(difference, 1)
        contactFile.close()

    def test_seeAll(self):
        contactFile = open(".contacts.csv", "a+")
        contacts = contactFile.read()
        book.seeAll()
        self.assertEqual(book.labelMain.cget("text"), contacts.replace(";", "\t \t|\t ").replace(" ", ""))
        contactFile.close()

    def test_reminder(self):
        book.reminder()
        try:
            realNames = book.labelBirthday.cget("text").replace("Today is a birthday of ", "")
            listNames=realNames.split("', '")
            contactFile = open(".contacts.csv", "a+")
            contacts = contactFile.read()
            contactsSplit=contacts.split(';')
        except:
            return
        
        i=0
        now = datetime.datetime.now()
        birthday=""
        today=str(now.day)+"."+str(now.month)
        try:
            while  i<len(contactsSplit)-1:
                if contactsSplit[i].replace("\n", "")==listNames[0]:
                      birthday=contactsSplit[i+2]
                i=i+3
        except:
            pass
        
        self.assertEqual(birthday, today)
        
  
book=Book()
if __name__ == '__main__':
    unittest.main()
