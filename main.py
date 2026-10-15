from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates #  Templates 
from fastapi import Request # Templates 
from fastapi import Form #portal.html (tüm HTML,POST,GET) .

# PROJECT START
# python3 -m venv .venv
# source .venv/bin/activate
# pip install fastapi "uvicorn[standard]" jinja2 python-multipart


#-----------------------------------------------------------------------------------------------------------
# FastAPI()     → Uygulamamızı oluşturuyor.
# @app.get("/") → Ana adresimize (/) gelen GET isteğini bu fonksiyona yönlendiriyor.
# ana_sayfa()   → Python fonksiyonumuz; yanıtı hazırlıyor.
# return        → FastAPI, sözlüğü JSON yanıtına dönüştürüyor.

# uvicorn main:app --reload      Terminale çalıştır , main.py dosyası; app ise dosyanın içindeki app = FastAPI() nesnesi.
# Sunucu açılırsa tarayıcıda http://127.0.0.1:8000 adresine git.


app = FastAPI()
templates = Jinja2Templates(directory="templates") 


@app.get("/") 
def ana_sayfa():
    return {"mesaj": "Mini IT Portalımıza hoş geldin!"}



@app.get("/portal") # GET → Sayfayı açar, formu gösterir.
def portal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="portal.html",
        context={}
    )


@app.post("/portal") # POST → Formu gönderir, gelen veriyi işler.
def talep_gonder(
    request: Request,
    talep_basligi: str = Form(...),
    aciklama: str = Form(...)
):
    return templates.TemplateResponse(
        request=request,
        name="portal.html",
        context={
                "baslik": "Mini IT Destek Portalı",
                "kullanici": "Kral",
                "mesaj": f"Talebin alındı: {talep_basligi} — {aciklama}",
                "talep_basligi": talep_basligi,
                "aciklama": aciklama
                }
    )
