## Project information
This project is designed to obtain a summary of the text entered manually or contained in a file. The summarization process is carried out using the BART (Bidirectional & AutoRegressive Transformer) and Mistral models (through Together API).

## Repository content
The project repository contains the following files:
- `models.py` — this file contains the project functionality, with the help of which the text is summarized, as well as reading text from a file;
- `app.py` — this file is the entry point of the project, containing the code for building a web application using the gradio library;
- `.gitattributes` — configuration file git, created automatically when the repository was initialized. Doesn't store important information, can be deleted;
- `__pycache__` — system folder python which contains .pyc files created during the execution of scripts;
- `README.md` — description of the project and used technologies.

## How it works
Interaction between the user and the system occurs through a web application written using the gradio library. The application interface contains the following interaction elements:
- Text input field;
- Add file button;
- Button to select a model to perform the summarization task. Contains 2 options to choose: BART and Mistral;
- Button to clear the entered text or attached file;
- Field for displaying execution results.



[needs improvement]
