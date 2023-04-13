import requests
import sys

def withdraw(researcher_id, acronym):
    researcher_url = "http://localhost:8001"
    params = {
        "researcher_id": researcher_id,
    }
    transactions_url = f"{researcher_url}/researcher/transactions/{acronym}"
    response = requests.get(transactions_url, params=params)
    proposal_result = response.text
    return proposal_result


def main():
    researcher_id = sys.argv[1]
    acronym =  sys.argv[2]
    
    print(withdraw(researcher_id, acronym))

if __name__ == "__main__":
    main()