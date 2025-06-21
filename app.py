import gradio as gr # package for build web application

# function from the models.py for summarize text 
# and read contents from the file with pdf, docx, txt extensions
from models import Summarize_with_BART, Summarize_with_Mistral, Read_text_from_file 

# function for summarize text (from a file or from the entered text)
def Summarize_text(text: str, file: str, model_choice: str) -> str:
    """
    This function accepts text written in a text field or in an attached file; 
    in case both are done, the document is given preference.

    Args:
        text (str): Text entered into the form in the appropriate field (if any);
        file (str): Name of the attached file (if any);
        model_choice (str): Model chosen by the user.

    Returns:
        summary (str): Summary of the text.
    """
    
    # if a document is attached, read its contents using the function
    if file is not None:
        text = Read_text_from_file(file)
    
    # use the model according to the user's choice
    if model_choice == "BART":
        return Summarize_with_BART(text)
    elif model_choice == "Mistral":
        return Summarize_with_Mistral(text)
    
# build gradio interface
interface = gr.Interface(
    fn=Summarize_text, # function to call when the user submits
    inputs=[
        gr.Textbox(placeholder="Enter text"), # textbox for text input
        gr.File(label="Add File", type="filepath"), # option to upload a text file
        gr.Dropdown( # dropdown menu to select the summarization model
            choices=["BART", "Mistral"], # selection options
            label="Choose Model", # menu name
            value="BART" # default value
        )
    ],
    outputs="text", # output will be displayed as text
    title="Summarize Text", # title of the app
    description="Paste text or attach a file, select model, then click Submit", # explanation of how the application works
    allow_flagging="never" # disable the flagging feature (button "flag")
)

# run the gradio app
if __name__ == "__main__":
    interface.launch()
