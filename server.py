import os
import core
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import io
import requests

ngrok_token = "2ST8bvXhOYVVsUKv1qe1jOnqgNW_5N8Pt75i32ijBJh3NDcNJ"
port = 8000

if __name__ == '__main__':

    ngrok.set_auth_token(ngrok_token)
    public_url = ngrok.connect(port).public_url
    print("Public URL:", public_url)
    nest_asyncio.apply()
    config = uvicorn.Config("core.asgi:application", port=port, log_level="info")
    server = uvicorn.Server(config)
    server.run()
    

