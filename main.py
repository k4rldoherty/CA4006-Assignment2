import subprocess

# Start fund.py in a new Command Prompt window
fund_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'fund.py'])

# Start researcher.py in a new Command Prompt window
researcher_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'researcher.py'])

# Start dcu.py in a new Command Prompt window
dcu_process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'py', 'dcu.py'])

# Take input as integer

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
                # Run proposal_submission.py using subprocess
                subprocess.run(['py', 'proposal_submission.py'])
            except FileNotFoundError:
                print("Option unavailable")
        elif option == '2':
            try:
                # Run withdraw-submission.py using subprocess
                subprocess.run(['py', 'withdraw_submission.py'])
            except FileNotFoundError:
                print("driver.py file not found!")
        elif option == '3':
            try:
                # Run withdraw-submission.py using subprocess
                subprocess.run(['py', 'edit_researchers.py', "add"])
            except FileNotFoundError:
                print("driver.py file not found!")
        elif option == '4':
            try:
                # Run withdraw-submission.py using subprocess
                subprocess.run(['py', 'edit_researchers.py', "del"])
            except FileNotFoundError:
                print("driver.py file not found!")
        elif option == '5':
            try:
                # Run withdraw-submission.py using subprocess
                subprocess.run(['py', 'view_transactions.py'])
            except FileNotFoundError:
                print("driver.py file not found!")
        elif option == '6':
            print("Logging out....")
            break
        else:
            print("Invalid choice. Please try again.")

