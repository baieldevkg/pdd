import base64
from fastapi import APIRouter, UploadFile, File, HTTPException
from mysite.chain.Pdd import pdd_chain
from mysite.database.schemas import TrafficSign

pdd_router = APIRouter(prefix='/pdd', tags=['PDD'])


@pdd_router.post('/analyze', response_model=TrafficSign)
async def analyze_sign(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail='Нужно отправить изображение')

    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return await pdd_chain.ainvoke({'image_base64': image_base64})