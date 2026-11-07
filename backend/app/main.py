from fastapi import FastAPI

app = FastAPI(
    title="Sistema de Asistencia Laboral Mediante Reconocimiento Facial con Redes Siamesas y Analítica de Comportamiento de Asistencia",
    docs_url="/docs"
)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Sistema de Asistencia Laboral", "docs": "/api/docs"}

@app.get("/api/health")
def health():
    return {"estado": "ok"}

