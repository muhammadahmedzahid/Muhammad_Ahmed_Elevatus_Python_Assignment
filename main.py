import uvicorn
# http://localhost:8081/docs It will generate the swagger UI
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)