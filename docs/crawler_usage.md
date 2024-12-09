# Crawler Usage Guide

This document explains how to use the web crawler in the project.

---

## **Function: `start_crawler(url)`**
The `start_crawler(url)` function initiates the web crawling process.

---

### **Code Example**
```python
import os
import subprocess

def start_crawler(url):
    os.chdir("crawler")  # Navigate to the crawler folder
    generate_config(url)  # Generate the crawler configuration file
    command = "npm start"  # Run the crawler using npm
    subprocess.run(command, shell=True)

# Example Usage
url = "https://example.com"  # Replace with the target URL
start_crawler(url)
```

### **How It Works**
1. Navigate to the Crawler Folder:
The function changes the working directory to crawler.

2. Generate Crawler Configuration:
Calls the generate_config(url) function to create a configuration file based on the provided URL.

3. Run the Crawler:
Executes the npm start command to start the crawler.

### **Crawler Output**
After running the crawler, the output is stored in:
`crawler/output-1.json`
This file contains the results of the web crawling process, typically in JSON format.

#### Important Notes
Ensure that Node.js, npm, and required packages are installed.
Customize the url variable as needed before running the function.

# How the crawler is implemented?

This section explains how the web crawler is implemented, covering the main modules and their functionalities.

---

## **1. Overview**
The crawler system is built using **Node.js**, **TypeScript**, and **Playwright**. The architecture is modular, with different files handling specific tasks such as configuration management, crawling logic, and command-line interface integration.

---

## **2. Core Modules**
### **2.1 CLI Interface (`cli.ts`)**
- Uses the `commander` library to create a command-line interface.
- Interactively collects inputs like:
  - The target website's starting URL.
  - URL matching patterns.
  - CSS selectors to extract content.
- Calls the crawling process using `core.ts` functions.

---

### **2.2 Configuration Management (`config.ts`)**
- Defines and validates the crawling configuration using `zod`.
- Loads environment variables using `dotenv`.

---

### **2.3 Crawling Logic (`core.ts`)**
- Implements the crawling process using **Crawlee** and **Playwright**.
- Key functions:
  - `crawl(config: Config)`: Initiates a crawling session using Playwright.
  - `write(config: Config)`: Writes the crawled data to the specified output file.
  - `getPageHtml(page, selector)`: Extracts page content based on CSS selectors.

---

### **2.4 Main Application Entry (`main.ts`)**
- Contains the main execution logic:
  - Loads the default configuration.
  - Calls the `crawl()` and `write()` functions.

---

### **2.5 REST API Server (`server.ts`)**
- Uses **Express.js** to provide a REST API.
- Key API endpoint:
  - `POST /crawl`: Accepts a crawling request and triggers the crawling process.
- Supports:
  - Cross-Origin Resource Sharing (CORS).
  - JSON request/response payloads.

---

## **3. Summary**
The crawler system integrates a robust configuration scheme, scalable crawling logic using Playwright, and a command-line interface for interactive use. Additionally, a REST API endpoint is provided for external integration.

---