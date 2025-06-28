import os
import asyncio
import logging
import json
from uuid import uuid4
from pydub import AudioSegment
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
)

# 🔐 Load secrets from Replit environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_PROJECT = os.getenv("OPENAI_PROJECT")
MEMORY_PATH = "memory"

client = OpenAI(api_key=OPENAI_API_KEY, project=OPENAI_PROJECT)
logging.basicConfig(level=logging.INFO)

user_personas = {}
user_histories = {}

def load_memory(user_id):
    os.makedirs(MEMORY_PATH, exist_ok=True)
    path = os.path.join(MEMORY_PATH, f"{user_id}.json")
    if os.path.exists(path
