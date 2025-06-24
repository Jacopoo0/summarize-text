# Text Analysis Services with FastAPI and HuggingFace

This project provides a simple web service for text analysis, including summarization and sentiment analysis, using FastAPI and HuggingFace Transformers.

## Folder Structure

```
huggingface/
│
├── main.py                  # Main FastAPI application
├── requirements.txt         # Required Python dependencies
└── templete/
    ├── index.html           # Main page with input form
    └── summary.html         # Result display page
```

## Requirements

- Python 3.8+
- The dependencies listed in `requirements.txt`:
  - fastapi
  - transformers
  - jinja2
  - uvicorn

## Installation

1. **Clone the repository or copy the files into your working directory.**
2. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Server

To start the FastAPI server, run:

```sh
uvicorn main:app --reload
```

The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## How It Works

1. **Access the Home Page:**  
   Go to `http://127.0.0.1:8000` to see the main page (`index.html`), where you can enter the text to analyze and select the service type (summarization or sentiment analysis).

2. **Submit Text:**  
   After entering your text and selecting the service, click "Submit". The form sends a POST request to `/summary`.

3. **Processing:**  
   - If you select "Summarization", the HuggingFace pipeline is used to generate a summary of the text.
   - (To be implemented: if you select "Sentiment Analysis", sentiment analysis will be performed.)

4. **Result:**  
   The result is displayed on a new page (`summary.html`).

## Notes

- You can add more services by modifying the logic in `main.py` and updating the HTML templates.
- Make sure the `templete` folder is spelled correctly and contains the necessary HTML files.

## Example requirements.txt

```
fastapi
transformers
jinja2
uvicorn
```

---


