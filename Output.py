from setup import tokenizer_model, generator_model


def generate_answer(query):
    """
    Function takes a query as input, tokenizes it, and generates
    an answer using a pre-trained model.

    Args:
        query (str): string containing the query to be answered.

    Returns:
        answer (str): string containing the generated answer to the query.
    """
    # Tokenize the query
    inputs = tokenizer_model([query], max_length=1024,
                             return_tensors="pt", truncation=False)

    # Use generator to predict output ids
    ids = generator_model.generate(
        inputs["input_ids"], num_beams=1, min_length=5, max_length=40)

    # Use tokenizer to decode the output ids
    answer = tokenizer_model.batch_decode(
        ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return answer
