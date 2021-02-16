import pandas as pd
from openpyxl import Workbook


class Contact:

    # Constructor
    def __init__(self, name, surname, email, phone, birthday, city):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone
        self.__birthday = birthday
        self.__city = city
    
    # Getters and Setters
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value):
        self.__surname = value
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    @property
    def birthday(self):
        return self.__birthday
    @birthday.setter
    def birthday(self, value):
        self.__birthday = value
    
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, value):
        self.__city = value

    # Dictionary
    def dicc(self):
        return {
            "name": self.__name,
            "surname": self.__surname,
            "email": self.__email,
            "phone": self.__phone,
            "birthday": self.__birthday,
            "city": self.__city
        }

def print_contacts(contact_list):
    
    for contact in contact_list:
        print("-" * 30)
        print(f'Name: {contact.get_name()}')
        print(f'Surname: {contact.get_surname()}')
        print(f'Email: {contact.get_email()}')
        print(f'Phone: {contact.get_phone()}')
        print(f'Birthday: {contact.get_birthday()}')
        print(f'City: {contact.get_city()}')

""" 
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
"""

def create_dataframe(dicc_list):
    df = pd.DataFrame(dicc_list)
    return df

def save_excel(dataframe):
    dataframe.to_excel(
        'contacts/contacts_excel.xlsx',
        sheet_name='Contacts',
        index=False)
    # dataframe.to_csv('contacts/contacts_excel.xlsx', sep=',', index=False, columns=True)