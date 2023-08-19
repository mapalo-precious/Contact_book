contacts= {'name':["Number",'Email',"Address"]}
welcome='Welcome to my contact book you can create and delete contacts'
print(welcome)

def main():
  contact=input('Would you like to:\n~Create a new contact(Type "N")\n~Delete an existing contact(Type "D")\nHere is your contact book so far\n{}\nYour answer:   '.format(contacts) )
  if contact.lower()=='n':
    name=input("What is the name of your contact")
    number=input('What is the number of your new contact')
    address=input('What is the address of your new contact')
    email=input('What is the email address for your new contact (Use this format: firstname.lastname@domain.com )')
    contacts[name] =[number,email,address]
    print("This is your updated contact book\n{}".format(contacts))
  elif contact.lower()=='d':
    delete=input("What would you like to delete?{}\nyour answer:     ".format({k.lower(): v for k, v in contacts.items()}.keys()))
    delete.lower()
    del contacts[delete]
    print("This is your updated contact book\n{}".format(contacts))
  else:
    print('Error:Invalid process')

while True:
  ask=input('Would you like to continue? (Press "a" to continue or "e" to exit)\nYour answer:   ')
  if ask.lower()=='a':
    print(main())
  elif ask.lower()=='e':
    break
  else:
    print('Error: Invalid answer')
    break
