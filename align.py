import requests
import json
import sys
import argparse

api_url = "https://dharmamitra.org/api-aligner/align-full-sentences/"

def read_file_to_list(file_path):
    """
    Reads a text file and splits it into a list of sentences based on newlines.
    
    Args:
    file_path (str): The path to the text file.
    
    Returns:
    List[str]: A list of sentences.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        sentences = content.splitlines()
    return sentences

def send_request_to_api(sentences_a, sentences_b, api_url):
    """
    Sends the lists of sentences to the API for alignment and returns the response.
    
    Args:
    sentences_a (List[str]): The first list of sentences.
    sentences_b (List[str]): The second list of sentences.
    api_url (str): The URL of the API endpoint.
    
    Returns:
    dict: The JSON response from the API containing aligned sentence pairs.
    """
    payload = {
        "sentences_a": sentences_a,
        "sentences_b": sentences_b
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()  # Raise an error if the request failed
    
    return response.json()

def write_aligned_sentences_to_tsv(aligned_sentences, output_file_path):
    """
    Writes the aligned sentences to a TSV file.
    
    Args:
    aligned_sentences (List[dict]): A list of aligned sentence pairs.
    output_file_path (str): The path to the output TSV file.
    """
    with open(output_file_path, "w", encoding="utf-8") as file:
        for pair in aligned_sentences:
            file.write(f"{pair['sentence_a']}\t{pair['sentence_b']}\n")

def main(input_a, input_b, output_file):
    """
    Main function to read input files, send data to the API, and write the output to a TSV file.
    
    Args:
    input_a (str): Path to the first input text file. Make sure that each line contains a separate sentence.
    input_b (str): Path to the second input text file. Make sure that each line contains a separate sentence.    
    output_file (str): Path to the output TSV file.
    """
    # Read the input files into lists of sentences
    sentences_a = read_file_to_list(input_a)
    sentences_b = read_file_to_list(input_b)
    
    # Send the lists of sentences to the API for alignment
    print("Sending request to the API, waiting for aligned results...")
    response_json = send_request_to_api(sentences_a, sentences_b, api_url)
    print("Received response from the API.")
    # Extract the aligned sentences from the response
    aligned_sentences = response_json["aligned_sentences"]
    print(f"Received {len(aligned_sentences)} aligned sentence pairs.")
    # Write the aligned sentences to a TSV file
    print(f"Writing aligned sentences to {output_file}...")
    write_aligned_sentences_to_tsv(aligned_sentences, output_file)
    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Align sentences from two text files using an API and save the result to a TSV file.")
    parser.add_argument("--input-a", required=True, help="Path to the first input text file. Each line should be a separate sentence.")
    parser.add_argument("--input-b", required=True, help="Path to the second input text file. Each line should be a separate sentence.")
    parser.add_argument("--output", required=True, help="Path to the output TSV file.")

    args = parser.parse_args()
    
    main(args.input_a, args.input_b, args.output)
