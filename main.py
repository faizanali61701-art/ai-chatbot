import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="AI Chatbot")

# Tokens aur Keys (محفوظ ڈمی ویلیوز)
VERIFY_TOKEN = "faisal123"
GEMINI_API_KEY = "YOUR_GEMINI_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PHONE_NUMBER_ID = "1354741821055868"

@app.get("/")
async def root():
    return {"status": "Bot is Running"}

@app.get("/webhook")
async def verify_webhook(request: Request):
    # Meta Webhook Verification
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return int(challenge)
        else:
            return JSONResponse(content={"error": "Verification failed"}, status_code=403)
    return JSONResponse(content={"error": "Missing parameters"}, status_code=400)

@app.post("/webhook")
async def webhook_handler(request: Request):
    try:
        body = await request.json()
        # یہاں واٹس ایپ اور جیمینی اے آئی کی پروسیسنگ لکھی جائے گی
        return {"status": "ok"}
    except Exception as e:
        print("Error aaya hai:", e)
        return {"status": "ok"}