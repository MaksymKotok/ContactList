contacts = []


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


def print_contacts():
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    i = 0
    print("№".ljust(4) + " | " + "Name".ljust(20) + " | Phone")
    for contact in contacts:
        print(str(i).ljust(4) + " | " + contact.name.ljust(20) + " | " + contact.phone)
        i += 1


def add_contact():
    while True:
        name = input("Type in contact's name:\n").strip()
        while True:
            phone = input("Type in contact's phone number:\n").strip()
            if not(phone.isdigit()) or len(phone) > 15:
                print("Invalid phone number. It must contain only digits and have length equal or less than 15!")
            else:
                is_duplicate = False
                for contact in contacts:
                    if contact.name == name:
                        print("There is already a contact with name " + name)
                        is_duplicate = True
                    if contact.phone == phone:
                        print("There is already a contact with phone number " + phone)
                        is_duplicate = True
                    if is_duplicate:
                        break
                if not is_duplicate:
                    contacts.append(Contact(name, phone))
                    print("Done!")
                    _command = input("Enter 1 to add one more contact. Enter something else to get back to main menu.\n")
                    if not(_command == "1"):
                        return
                    else:
                        break


def change_contact():
    if len(contacts) == 0:
        print("Contact list is empty! There is nothing to change!")
        return
    while True:
        contact_id = input("Enter number of contact, which you want to change (from 0 to "
                           + str(len(contacts) - 1) + ").\n")
        try:
            contact_id = int(contact_id)
            if contact_id < 0 or contact_id >= len(contacts):
                print("Number of contact is out of range. Try again")
            else:
                while True:
                    print("Contact:")
                    print(str(contact_id).ljust(4) + " | " + contacts[contact_id].name.ljust(20) + " | "
                          + contacts[contact_id].phone)
                    _command = input("Enter 1, if you want to change the contact's name.\n"
                                     "Enter 2, if you want to change the contact's phone.\n"
                                     "Enter 3, if you want to change both.\n"
                                     "Enter something else to return back to main menu.\n")
                    if _command == "1":
                        name = input("Type in contact name\n").strip()
                        contacts[contact_id].name = name
                        print("Done!")
                        return
                    elif _command == "2":
                        phone = input("Type in contact phone\n").strip()
                        if not (phone.isdigit()) or len(phone) > 15:
                            print("Invalid phone number. It must contain only digits and have length equal or less than 15!")
                            break
                        contacts[contact_id].phone = phone
                        print("Done!")
                        return
                    elif _command == "3":
                        name = input("Type in contact name\n").strip()
                        phone = input("Type in contact phone\n").strip()
                        if not (phone.isdigit()) or len(phone) > 15:
                            print("Invalid phone number. It must contain only digits and have length equal or less than 15!")
                            break
                        contacts[contact_id].name = name
                        contacts[contact_id].phone = phone
                        print("Done!")
                        return
                    else:
                        return
        except:
            print("Invalid value. Try again")


def delete_contact():
    if len(contacts) == 0:
        print("Contact list is empty! There is nothing to delete!")
        return
    while True:
        contact_id = input("Enter number of contact, which you want to change (from 0 to "
                           + str(len(contacts) - 1) + ").\n")
        try:
            contact_id = int(contact_id)
            if contact_id < 0 or contact_id >= len(contacts):
                print("Number of contact is out of range. Try again")
            else:
                print("Contact: ")
                print(str(contact_id).ljust(4) + " | " + contacts[contact_id].name.ljust(20) + " | "
                      + contacts[contact_id].phone)
                _command = input("Enter 1, if you want to delete this contact.\n"
                                 "Enter something else to return back to main menu.\n")
                if _command == "1":
                    contacts.pop(contact_id)
                    print("Done!")
                    return
                else:
                    return
        except:
            print("Invalid value. Try again")


def find_contact():
    if len(contacts) == 0:
        print("Contact list is empty! There is no place to search in!")
        return
    while True:
        _command = input("Enter 1 to find contact by name.\nEnter 2 to find contact by phone number\n"
                         "Enter something else to get back to main menu.\n")
        if _command == "1":
            name = input("Type in the contact's name:\n")
            contact_id = 0
            is_founded = False
            for i in range(len(contacts)):
                if contacts[i].name == name:
                    contact_id = i
                    is_founded = True
                    break
            if is_founded:
                print("Wanted contact:")
                print(str(contact_id).ljust(4) + " | " + contacts[contact_id].name.ljust(20) + " | "
                      + contacts[contact_id].phone)
                return
            else:
                print("There is no contact with name `" + name + "`.")
        elif _command == "2":
            phone = input("Type in the contact's phone number:\n")
            contact_id = 0
            is_founded = False
            for i in range(len(contacts)):
                if contacts[i].phone == phone:
                    contact_id = i
                    is_founded = True
                    break
            if is_founded:
                print("Wanted contact:")
                print(str(contact_id).ljust(4) + " | " + contacts[contact_id].name.ljust(20) + " | "
                      + contacts[contact_id].phone)
                return
            else:
                print("There is no contact with phone `" + phone + "`.")
        else:
            return


contacts.append(Contact("Dmytro Shostak", "380966547630"))
contacts.append(Contact("Kolya Ziryanov", "88005553535"))
contacts.append(Contact("Valik Mikhienko", "9379992"))
contacts.append(Contact("Andrii Luzan", "82852257380"))


print("ContactList v1.0\n")
print_contacts()
while True:
    command = input("\nEnter 1 to print contact list.\nEnter 2 to add contact.\nEnter 3 to change contact\n"
                    "Enter 4 to delete contact\nEnter 5 to search in contact list\nEnter 0 to close program\n")
    if command == "0":
        break
    elif command == "1":
        print_contacts()
    elif command == "2":
        add_contact()
    elif command == "3":
        change_contact()
    elif command == "4":
        delete_contact()
    elif command == "5":
        find_contact()
    else:
        print("Invalid input. Try again")
