import sys
import requests
import datetime

def edit(researcher_id, acronym, other_id, action):
    researcher_url = "http://localhost:8001"
    params = {
        "researcher_id": researcher_id,
        "action": action,
        "other_id": other_id,
    }
    edit_url = f"{researcher_url}/researcher/{acronym}/edit"
    response = requests.post(edit_url, params=params)
    proposal_result = response.text
    return proposal_result


def main():
    if sys.argv[1] == "add":
        action = "add"
    elif sys.argv[1] == "del":
        action = "del"
    researcher_id = sys.argv[2]
    other_id = int(sys.argv[4])
    acronym =  sys.argv[3]
    
    print(edit(researcher_id, acronym, other_id, action))

if __name__ == "__main__":
    main()