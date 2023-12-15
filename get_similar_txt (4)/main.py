from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import get_txt 
import PnP_hack as hack_main
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Base_url(BaseModel):
    url: str
    url_domain: str | None = None


class Query_url(BaseModel):
    query: str
    url_domain: str | None = None

@app.post("/get_txt")

async def root(request_body:Base_url):
    try:
        url = request_body.url
        # url_domain = request_body.url_domain
        url_domain = "webDataText"
        # print("---url---",url)
        # print("---url_domain---",url_domain)
        get_txt.extract_save_txt(url,url_domain)
        return {"statusCode":200,"message": "Successfully Extracted text"}
    except Exception as err:
        print("---error----",str(err))
        return {"statusCode":500,"message": "Internal Server error"}
    
@app.post("/query")
async def root(request_body:Query_url):
    try:
        query = request_body.query
        # url_domain = request_body.url_domain
        url_domain = "webDataText"

        response = hack_main.get_ai_response(url_domain,query)
        return {"statusCode":200,"message": response}
    except Exception as err:
        print("---error----",str(err))
        return {"statusCode":500,"message": "Internal Server error"}
    
app.mount("/static", StaticFiles(directory="Chatbot"), name="static")
if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=3000, reload=True, workers=3)