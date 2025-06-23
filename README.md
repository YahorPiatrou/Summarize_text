## Project information
This project is designed to obtain a summary of the text entered manually or contained in a file. The summarization process is carried out using the BART (Bidirectional & AutoRegressive Transformer) and Mistral models (through Together API).

## Repository content
The project repository contains the following files:
- `models.py` — this file contains the project functionality, with the help of which the text is summarized, as well as reading text from a file;
- `app.py` — this file is the entry point of the project, containing the code for building a web application using the gradio library;
- `.gitattributes` — configuration file git, created automatically when the repository was initialized. Doesn't store important information, can be deleted;
- `__pycache__` — system folder python which contains .pyc files created during the execution of scripts;
- `requirements.txt` — a text file that contains a list of all dependencies (packages & libraries) required for the project to work;
- `README.md` — description of the project and used technologies.

## How it works
Interaction between the user and the system occurs through a web application written using the gradio library. The application interface contains the following interaction elements:
- Text input field;
- Add file button;
- Button to select a model to perform the summarization task. Contains 2 options to choose: BART and Mistral;
- Button to clear the entered text or attached file;
- Field for displaying execution results.

After entering text or attaching a file, user selects a model with which the summarization task will be performed. After waiting for some time, the user will see the result in the corresponding field of the web application interface. After receiving the result, it is possible to clear the input data using the corresponding button.

## Instructions for launching the project

1. First, you need to install the libraries used in the project. In the console, you need to enter the following command (while in the project area):

```bash
pip install -r requirements.txt
```

2. After installing the libraries, you can proceed to launching the project. While in the project workspace, you need to run the following command:

```bash
python app.py
```

3. After entering the command described above, the following message will be displayed in the console:
> Running on local URL:  http://127.0.0.1:7860

By clicking on the link from the response (in its console) the user will see the web application interface.

4. After opening the application interface, the user will be able to enter their text manually in the appropriate field or attach a file. Then it is necessary to select the model with which the summation will take place (default value — BART).

5. After waiting for some time, user will see the result.

## Example of work
The following text was fed to the models as input:
> In a quiet village nestled between green hills and vast meadows, life moved slowly. Children played near the riverbanks, elders gathered under ancient trees to share
> stories, and farmers worked their fields from dawn until dusk. It was a place where everyone knew each other, and every face carried a memory.
> One day, a stranger arrived—a tall man with a worn leather bag and eyes that held the weight of many roads. He spoke little, yet listened carefully. The villagers, curious but cautious, watched him as he helped repair the school’s broken roof and shared bread with the poorest family in town. Slowly, trust formed.
> As days turned into weeks, the stranger became part of the village’s rhythm. He taught the children stories from faraway lands, helped build stronger bridges over the stream, and reminded everyone of the power of kindness. But he never spoke of his past.
> One morning, he was gone. No farewell, no explanation. Only the repaired village, a letter left on the school’s doorstep, and memories that would last for years. In the
> letter, he wrote:
> "Sometimes, healing happens in silence. Thank you for giving me peace."
> The villagers never saw him again, but his presence remained — in the way they greeted newcomers, helped one another, and believed in quiet transformations.

**Result from the BART model:**
>In a quiet village, a stranger arrived with a worn leather bag and eyes that held the weight of many roads. He helped repair the school’s broken roof and shared bread with
>the poorest family in town. He taught the children stories from faraway lands, helped build stronger bridges over the stream, and reminded everyone of the power of kindness.


**Result from the Mistral model:**
>A stranger, a tall man with a worn leather bag, arrived in a peaceful village nestled between hills and meadows. He helped repair the school and shared bread with the
>needy, gradually earning the villagers' trust. Over time, he became an integral part of the community, teaching stories, building bridges, and promoting kindness. He never
>revealed his past and one morning, he vanished without a trace.
