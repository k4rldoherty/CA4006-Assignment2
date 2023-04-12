from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()
fund_url = "http://localhost:8002"

# Define routes for researcher app
@app.get("/researcher/{researcher_id}")
async def get_researcher(researcher_id: int):
    return {"researcher_id": researcher_id, "message": "Researcher details retrieved successfully!"}

async def submit_proposal_async(researcher_id: int, acronym: str, title: str, description: str, budget: float, end_date: str):
    # Logic for submitting research proposal
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
        await client.post(submit_proposal_url, params=params)

    return {"message": "Research proposal submitted successfully!"}

@app.post("/researcher/{researcher_id}/submit_proposal")
async def submit_proposal(researcher_id: int, acronym: str, title: str, description: str, budget: float, end_date: str):
    # Run the submit_proposal_async function concurrently using asyncio.gather()
    await asyncio.gather(
        submit_proposal_async(researcher_id, acronym, title, description, budget, end_date)
    )

    return {"researcher_id": researcher_id, "acronym": acronym, "title": title, "description": description,
            "message": "Research proposal submitted successfully!"}

# Run the researcher app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)