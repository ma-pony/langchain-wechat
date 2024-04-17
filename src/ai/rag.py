from typing import Literal

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pydantic.v1 import BaseModel, Field

from config import Settings

embeddings = OpenAIEmbeddings()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]
documents_topics = "agent, prompt-engineering, adv-attack-llm"

# load web documents
web_docs = [WebBaseLoader(url).load() for url in urls]
docs = [item for doc in web_docs for item in doc]

# split text into characters
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=512, chunk_overlap=0)
docs_splits = text_splitter.split_documents(docs)

# add embeddings to the vector store
vectorstore = Chroma.from_documents(
    documents=docs_splits,
    collection_name="langchain-wechat",
    embeddings=embeddings,
)
retriever = vectorstore.as_retriever()


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "web_search"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a " "vectorstore.",
    )


llm = ChatOpenAI(
    model=Settings.OPENAI_MODEL,
    temperature=0,
)
structured_llm_router = llm.with_structured_output(RouteQuery)

system_role_prompt = f"""
You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to {documents_topics}.
Use the vectorstore for questions on these topics.
Otherwise, use web search.
"""

prompt = ChatPromptTemplate.from_messages([("system", system_role_prompt), ("human", "{query}")])

question_router = prompt | structured_llm_router
