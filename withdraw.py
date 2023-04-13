import sys
import requests
import datetime

def withdraw(researcher_id, acronym, amount, date):
    researcher_url = "http://localhost:8001"
    params = {
        "acronym": acronym,
        "amount": amount,
        "date": date,
    }
    withdraw_url = f"{researcher_url}/researcher/{researcher_id}/withdraw_request"
    response = requests.post(withdraw_url, params=params)
    proposal_result = response.text
    return proposal_result


def main():
    researcher_id = sys.argv[1]
    acronym =  sys.argv[2]
    amount = float(sys.argv[3])
    current_date = datetime.datetime.now()
    date = current_date.strftime('%d-%m-%Y')

    print(withdraw(researcher_id, acronym, amount, date))

if __name__ == "__main__":
    main()