
markdown
Copy code
# Vector Database Guide

This document explains how to use the vector database system for information retrieval using FAISS and HuggingFace embeddings.

---

## **1. Code Overview**
The following functions are used for creating and querying a vector database:

---

### **1.1 Function: `retrieve_info(db, query)`**
Retrieves similar content from the vector database based on a query.
```def retrieve_info(db, query)```

### **1.2 Function: load_documents(output_path, load=False)**
Loads and processes documents into a vector database using FAISS and HuggingFace embeddings.

## **2. Usage Example**
1. Start the Crawler: Use the crawler to extract web content.
start_crawler(url)
2. Load the Data into the Vector Database: Use the crawler output (output-1.json) as input for the vector database.
rag_db = load_documents('output-1.json', load=False)
3. Retrieve Relevant Information: Pass the rag_db to a function like generate_prompt_with_knowledge() to search for relevant content using specific keywords.

## **Important Notes:**
Ensure all dependencies are installed, including:
```
pip install sentence-transformers langchain-community langchain
```
If running the system multiple times, set load=True to reuse the existing vector database instead of recreating it.


# How the vector database is implemented?

This section explains the implementation of the vector database system using `FAISS`, `HuggingFaceEmbeddings`, and `LangChain`.

---

## **1. Overview**
The vector database system processes and indexes crawled data for efficient retrieval. It leverages FAISS as the storage backend and HuggingFace embeddings for text vectorization.

---

## **2. Core Functions (rag_utils.py)**

### **2.1 Document Loading (`load_documents`)**
This function loads crawled web content into a vector database. It supports both creating a new database and loading an existing one.

### **2.2 Information Retrieval (retrieve_info)**
Retrieves relevant text data from the vector database based on a query.
```
def retrieve_info(db, query):
    similar_response = db.similarity_search(query, k=4)
    page_contents_array = [doc.page_content for doc in similar_response]
    return page_contents_array

```

How It Works:

Query Execution: Searches for similar content using the provided query and returns the top 4 matching results.
Result Extraction: Extracts and returns relevant page content.

## **3. Summary**
The implementation leverages LangChain’s components for embeddings, text splitting, and FAISS vector storage. The system efficiently processes web-crawled data, enabling semantic search using a vectorized format.