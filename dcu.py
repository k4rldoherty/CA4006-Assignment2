from fastapi import FastAPI

app = FastAPI()

approved_project = {}

# Define routes for DCU app
@app.get("/dcu/{project_id}")
async def get_project(project_id: str):
    # Logic for getting project details
    return {"project_id": project_id, "message": "This project is aproved and is being stored by DCU!", "projects": approved_project}

@app.post("/dcu/{project_id}/notify")
async def notify(project_id: str, budget: float, researcher_id: int, end_date: str):
    # Logic for notifying DCU about approved project
    approved_project[project_id] = {"budget_id":budget,'researcher': researcher_id, "end_date": end_date}
    return {"message": "Project notification sent successfully!","projects": approved_project }

# Run the DCU app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)
    pass