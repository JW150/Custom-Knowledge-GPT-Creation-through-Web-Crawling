import subprocess
import os
from datetime import datetime
from crawler_utils import start_crawler
from rag_utils import load_documents
from config import *
from prompt import *
from llm import llm_generate, generate_prompt_with_knowledge

load = False

def save_report(text):
    relative_path_to_target = os.path.join('.', 'report_files')
    target_directory = os.path.abspath(relative_path_to_target)
    current_time = datetime.now()
    file_name = "report" + current_time.strftime("%Y%m%d%H%M%S") + ".md"
    file_path = os.path.join(target_directory, file_name)

    with open(file_path, "w", encoding='utf-8') as file:
        file.write(text)

    os.chdir(target_directory)
    convert_command = f"md-to-pdf {file_name}"  
    subprocess.run(convert_command, shell=True)

def analyze_website(url):

    original_dir = os.getcwd()
    start_crawler(url)

    rag_db = load_documents('output-1.json', load)

	# here is an example of using RAG system for LLM to do product research
    product_description = llm_generate(SYS_PROMPT, generate_prompt_with_knowledge(USR_PROMPT1, rag_db, "company Description, product usecase"))
    target_market = llm_generate(SYS_PROMPT, generate_prompt_with_knowledge(USR_PROMPT2 + product_description, rag_db, "Target Market Analysis, Product Description"))
    competitive_analysis = llm_generate(SYS_PROMPT, generate_prompt_with_knowledge(USR_PROMPT3 + product_description, rag_db, "Product details, features, Invention, new and different"))
    pricing = llm_generate(SYS_PROMPT, generate_prompt_with_knowledge(USR_PROMPT4 + product_description, rag_db, "Pricing"))

    final_usr_prompt = """\nPlease provide a short executive summary of the following paragraphs into one short paragraph and include concrete conclusion judegment. start with section title "Conclusion" and your response needs to be in markdown format. Always start from second level (##) heading\n\n""" \
    + product_description + competitive_analysis + target_market + pricing

    summary = llm_generate(SYS_PROMPT, final_usr_prompt) 
    final_report = "# Research Report\n" + product_description + "\n" + competitive_analysis + "\n" + target_market + "\n" + pricing + "\n" + summary 

    os.chdir(original_dir)
    save_report(final_report)
    os.chdir(original_dir)

analyze_website("https://www.rabbit.tech/")

# SYS_PROMPT = "You are a world class analyst. You are very senstive to numbers since numbers are important. You have strong Analytical Skills and always paying Attention to Details. You use Problem-Solving techniques and Critical Thinking when needed."
# usr_prompt1 = "\nPlease write a couple sentences short Product Descriptions given the following content."
# product_description = llm_generate(SYS_PROMPT, usr_prompt1)