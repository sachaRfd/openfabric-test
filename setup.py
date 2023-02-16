from transformers import BartTokenizer, BartForConditionalGeneration
import pinecone
from sentence_transformers import SentenceTransformer


# Checknotebook for how I implemented the
retriever_model = SentenceTransformer(
    "flax-sentence-embeddings/all_datasets_v3_mpnet-base")


# Connect to Pinecone:
pinecone.init(
    api_key="64661917-e6c9-41c5-a4bf-bfcca4c85091",
    environment="us-east1-gcp"
)

# connect to science-bot index we created
index_name = 'science-bot'
index = pinecone.Index(index_name)


# load bart tokenizer and model from huggingface
tokenizer_model = BartTokenizer.from_pretrained('vblagoje/bart_lfqa')
generator_model = BartForConditionalGeneration.from_pretrained(
    'vblagoje/bart_lfqa')
