import pinecone


# Connect to Pinecone:
pinecone.init(
    api_key="64661917-e6c9-41c5-a4bf-bfcca4c85091",
    environment="us-east1-gcp"
)

# connect to science bot index in Pinecode (created manually by me):
index_name = "science-bot"
index = pinecone.Index(index_name)
