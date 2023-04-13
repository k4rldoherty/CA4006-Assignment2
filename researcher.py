from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()
fund_url = "http://localhost:8002"
dcu_url = "http://localhost:8003"


@app.get("/researcher/{researcher_id}")
async def get_researcher(researcher_id: int):
    return {"researcher_id": researcher_id, "message": "Researcher details retrieved successfully!"}

async def submit_proposal_async(researcher_id: int, acronym: str, title: str, description: str, budget: float, end_date: str):
    params = {
        "acronym": acronym,
        "title": title,
        "description": description,
        "budget": budget,
        "end_date": end_date,
        "researcher_id": researcher_id
    }

    submit_proposal_url = f"{fund_url}/funding_group/confirm"
    async with httpx.AsyncClient() as client:
        response = await client.post(submit_proposal_url, params=params)
        if response.status_code == 200:
            status = response.json()["status"]
        else:
            status = 'Project was not approved'
    return {"status": status, "acronym" : acronym}

@app.post("/researcher/{researcher_id}/submit_proposal")
async def submit_proposal(researcher_id: int, acronym: str, title: str, description: str, budget: float, end_date: str):
    result = await asyncio.gather(
        submit_proposal_async(researcher_id, acronym, title, description, budget, end_date)
    )
    return {"acronym": result[0]["acronym"],"status": result[0]["status"]}

async def withdraw_async(researcher_id: int, acronym: str, amount: float, date: str):
    params = {
        "amount": amount,
        "researcher_id": researcher_id,
        "date": date
    }

    withdraw_url = f"{dcu_url}/dcu/{acronym}/withdraw"
    async with httpx.AsyncClient() as client:
        response = await client.post(withdraw_url, params=params)
        if response.status_code == 200:
            status = response.json()["status"]
        else:
            status = 'Could not withdraw'
    return {"status": status, "acronym" : acronym}

@app.post("/researcher/{researcher_id}/withdraw_request")
async def withdraw_request(researcher_id: int, acronym: str, amount: float, date: str):
    result = await asyncio.gather(
        withdraw_async(researcher_id, acronym, amount, date)
    )
    return {"acronym": result[0]["acronym"],"status": result[0]["status"]}

async def edit_async(researcher_id: int, acronym: str, other_id: int, action: str):
    params = {
        "researcher_id": researcher_id,
        "other_id": other_id,
        "action": action
    }

    edit_url = f"{dcu_url}/dcu/{acronym}/edit"
    async with httpx.AsyncClient() as client:
        response = await client.post(edit_url, params=params)
        if response.status_code == 200:
            status = response.json()["status"]
        else:
            status = 'Could not edit researchers'
    return {"status": status, "acronym" : acronym}

@app.post("/researcher/{acronym}/edit")
async def edit_request(researcher_id: int, acronym: str, other_id: int, action: str):
    result = await asyncio.gather(
        edit_async(researcher_id, acronym, other_id, action)
    )

    return {"acronym": result[0]["acronym"],"status": result[0]["status"]}

async def transactions_async(researcher_id: int, acronym: str):
    params = {
        "researcher_id": researcher_id,
    }

    transaction_url = f"{dcu_url}/dcu/transactions/{acronym}"
    async with httpx.AsyncClient() as client:
        response = await client.get(transaction_url, params=params)
        if response.status_code == 200:
            status = response.json()["transactions"]
        else:
            status = 'cannot edit researchers who have access'
    return {"transactions": status, "acronym" : acronym}

@app.get("/researcher/transactions/{acronym}")
async def transactions_request(researcher_id: int, acronym: str):
    result = await asyncio.gather(
        transactions_async(researcher_id, acronym)
    )

    return {"acronym": result[0]["acronym"],"status": result[0]["transactions"]}


# Run the researcher app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
