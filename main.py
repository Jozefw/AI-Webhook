# Import FastAPI
from fastapi import FastAPI
from fastapi.requests import Request  # For accessing JSON data

# Create the FastAPI app instance
app = FastAPI()

# Define a POST endpoint at /ai-webhook
@app.post("/ai-webhook")
async def ai_webhook(request: Request):
    # Parse incoming JSON
    data = await request.json()

    # Extract the question from JSON
    question = data.get("question", "No question provided")

    # Prepare the response
    response = {"answer": f"You asked: {question}"}

    # Return the response (FastAPI will convert it to JSON)
    return response