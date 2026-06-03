from fastapi import FastAPI
from .routes import router
import uvicorn

# fastAPI app instance - contains: settings, middleware, endpoints
# app that uvicorn serves
app = FastAPI()

# Include the router instance from routes.py into app
app.include_router(router)

# Run the dev ASGI server on localhost when main.py is run
if __name__ == "__main__":
  print(f"Welcome to arcvault version 1.0.0")
  uvicorn.run("src.app.main:app", host = "0.0.0.0", port = 8000, reload = True)