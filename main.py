from transformers import pipeline
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templete")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/summary", response_class=HTMLResponse)
def summary(request: Request, input_text: str = Form(...), service_type: str = Form(...) ):
    if service_type == "summary":
        generator = pipeline("summarization")
        riassunto = generator(input_text)
        return templates.TemplateResponse(request=request, name="summary.html", context={'summary': riassunto[0]["summary_text"]})
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)


