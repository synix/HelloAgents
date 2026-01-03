import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

def create_qdrant_client():
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")

    client = QdrantClient(
        url=qdrant_url, 
        api_key=qdrant_api_key,
    )

    return client

if __name__ == "__main__":
    client = create_qdrant_client()
    print("创建qdrant client后, collections: ", client.get_collections())
    print("qdrant default embedding model: ", client.DEFAULT_EMBEDDING_MODEL)

    # Prepare your documents, metadata, and IDs
    docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
    metadata = [
        {"source": "Langchain-docs"},
        {"source": "Linkedin-docs"},
    ]
    ids = [42, 2]

    # Use the new add method
    client.add(
        collection_name="demo_collection",
        documents=docs,
        metadata=metadata,
        ids=ids
    )

    search_result = client.query(
        collection_name="demo_collection",
        query_text="What integrations does Qdrant support?",
        limit=2
    )

    print(search_result)