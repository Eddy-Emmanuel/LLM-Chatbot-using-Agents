from agent_1 import llm_model

from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader


def AGENT_2(url):
    if "youtube.com" in url:
        url_loader = YoutubeLoader.from_youtube_url(youtube_url=url)
    else:
        url_loader = UnstructuredURLLoader(urls=[url])
    
    url_doc = url_loader.load()

    txt_splitter = RecursiveCharacterTextSplitter()

    splitted_doc = txt_splitter.split_documents(url_doc)

    summary_chain = load_summarize_chain(llm=llm_model, chain_type="refine")

    return summary_chain.invoke(splitted_doc)["output_text"]


# print(AGENT_2("https://www.youtube.com/shorts/3qrMUZcZ4RQ"))