from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.database import Base, engine
from api.routers import auth, workouts, rotines

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.state.port = 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check")
def check():
    return {"message": f"Check completed, server is running at port: {app.state.port}"}

app.include_router(auth.router)
app.include_router(workouts.router)
app.include_router(rotines.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=app.state.port, reload=True, app_dir='fastapi')
