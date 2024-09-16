service_tickets = {}

def open_ticket():
    ticket_id = len(service_tickets) + 1
    customer = input("Enter customer name: ")
    issue = input("Enter issue: ")  
    status = input("Status: open or closed? ")
    service_tickets[ticket_id] = {"customer": customer, "issue": issue, "status": status}
    print("Ticket opened successfully.")

def updated_ticket():
    request = input("Enter ticket ID: ")
    service_tickets[int(request)]["status"] = input("Status: open or closed? ")
    print("Ticket updated successfully.")

def display_all():
    print(service_tickets)

def display_open():
    for ticket in service_tickets:
        if service_tickets[ticket]["status"] == "open":
            print(service_tickets[ticket])

def main():
    while True:
        print("1. Open a ticket")
        print("2. Update a ticket")
        print("3. Display all tickets")
        print("4. Display open tickets")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            open_ticket()
        elif choice == "2":
            updated_ticket()
        elif choice == "3":
            display_all()
        elif choice == "4":
            display_open()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
