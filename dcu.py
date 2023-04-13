from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

approved_project = {}

# Define routes for DCU app
@app.get("/dcu/transactions/{project_id}")
async def get_project_transactions(project_id: str):
    # Logic for getting project details
    transactions_arr  = approved_project[project_id]["transactions"]
    return {"project_id": project_id, "transactions": f"Transactions: {transactions_arr}"}

@app.post("/dcu/{project_id}/notify")
async def notify(project_id: str, budget: float, researcher_id: int, end_date: str):
    # Logic for notifying DCU about approved project
    approved_project[project_id] = {"balance":budget,"researcher": researcher_id, "end_date": end_date, "transactions": {}, "researchers":[]}
    return {"message": "Project notification sent successfully!","projects": approved_project }


@app.post("/dcu/{project_id}/withdraw")
async def withdraw(project_id: str, amount: float, researcher_id: int, date:str):
    if project_id not in approved_project:
        raise HTTPException(status_code=400, detail="Project not approved or doesn't exist")
    
    project = approved_project[project_id]
    if researcher_id != project["researcher"] and researcher_id not in project["researchers"]:
        raise HTTPException(status_code=400, detail="User does not have access")
    if amount > project["balance"]:
       raise HTTPException(status_code=400, detail="Not enough funds")
    if datetime.strptime(date, "%d-%m-%Y") > datetime.strptime(project["end_date"], "%d-%m-%Y"):
        raise HTTPException(status_code=400, detail="Your account has expired")

    project["balance"] -= amount
    balance = project["balance"]
    project["transactions"][len(project["transactions"])] = {"date": date, "withdrawn": amount} 
    return {"project": project_id, "status": f"Withdraw Successful, Remainng balance:{balance}"}

@app.post("/dcu/{project_id}/edit")
async def withdraw(project_id: str, researcher_id: int, other_id: int, action:str):
    if project_id not in approved_project:
        raise HTTPException(status_code=400, detail="Project not approved or doesn't exist")

    project = approved_project[project_id]
    if project["researcher"] != researcher_id:
       raise HTTPException(status_code=400, detail="User does not have access")
    
    researchers_list = project["researchers"]
    if action == "add":
        if other_id in project["researchers"]:
            raise HTTPException(status_code=400, detail="Already been added to project")
        else:
            project["researchers"].append(other_id)
            return {"status": f"added succesfully, current researchers: {researchers_list}"}
    elif action == "del":
        if other_id not in project["researchers"]:
            raise HTTPException(status_code=400, detail="Cannot delete")
        else:
            project["researchers"].remove(other_id)
            return {"status": f"removed succesfully, current researchers: {researchers_list}"}
    

# Run the DCU app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)
    pass