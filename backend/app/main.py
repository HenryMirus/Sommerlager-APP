from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import deiner Router
from backend.app.routes import (
    auth_routes,
    user_routes,
    sommerlager_routes,
    group_routes,
    bank_account_routes,
    kiosk_routes,
    document_routes,
    photo_routes
)

app = FastAPI(
    title="KjG Sommerlager-APP",
    description="Verwaltung für Kinder, Betreuer, Banking und Kiosk im Sommerlager.",
    version="0.0.1"
)

# Statische Dateien (CSS, JS, Bilder)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# HTML-Templates (Jinja2)
templates = Jinja2Templates(directory="frontend/templates")


# Startroute: Dashboard oder Login-Seite
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/user", response_class=HTMLResponse)
async def read_user(request: Request):
    return templates.TemplateResponse("Benutzerverwaltung.html", {"request": request})


# Router registrieren
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/user", tags=["Users"])
app.include_router(sommerlager_routes.router, prefix="/lager", tags=["Sommerlager"])
app.include_router(group_routes.router, prefix="/groups", tags=["Gruppen"])
app.include_router(bank_account_routes.router, prefix="/bank", tags=["Banking"])
app.include_router(kiosk_routes.router, prefix="/kiosk", tags=["Kiosk"])
app.include_router(document_routes.router, prefix="/documents", tags=["Dokumente"])
app.include_router(photo_routes.router, prefix="/photos", tags=["Fotos"])


# Starten via: `python main.py` (für Dev-Modus auf dem Raspberry Pi)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
