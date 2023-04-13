from fastapi import FastAPI, HTTPException
import httpx
import asyncio

app = FastAPI()

TOTAL_BUDGET = 1_000_000
dcu_url = "http://localhost:8003"

# Define routes for funding group app
@app.post("/funding_group/confirm")
async def approve(researcher_id: int, acronym: str, title: str, description: str, budget: float, end_date: str):
    global TOTAL_BUDGET
    if not (200_000 <= budget <= 500_000):
        raise HTTPException(status_code=400, detail="Invalid funding amount")
    if TOTAL_BUDGET - budget < 0:
        raise HTTPException(status_code=400, detail="Funding agency budget exceeded")
    TOTAL_BUDGET -= budget

    # Approve the proposal and return its ID
    params = {
        "budget": budget,
        "end_date": end_date,
        "researcher_id": researcher_id
    }

    submit_proposal_url = f"{dcu_url}/dcu/{acronym}/notify"

    async with httpx.AsyncClient() as client:
        await client.post(submit_proposal_url, params=params)

    return {"id": acronym, "status": "approved", "fund_left": TOTAL_BUDGET}

# Run the funding group app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
