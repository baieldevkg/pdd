from fastapi import FastAPI
import uvicorn
from mysite.api import pdd

app = FastAPI(title='TraficSign')

app.include_router(pdd.pdd_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)