from fastapi import FastAPI, UploadFile, File

import numpy as np
import torch
import torchvision

from app.pipeline_classify import run_classification

app = FastAPI()

@app.post("/classify-bottle/")
async def classify_bottle(file: UploadFile = File(...)):
    
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    nparr = torch.from_numpy(nparr)

    img = torchvision.io.decode_png(nparr)[:3]

    out = run_classification(img)
    
    return out
