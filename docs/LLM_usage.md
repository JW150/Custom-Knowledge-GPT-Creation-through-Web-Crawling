# LLM Usage Guide

This document explains how to use the LLM integration for generating responses using OpenAI's API.

---

## **1. Function Overview**

### **1.1 Function: `llm_generate(sys_prompt, input_text)`**
Generates a response using the OpenAI API based on a system prompt and user input.

## **2. Usage Example**
To use this function, follow these steps:
1. Generate the Prompt with Knowledge: Use the generate_prompt_with_knowledge() function to create a specific prompt using the built vector database (rag_db), the original user prompt, and the targeted keywords.
```
product_description = llm_generate(
    SYS_PROMPT, 
    generate_prompt_with_knowledge(USR_PROMPT1, rag_db, "company Description, product usecase")
)
```

### How It Works
1. Create the Prompt:
	The generate_prompt_with_knowledge() function retrieves relevant content from the vector database rag_db using specific keywords like "company Description" and "product usecase."

2. Call the LLM API:
	The generated prompt is passed to the llm_generate() function, along with the system prompt SYS_PROMPT.
	The function sends the request to OpenAI's API and prints the response.

3. Receive the Response:
	The API returns the relevant answer, which is displayed and returned by the function.

### Important Notes
Make sure to set the following environment variables before running:
```
export OPENAI_API_KEY="your_openai_api_key"
export OPENAI_API_BASE="https://api.openai.com/v1"
export MODEL_NAME="gpt-3.5-turbo"
```

Ensure all required packages are installed:
```
pip install requests
```
Use the response from the API for further processing or display in your application.