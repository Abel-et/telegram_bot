import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from google import genai

# Enable logging to see errors in the VS Code console
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
print('started')
# 🔴 PASTE YOUR API TOKENS HERE
TELEGRAM_BOT_TOKEN = "8917011782:AAFDRUmmC0WlLVvY7NmiWCL6S0-RVjJTcAQ"
GEMINI_API_KEY = "AQ.Ab8RN6JPMrlzFja6FnA2bt4umzal-DzV27GgHqNVnx0OVBV_MQ"

# Initialize the official Gemini Client
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Hello! I am your Gemini AI assistant. Ask me anything, and I will answer!"
    )

# Message handler to process incoming texts and query Gemini
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    logging.info(f"User sent: {user_text}")
    
    # Send a typing indicator so the user knows the AI is thinking
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    try:
        # Request a response from Gemini (using the fast and capable gemini-2.5-flash)
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_text,
        )
        
        # Send the AI response back to Telegram
        await update.message.reply_text(response.text)
        
    except Exception as e:
        logging.error(f"Error calling Gemini API: {e}")
        await update.message.reply_text("❌ Sorry, I encountered an error while processing your request.")

def main():
    # Build the Telegram Bot application
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register handlers 36316503
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling Telegram for messages
    print("🚀 Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
if __name__ == "__main__":
    print("🔄 Attempting to launch the main function...")
    try:
        main()
    except Exception as error:
        print(f"❌ CRITICAL ERROR OCCURRED: {error}")
