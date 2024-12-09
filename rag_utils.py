from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS

def retrieve_info(db, query):
    similar_response = db.similarity_search(query, k=4)
    page_contents_array = [doc.page_content for doc in similar_response]
    return page_contents_array

def load_documents(output_path, load=False):
    db = None
    if load == False:
        embeddings = HuggingFaceEmbeddings()
        with open(output_path, encoding='utf-8') as f:
            data = f.read()

        text_splitter = CharacterTextSplitter(
            separator=" ",
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False,
        )

        documents = text_splitter.create_documents([data])
        db = FAISS.from_documents(documents, embeddings)
        db.save_local("research_db")

    else:
        embeddings = HuggingFaceEmbeddings()
        db = FAISS.load_local("research_db", embeddings)
    return db