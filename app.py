from fastapi import FastAPI, Response
import requests
import time

app = FastAPI()

STUDENT_ID = "BSCS-22051"

# Middleware Header
@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = STUDENT_ID
    return response

# Circuit Breaker Variables
failure_count = 0
FAILURE_THRESHOLD = 3
circuit_open = False
last_failure_time = 0
RECOVERY_TIME = 10


@app.get("/")
def home():
    return {"message": "StudySync Running"}

@app.get("/ask-llm")
def ask_llm():
    global failure_count
    global circuit_open
    global last_failure_time

    # Open state
    if circuit_open:
        current_time = time.time()

        # Half-open check
        if current_time - last_failure_time > RECOVERY_TIME:
            circuit_open = False
            failure_count = 0
        else:
            return {
                "status": "fallback",
                "message": "LLM service unavailable. Try later."
            }

    try:
        # Fake external API call
        response = requests.get(
            "https://httpstat.us/500",
            timeout=3
        )

        response.raise_for_status()

        return {
            "status": "success",
            "data": response.text
        }

    except Exception:
        failure_count += 1

        if failure_count >= FAILURE_THRESHOLD:
            circuit_open = True
            last_failure_time = time.time()

        return {
            "status": "error",
            "message": "External API failed"
        }