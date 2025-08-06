from backend.app.database import Base, engine
from backend.app.models import user  # später auch weitere models importieren

print("📦 Erstelle Datenbank...")
Base.metadata.create_all(bind=engine)
print("✅ Datenbank erfolgreich erstellt.")