import os
from dotenv import load_dotenv
from fastembed import TextEmbedding
from hello_agents.memory.storage.qdrant_store import QdrantConnectionManager

load_dotenv()

def create_fastembed_vectors():
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium",
    ]

    metadata = [
        { "topic": "weather" },
        { "topic": "weather" },
        { "topic": "life" },
    ]

    ids = [101, 102, 103]

    embedding_model = TextEmbedding()
    embeddings_list = list(embedding_model.embed(documents=sentences))

    print(len(embeddings_list))
    print(embeddings_list[0].shape)
    return embeddings_list, metadata, ids

def create_qdrant_conn_manager():
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    qdrant_conn_manager = QdrantConnectionManager.get_instance(
        url=qdrant_url,
        api_key=qdrant_api_key,
    )

    qdrant_stats = qdrant_conn_manager.get_collection_stats()
    print("✏️ qdrant stats:", qdrant_stats)

    qdrant_connection_info = qdrant_conn_manager.get_collection_info()
    print("✒️ qdrant connection info:", qdrant_connection_info)
    
    embedding_size = qdrant_conn_manager.client.get_embedding_size(
        qdrant_conn_manager.client.DEFAULT_EMBEDDING_MODEL
    )

    print("📒 qdrant default embedding model dimension:", embedding_size)

    return qdrant_conn_manager


if __name__ == "__main__":
    qdrant_conn_manager = create_qdrant_conn_manager()
    vectors, metadata, ids = create_fastembed_vectors()
    # qdrant_conn_manager.add_vectors(vectors=vectors, metadata=metadata, ids=ids)

    for i, vec in enumerate(vectors):
        search_results = qdrant_conn_manager.search_similar(vec, limit=3)
        print(f"🚀 Search results for vector {i}:\n", search_results)