from config import *
import json
import requests
from rag_utils import retrieve_info

def llm_generate(sys_prompt,input_text):
    # Set up the API request
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    # input_text = "You must strickly follow the chat history and response my question. \n" + input_text
    # Set up the data for the API request
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "system", "content": sys_prompt}, {"role": "user", "content": input_text}],
        "temperature": 0
    }

    # Make the API request
    print("\n---------------------Prompt is below ---------------------\n")
    print(input_text)
    # Make the HTTP POST request
    session = requests.Session()
    session.trust_env = True

    response = session.post(f"{OPENAI_API_BASE}/chat/completions", headers=headers, data=json.dumps(data))
    print("response", response)
    response_data = response.json()

    # Extract the response from the API
    prompt_response = response_data["choices"][0]["message"]["content"]
    usage = response_data["usage"]

    # Print the response
    print(prompt_response)
    return prompt_response

def generate_prompt_with_knowledge(original_prompt, vec_db, search_keyword):
    return original_prompt + "".join([item + "\n" for item in retrieve_info(vec_db, search_keyword)])