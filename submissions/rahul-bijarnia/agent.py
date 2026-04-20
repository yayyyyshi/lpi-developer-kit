import requests
import sys

query = sys.argv[1]

BASE_URL = "http://localhost:8000"   # LPI sandbox URL

# ---- REAL LPI TOOL CALLS ----
def smile_overview():
    res = requests.get(f"{BASE_URL}/smile_overview")
    return res.json()

def query_knowledge(q):
    res = requests.get(f"{BASE_URL}/query_knowledge", params={"query": q})
    return res.json()

def get_case_studies(q):
    res = requests.get(f"{BASE_URL}/get_case_studies", params={"query": q})
    return res.json()

# ---- CALL TOOLS ----
smile = smile_overview()
knowledge = query_knowledge(query)
cases = get_case_studies(query)

# ---- COMBINE ----
combined = f"""
SMILE:
{smile}

KNOWLEDGE:
{knowledge}

CASE STUDIES:
{cases}
"""

# ---- LLM CALL ----
def call_llm(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        return res.json()["response"]
    except:
        return "LLM not running.\n" + prompt

final = call_llm(combined)

# ---- OUTPUT ----
print("\n--- SMILE OVERVIEW ---")
print(smile)

print("\n--- KNOWLEDGE ---")
print(knowledge)

print("\n--- CASE STUDIES ---")
print(cases)

print("\n--- FINAL ANSWER ---")
print(final)
