from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

config = Config('.env')

oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=config('GOOGLE_CLIENT_ID'),
    client_secret=config('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
)

print(f"client_id : {config('GOOGLE_CLIENT_ID')}")
print(f"client_secret : {config('GOOGLE_CLIENT_SECRET')}")


@app.get("/")
async def root():
    return {"message": "Hello World"}
