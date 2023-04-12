import asyncio
import requests
import datetime

async def submit_proposal(researcher_id, acronym, title, description, budget, end_date):
    # Define the URL for the FastAPI app
    researcher_url = "http://localhost:8001"
    
    # Define the data for the research proposal
    params = {
        "acronym": acronym,
        "title": title,
        "description": description,
        "budget": budget,
        "end_date": end_date, 
    }

    # Send a POST request to the submit_proposal function in the researcher app with query parameters
    submit_proposal_url = f"{researcher_url}/researcher/{researcher_id}/submit_proposal"
    response = requests.post(submit_proposal_url, params=params)
    proposal_result = response.json()
    return proposal_result

async def get_approval(acronym):
    # Define the URL for the FastAPI app
    funding_group_url = "http://localhost:8003"
    
    # Send a GET request to the get_approval function in the funding group app with query parameters
    get_approval_url = f"{funding_group_url}/dcu/{acronym}"
    response = requests.get(get_approval_url)
    approval_result = response.json()
    return approval_result

async def submit_and_get_approval(researcher_id, acronym, title, description, budget, end_date):
    # Submit proposal
    proposal_result = await submit_proposal(researcher_id, acronym, title, description, budget, end_date)

    # Get approval
    approval_result = await get_approval(acronym)

    print(f"Proposal Result: {proposal_result}")
    print(f"Approval Result: {approval_result}")

async def main():
    researcher_id = 2
    proposals = [
        {"acronym": "DTF", "title": "Example Research Proposal 1", "description": "This is an example research proposal 1.", "budget": 300_000},
        {"acronym": "ABC", "title": "Example Research Proposal 2", "description": "This is an example research proposal 2.", "budget": 500_000},
        # Add more research proposals here as needed
    ]
    current_date = datetime.datetime.now()
    endate = current_date + datetime.timedelta(days=365)
    end_date = endate.strftime('%d-%m-%Y')

    # Create tasks for the concurrent execution of submit_and_get_approval
    submit_and_get_approval_tasks = []
    for proposal in proposals:
        acronym = proposal["acronym"]
        title = proposal["title"]
        description = proposal["description"]
        budget = proposal["budget"]
        submit_and_get_approval_task = asyncio.create_task(submit_and_get_approval(researcher_id, acronym, title, description, budget, end_date))
        submit_and_get_approval_tasks.append(submit_and_get_approval_task)

    # Gather tasks and wait for them to complete
    await asyncio.gather(*submit_and_get_approval_tasks)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())