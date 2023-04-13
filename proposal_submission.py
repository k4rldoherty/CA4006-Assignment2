import sys
import requests
import datetime

def submit_proposal(researcher_id, acronym, title, description, budget, end_date):
    researcher_url = "http://localhost:8001"
    params = {
        "acronym": acronym,
        "title": title,
        "description": description,
        "budget": budget,
        "end_date": end_date, 
    }
    submit_proposal_url = f"{researcher_url}/researcher/{researcher_id}/submit_proposal"
    response = requests.post(submit_proposal_url, params=params)
    proposal_result = response.text
    return proposal_result


def main():
    researcher_id = sys.argv[1]
    acronym = sys.argv[2] 
    title = sys.argv[3]
    description = sys.argv[4]
    budget = float(sys.argv[5])
    end_date = sys.argv[6]

    print(submit_proposal(researcher_id, acronym,title,description, budget, end_date))

if __name__ == "__main__":
    main()