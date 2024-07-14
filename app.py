import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import User
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging to save to a file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='bot_info.log',
                    filemode='w')
logger = logging.getLogger(__name__)

async def get_bot_info(bot: Bot) -> User:
    try:
        bot_info = await bot.get_me()
        return bot_info
    except Exception as e:
        logger.error("An error occurred while fetching bot info: %s", e)
        raise

async def main():
    if not BOT_TOKEN:
        logger.error("Bot token not found. Please set the BOT_TOKEN environment variable.")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    
    try:
        bot_info = await get_bot_info(bot)
        logger.info("Bot ID: %s", bot_info.id)
        logger.info("First Name: %s", bot_info.first_name)
        logger.info("Username: %s", bot_info.username)
        logger.info("Can Join Groups: %s", bot_info.can_join_groups)
        logger.info("Can Read All Group Messages: %s", bot_info.can_read_all_group_messages)
        logger.info("Supports Inline Queries: %s", bot_info.supports_inline_queries)
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
