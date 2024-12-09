import subprocess
import os
from datetime import datetime
from crawler_utils import start_crawler
from rag_utils import retrieve_info, load_documents
from config import *
from prompt import *
from llm import llm_generate, generate_prompt_with_knowledge

load = False

def analyze_website(url):

    original_dir = os.getcwd()
    start_crawler(url)

    rag_db = load_documents('output-1.json', load)

    product_description = llm_generate(SYS_PROMPT, generate_prompt_with_knowledge(USR_PROMPT1, rag_db, "company Description, product usecase"))
    
    usr_prompt2 = "\nPlease perform Target Market Analysis (demographics, psychographics, behavior) given the following content. Your response needs to be in markdown format. Always start from second level (##) heading\n\n" \
    + product_description + "".join([item + "\n" for item in retrieve_info(rag_db, "Target Market Analysis, Product Description")])

    target_market = llm_generate(SYS_PROMPT, usr_prompt2)

    usr_prompt3 = "\nPlease perform detailed Competitive Analysis given the following content.You need to include product details. Your response needs to be in markdown format. Always start from second level (##) heading\n\n" \
    + product_description + "".join([item + "\n" for item in retrieve_info(rag_db, "Product details, features, Invention, new and different")])

    competitive_analysis = llm_generate(SYS_PROMPT, usr_prompt3)

    usr_prompt4 = "\nPlease perform Pricing Strategy Analysis given the following content. Your response needs to be in markdown format. Always start from second level (##) heading\n\n" \
    + product_description + "".join([item + "\n" for item in retrieve_info(rag_db, "Pricing")])

    pricing = llm_generate(SYS_PROMPT, usr_prompt4)

    usr_prompt5 = """\nPlease provide a short executive summary of the following paragraphs into one short paragraph and include concrete conclusion judegment. start with section title "Conclusion" and your response needs to be in markdown format. Always start from second level (##) heading\n\n""" \
    + product_description + competitive_analysis + target_market + pricing

    summary = llm_generate(SYS_PROMPT, usr_prompt5) 

    final_report = "# Research Report\n" + product_description + "\n" + competitive_analysis + "\n" + target_market + "\n" + pricing + "\n" + summary 

    relative_path_to_target = os.path.join('..', 'files_storage', 'report_files')
    target_directory = os.path.abspath(relative_path_to_target)
    current_time = datetime.now()
    file_name = "report" + current_time.strftime("%Y%m%d%H%M%S") + ".md"
    pdf_name = "report" + current_time.strftime("%Y%m%d%H%M%S") + ".pdf"
    file_path = os.path.join(target_directory, file_name)
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(final_report)

    os.chdir(target_directory)
    convert_command = f"md-to-pdf {file_name}"  

    subprocess.run(convert_command, shell=True)

    os.chdir(original_dir)
    return final_report + f"\n\n[Download Report PDF](http://localhost:8080/report_files/{pdf_name})"

analyze_website("https://www.rabbit.tech/")

# SYS_PROMPT = "You are a world class analyst. You are very senstive to numbers since numbers are important. You have strong Analytical Skills and always paying Attention to Details. You use Problem-Solving techniques and Critical Thinking when needed."
# usr_prompt1 = "\nPlease write a couple sentences short Product Descriptions given the following content."
# product_description = llm_generate(SYS_PROMPT, usr_prompt1)