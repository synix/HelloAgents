import os
from dotenv import load_dotenv
import torch
from hello_agents.memory.embedding import create_embedding_model

load_dotenv()

def test_dashscope_embedding():
    dashscope_embedding = create_embedding_model(
        model_type="dashscope",
        model_name="text-embedding-v3",
        api_key=os.getenv("EMBED_API_KEY"),
        base_url=os.getenv("EMBED_BASE_URL")
    )

    print(f"dashscope_embedding.dimension: {dashscope_embedding.dimension}")

    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium",
    ]

    embeddings = dashscope_embedding.encode(texts=sentences)
    print(f"embeddings: {embeddings}")
    embedding_tensor = torch.tensor(embeddings, dtype=torch.float32)

    similarities = torch.cosine_similarity(
        embedding_tensor.unsqueeze(1),  # [n, 1, d]
        embedding_tensor.unsqueeze(0),  # [1, n, d]
        dim=2  # 在最后一维计算相似度
    )

    print("✅ similarities:\n ", similarities)

def test_local_sentence_transformers_embedding():
    local_embedding = create_embedding_model(
        model_type="local",
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )

    print(f"local_embedding.dimension: {local_embedding.dimension}")

    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium",
    ]

    embeddings = local_embedding.encode(texts=sentences)
    print(f"embeddings: {embeddings}")
    embedding_tensor = torch.tensor(embeddings, dtype=torch.float32)

    similarities = torch.cosine_similarity(
        embedding_tensor.unsqueeze(1),  # [n, 1, d]
        embedding_tensor.unsqueeze(0),  # [1, n, d]
        dim=2  # 在最后一维计算相似度
    )

    print("✅ similarities:\n ", similarities)


def test_local_huggingface_embedding():
    local_embedding = create_embedding_model(
        model_type="huggingface",
        model_name="bert-base-uncased",
    )

    print(f"local_embedding.dimension: {local_embedding.dimension}")

    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium",
    ]

    embeddings = local_embedding.encode(texts=sentences)
    print(f"embeddings: {embeddings}")
    embedding_tensor = torch.tensor(embeddings, dtype=torch.float32)

    similarities = torch.cosine_similarity(
        embedding_tensor.unsqueeze(1),  # [n, 1, d]
        embedding_tensor.unsqueeze(0),  # [1, n, d]
        dim=2  # 在最后一维计算相似度
    )

    print("✅ similarities:\n ", similarities)


def test_tfidf_embedding():
    tfidf_embedding = create_embedding_model(
        model_type="tfidf",
    )

    print(f"local_embedding.dimension: {tfidf_embedding.dimension}")

    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium",
    ]

    embeddings = tfidf_embedding.encode(texts=sentences)
    print(f"embeddings: {embeddings}")
    embedding_tensor = torch.tensor(embeddings, dtype=torch.float32)

    similarities = torch.cosine_similarity(
        embedding_tensor.unsqueeze(1),  # [n, 1, d]
        embedding_tensor.unsqueeze(0),  # [1, n, d]
        dim=2  # 在最后一维计算相似度
    )

    print("✅ similarities:\n ", similarities)


if __name__ == "__main__":
    test_dashscope_embedding()
    test_local_sentence_transformers_embedding()
    test_local_huggingface_embedding()
    # 会报错: "TF-IDF模型未训练，请先调用fit()方法"
    # test_tfidf_embedding()
    