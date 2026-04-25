from fastapi import FastAPI

app = FastAPI()


@app.get("/api/admin/public-org-dump")
def public_admin_dump():
    # Intentionally insecure for demo only.
    return {"warning": "This endpoint is intentionally public and insecure."}
