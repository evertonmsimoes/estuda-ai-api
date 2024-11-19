from dotenv import load_dotenv
import os

load_dotenv(".env.local")

gptApiKey = os.getenv("gptApiKey")
