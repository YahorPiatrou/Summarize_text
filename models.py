# import libraries
from transformers import BartTokenizer, BartForConditionalGeneration # classes to create a BART model
from pypdf import PdfReader # library for read pdf-files
from docx import Document # library for read docx-files
from os.path import splitext # function for getting file extension (txt, pdf or docx)
import requests # library for create HTTP requests

# function for summarize text with BART model    
def Summarize_with_BART(text: str) -> str:
    """
    Summarizing text using the BART model (facebook/bart-large-cnn).
    if the text is long, it is divided into chunks of 1024 tokens.
    With this approach, a summary of each chunk is made, 
    and then a summarization of all answers.
    
    Args:
        text (str): The input text to be summarized;

    Returns:
        summary (str): The summarized version of the input text.
    """
    
    MAX_CHUNK_SIZE = 1024 # constant value of maximum chunk size
    MODEL_NAME = "facebook/bart-large-cnn" # name of the model used
    
    # load BART tokenizer and BART model 
    tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
    model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
    
    # tokenize input text 
    inputs = tokenizer(text, return_tensors="pt", truncation=False)
    input_ids = inputs["input_ids"][0]
    
    # splitting tokens into chunks (maximum size in MAX_CHUNK_SIZE)
    chunks = [input_ids[i:i + MAX_CHUNK_SIZE][None, :] for i in range(0, len(input_ids), MAX_CHUNK_SIZE)]
    
    # creating an empty list where the summary of each chunk will be written
    summaries = []
    
    # summary of each chunk from the list above (chunks)
    for chunk in chunks:
        summary_ids = model.generate(
            chunk, # tensor of input tokens for summarizing
            max_length=200, # maximum number of tokens in the summary
            min_length=30, # minimum number of tokens in the summary
            num_beams=5, # number of candidate sequences to consider at step
            early_stopping=True # parameter that controls the stopping condition (for num_beams methods)
        )
        
        # decoding tokens back into a sequence of words
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # adding a summary of each chunk to the list
        summaries.append(summary)
        
        # summation of each summary in one sequence
        final_summary = " ".join(summaries)
    
    # if initially there was 1 chunk, we can return its summary, 
    # if there were several, we need to do another one summarize
    if (len(summaries)) == 1:
        return final_summary
    else:
        return Summarize_with_BART(final_summary) # recursively call the function for the compressed text
    
# function for summarize text with Mistral model 
def Summarize_with_Mistral(text: str) -> str:
    """
    Summarizes input text using the Mistral-7B-Instruct model with Together API.

    Args:
        text (str): The input text to be summarized;

    Returns:
        summary (str): The summarized version of the input text.
    """
    
    # API token for authentication for Together API
    TOKEN = "69eb52e0a388356b75b84904ec29a87e531d10d553e128665fc020f71b7858f8" 
    
    # endpoint for the Together API
    URL = "https://api.together.xyz/v1/chat/completions"
    
    # header of HTTP requests with authorization and content type
    header = {
        "Authorization": f"Bearer {TOKEN}", 
        "Content-Type": "application/json"
    }
    
    # body request sent to Mistral model with Together API
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.3",
        "messages": [
        {"role": "user", "content": f"Summarize the following text:\n{text}"}],
        "temperature": 0.7,
        "max_tokens": 100,
    }
    
    # send the POST request to the API and parse the JSON response (with .json() method)
    answer = requests.post(URL, json=data, headers=header).json()
    
    # return summary from the response 
    return answer["choices"][0]["message"]["content"]

# function to read text from file with pdf-docx-txt extensions
def Read_text_from_file(filename: str) -> str:
    """
    Reads and extracts text content from a file (with pdf, txt, docx formats).

    Args:
        filename (str): The name of the file from which the text will be extracted;

    Returns:
        text (str): Text contained in a document.
    """
    
    text = ""
    _, ext = splitext(filename) # get the file extension, function splitext return tuple of name and ext file
    
    # file extension is checked:
    # if file extension = '.txt'
    if ext == ".txt":
        with open(filename, 'r') as file: # open the file for reading
            text = file.read()  # read data from file
            
    # if file extension = '.pdf'        
    elif ext == ".pdf":
        reader = PdfReader(filename) # create a pdf reader object
        for page in reader.pages: # read pages from a pdf document (reading pages is related to the peculiarity of pdf documents)
            text += page.extract_text() # combine all pages
            
    # if file extension = '.docx' 
    elif ext == ".docx":
        doc = Document(filename) # load the docx file
        text = "\n".join([paragraphs.text for paragraphs in doc.paragraphs]) # extract text from each paragraph in the document
    else:
        raise ValueError("Unsupported file type (only txt, pdf, docx can be uploaded)") # raise an error if the file extension is not among the supported formats
    
    # return the combined extracted text
    return text 
