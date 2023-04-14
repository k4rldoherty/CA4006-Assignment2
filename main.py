import subprocess

# Start fund server
fund_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'fund.py'])

# Start researcher server
researcher_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'researcher.py'])

# Start dcu server
dcu_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'dcu.py'])


while True:
    research_id = input("Enter your Researcher ID number:")
    
    while True:
        print("\nEnter Option Selection")
        print("Submit Proposal: 1")
        print("Withdraw funds: 2")
        print("Add resarcher: 3")
        print("Remove resarcher: 4")
        print("View Transactions: 5")
        print("Logout: 6\n")
        option = input("Enter your choice: ")
        if option == '1':
            try:
                print("\nPlease enter details:")
                acronym = input('Project Code: ')
                title = input('Project Title:')
                description = input('Project Description: ')
                budget = input("Amount of funding being requested(€):")
                end_date = input("End date(DD-MM-YYYY):")
                subprocess.run(['py', 'proposal_submission.py', research_id, acronym, title, description, budget, end_date])
            except FileNotFoundError:
                print("Option unavailable")
        elif option == '2':
            try:
                acronym = input('Project Code: ')
                amount = input("Amount to withdraw(€):")
                subprocess.run(['py', 'withdraw.py', research_id, acronym, amount])
            except FileNotFoundError:
                print("file not found!")
        elif option == '3':
            try:
                acronym = input('Project Code: ')
                other_id = input('Researcher to add to account (ID): ')
                subprocess.run(['py', 'edit_researchers.py', "add", research_id, acronym, other_id])
            except FileNotFoundError:
                print("file not found!")
        elif option == '4':
            try:
                acronym = input('Project Code: ')
                other_id = input('Researcher to remove from account (ID): ')
                subprocess.run(['py', 'edit_researchers.py', "del", research_id, acronym, other_id])
            except FileNotFoundError:
                print("file not found!")
        elif option == '5':
            try:
                acronym = input('Project Code: ')
                subprocess.run(['py', 'view_transactions.py',research_id, acronym])
            except FileNotFoundError:
                print("file not found!")
        elif option == '6':
            print("Logging out....")
            break
        else:
            print("Invalid choice. Please try again.")

