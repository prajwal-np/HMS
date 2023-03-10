from main import create_server
import uvicorn

app = create_server()

if __name__ == "__main__":
    config = uvicorn.Config("main:create_server",reload=True)
    server = uvicorn.Server(config)
    server.run()