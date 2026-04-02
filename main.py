# Import FastAPI Build web API.
from fastapi import FastAPI
# For accessing JSON data
from fastapi.requests import Request  
# operating system access, files and – Access environment variables like API keys.
import os
#Communicate with OpenAI models.
import openai
import time


# Create the FastAPI app instance
app = FastAPI()
# Set API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_RETRIES = 5
Backoff_time = 2

# Define a POST endpoint at /ai-webhook
@app.post("/ai-webhook")
async def ai_webhook(request: Request):
    # Parse incoming JSON
    data = await request.json()

    # Extract the question from JSON
    user_prompt = data.get("question", "No question provided")

    retry_count = 0
    while retry_count < MAX_RETRIES
        try:
            # Call AI – Send prompt to OpenAI.
            response = openai.ChatCompletion.create(
        model= "gpt-4",
        message=[{"role":"user", "content": user_prompt}])
        #extract the ai's response
            ai_reply = {"answer":response.choices[0].message.content}
        # Return the response (FastAPI will convert it to JSON)
            break
        except openai.error.RateLimitError:
            retry_count += 1
            print (f"Rate limit hit, retrying in {Backoff_time} seconds...")
            time.sleep(Backoff_time)
            Backoff_time*2
        except Exception as e:
            retry_count += 1
            print(f"Error occurred: {e}, retrying...")
            time.sleep(Backoff_time)
            Backoff_time*2
    return ai_reply