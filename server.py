import os
import core
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR,".env"))

ngrok_token = os.getenv('ngrok_token')
port = 8000


if __name__ == '__main__':

    ngrok.set_auth_token(ngrok_token)
    public_url = ngrok.connect(port).public_url
    print("Public URL:", public_url)
    nest_asyncio.apply()
    config = uvicorn.Config("core.asgi:application", port=port, log_level="info")
    server = uvicorn.Server(config)
    server.run()
    

