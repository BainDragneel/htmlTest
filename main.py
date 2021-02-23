import uvicorn
from app import create_app
from app.route import create_route

app = create_app()
create_route(app)

if __name__ == "__main__":
    uvicorn.run(app)
