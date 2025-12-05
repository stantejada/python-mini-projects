

def read_letter():
    with open("letter.txt", "r") as f:
        letter = f.read()
    return str(letter)

def read_contacts():
    contacts = []
    with open("contacts.txt", "r") as f:
        contacts = f.read()
    return contacts

def send_mail(letter, contact):
    merge_mail = letter.replace("[Name]", contact)
    return merge_mail

def main():
    letter = read_letter()
    contacts = list(filter(None, read_contacts().split("\n"))) 
    for contact in contacts:
        mail = send_mail(letter=letter, contact=contact)
        print(mail)



if __name__ == "__main__":
    app = main()