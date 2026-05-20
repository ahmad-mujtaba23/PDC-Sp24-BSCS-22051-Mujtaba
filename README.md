Ahmad Mujtaba — BSCS-22051

# PDC Assignment 4

## How to Run

### Step 1
Install Python.

### Step 2
Install dependencies:

pip install -r requirements.txt

### Step 3
Run FastAPI server:

uvicorn app:app --reload

### Step 4
Open browser:

http://127.0.0.1:8000/docs

### Step 5
Run test script:

python test_failure.py

## Expected Behavior

- First few requests fail normally.
- After threshold reached, circuit breaker opens.
- System returns fallback response.
- All responses include X-Student-ID header.