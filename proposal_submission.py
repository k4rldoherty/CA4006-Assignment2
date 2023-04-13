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
    researcher_id = 2
    acronym =  "ABC"
    title = "Example Research Proposal 2"
    description ="This is an example research proposal 2."
    budget = 500_000
        # Add more research proposals here as needed
    current_date = datetime.datetime.now()
    endate = current_date + datetime.timedelta(days=365)
    end_date = endate.strftime('%d-%m-%Y')

 
    print(submit_proposal(researcher_id, acronym,title,description, budget, end_date))

if __name__ == "__main__":
    main()