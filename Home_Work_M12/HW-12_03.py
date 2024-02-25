import csv


def write_contacts_to_file(filename, contacts):
    print(contacts)
    with open(filename, "w", newline='') as fh:
        field_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(fh, fieldnames = field_names)
        writer.writeheader()
        for row in contacts:
            # print(row)
            writer.writerow(row)
            
            
def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        contact_list = []
        for row in reader:
            contact = {"name": row["name"], "email": row["email"], "phone": row["phone"], "favorite": eval(row["favorite"])}
            # print(contact)
            contact_list.append(contact)
            # print(row['email'], row['name'])
        print(contact_list)    
    return contact_list      
    
