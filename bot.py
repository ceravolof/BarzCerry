import logging
import random
import json
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class JokeBot:
    def __init__(self):
        self.jokes = self.load_jokes()
    
    def load_jokes(self):
        """Carica le barzellette dal file JSON"""
        try:
            with open('jokes.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("File jokes.json non trovato!")
            return {"carabinieri": [], "scuola": [], "animali": []}
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        welcome_message = """
🍒 **Benvenuto in BarzCerry!** 🍒

Il bot delle barzellette più dolce di Telegram!

Comandi disponibili:
• `/barz` - Barzelletta casuale
• `/carabinieri` - Barzelletta sui carabinieri
• `/scuola` - Barzelletta sulla scuola  
• `/animali` - Barzelletta sugli animali
• `/help` - Mostra questo messaggio

Divertiticon BarzCerry! 😄🍒
        """
        await update.message.reply_text(welcome_message, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /help"""
        await self.start(update, context)
    
    async def random_joke(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /barz - barzelletta casuale"""
        categories = list(self.jokes.keys())
        if not categories:
            await update.message.reply_text("❌ Nessuna barzelletta disponibile!")
            return
        
        # Scegli categoria casuale
        category = random.choice(categories)
        joke = self.get_joke_from_category(category)
        
        if joke:
            # Crea keyboard inline per altre barzellette
            keyboard = [
                [InlineKeyboardButton("🎲 Altra barzelletta", callback_data='random')],
                [
                    InlineKeyboardButton("👮‍♂️ Carabinieri", callback_data='carabinieri'),
                    InlineKeyboardButton("🎓 Scuola", callback_data='scuola'),
                    InlineKeyboardButton("🐶 Animali", callback_data='animali')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                f"🎭 **Categoria: {category.title()}**\n\n{joke}",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text("❌ Nessuna barzelletta trovata in questa categoria!")
    
    async def category_joke(self, update: Update, context: ContextTypes.DEFAULT_TYPE, category: str):
        """Barzelletta per categoria specifica"""
        joke = self.get_joke_from_category(category)
        
        if joke:
            keyboard = [
                [InlineKeyboardButton("🎲 Barzelletta casuale", callback_data='random')],
                [InlineKeyboardButton(f"🔄 Altra {category}", callback_data=category)]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                f"🎭 **{category.title()}**\n\n{joke}",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(f"❌ Nessuna barzelletta trovata per: {category}")
    
    def get_joke_from_category(self, category):
        """Ottieni una barzelletta casuale dalla categoria"""
        if category in self.jokes and self.jokes[category]:
            return random.choice(self.jokes[category])
        return None
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Gestisce i click sui bottoni inline"""
        query = update.callback_query
        await query.answer()
        
        category = query.data
        
        if category == 'random':
            # Barzelletta casuale
            categories = list(self.jokes.keys())
            if categories:
                selected_category = random.choice(categories)
                joke = self.get_joke_from_category(selected_category)
                
                keyboard = [
                    [InlineKeyboardButton("🎲 Altra barzelletta", callback_data='random')],
                    [
                        InlineKeyboardButton("👮‍♂️ Carabinieri", callback_data='carabinieri'),
                        InlineKeyboardButton("🎓 Scuola", callback_data='scuola'),
                        InlineKeyboardButton("🐶 Animali", callback_data='animali')
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.edit_message_text(
                    f"🎭 **Categoria: {selected_category.title()}**\n\n{joke}",
                    reply_markup=reply_markup,
                    parse_mode='Markdown'
                )
        else:
            # Categoria specifica
            joke = self.get_joke_from_category(category)
            if joke:
                keyboard = [
                    [InlineKeyboardButton("🎲 Barzelletta casuale", callback_data='random')],
                    [InlineKeyboardButton(f"🔄 Altra {category}", callback_data=category)]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.edit_message_text(
                    f"🎭 **{category.title()}**\n\n{joke}",
                    reply_markup=reply_markup,
                    parse_mode='Markdown'
                )
    
    # Handler per categorie specifiche
    async def carabinieri_joke(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.category_joke(update, context, 'carabinieri')
    
    async def scuola_joke(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.category_joke(update, context, 'scuola')
    
    async def animali_joke(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.category_joke(update, context, 'animali')

def main():
    """Avvia il bot"""
    # Token del bot (da variabile d'ambiente)
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN non trovato nelle variabili d'ambiente!")
        return
    
    # Crea l'applicazione
    application = Application.builder().token(TOKEN).build()
    
    # Inizializza il bot
    joke_bot = JokeBot()
    
    # Aggiungi gli handler
    application.add_handler(CommandHandler("start", joke_bot.start))
    application.add_handler(CommandHandler("help", joke_bot.help_command))
    application.add_handler(CommandHandler("barz", joke_bot.random_joke))
    application.add_handler(CommandHandler("carabinieri", joke_bot.carabinieri_joke))
    application.add_handler(CommandHandler("scuola", joke_bot.scuola_joke))
    application.add_handler(CommandHandler("animali", joke_bot.animali_joke))
    application.add_handler(CallbackQueryHandler(joke_bot.button_callback))
    
    # Avvia il bot
    logger.info("🍒 BarzCerry avviato!")
    
    # Usa webhook per Render (production) o polling per sviluppo
    PORT = int(os.getenv('PORT', 8443))
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    
    if WEBHOOK_URL:
        # Modalità webhook (per Render)
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=f"{WEBHOOK_URL}/webhook"
        )
    else:
        # Modalità polling (per sviluppo locale)
        application.run_polling()

if __name__ == '__main__':
    main()