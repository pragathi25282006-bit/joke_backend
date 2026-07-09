from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import traceback
import os
app=FastAPI()
client=genai.Client(api_key=os.environ["GEMINI_API_KEY"])
class joke_genre(BaseModel):
    prompt:str
    category:str
    language:str
@app.post("/joke")
def joke(req:joke_genre):
    try:
        full_prompt=f"generate a funny {req.category} joke about {req.prompt} in {req.language}"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )
        return {
            "question": req.prompt,
            "category":req.category,
            "language":req.language,
            "answer": response.text
        }
    except Exception as e:
        traceback.print_exc()   # Prints the full error in the terminal
        return {"error": str(e)}