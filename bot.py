import logging
import random
import json
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Barzellette integrate nel codice
JOKES = {
    "carabinieri": [
        "Due carabinieri si trovano su una barca che sta affondando. Uno dice all'altro: 'Che facciamo?' E l'altro: 'Semplice, spegniamo il motore!'",
        "Un carabiniere va dal dottore e dice: 'Dottore, ho l'influenza!' Il dottore: 'Da quanto tempo?' Il carabiniere: 'Da quando sono nato!'",
        "Perché i carabinieri non usano l'aspirina? Perché non riescono a farla entrare nella bottiglia!",
        "Un carabiniere trova una bottiglia sulla spiaggia. La strofina ed esce un genio che gli dice: 'Esprimi tre desideri!' Il carabiniere: 'Vorrei essere intelligente!' Il genio: 'Fatto! Ora hai due desideri!'",
        "Due carabinieri guardano le impronte sulla neve. Uno dice: 'Sono di lupo!' L'altro: 'No, di orso!' Arriva il maresciallo: 'Ma cosa fate?' 'Seguiamo le impronte!' 'Ma quelle sono le vostre!'"
    ],
    "scuola": [
        "La maestra chiede: 'Pierino, dimmi una frase con il predicato nominale.' Pierino: 'Maestra, il cane abbaia.' La maestra: 'No Pierino, quello è predicato verbale!' Pierino: 'Ah, allora: il cane si chiama Fido!'",
        "La professoressa di geografia chiede: 'Dove si trova l'America?' Pierino: 'A pagina 35!'",
        "Pierino torna a casa con la pagella. Il papà: 'Pierino, hai preso 2 in matematica!' Pierino: 'Papà, non è colpa mia, la maestra mi ha chiesto quanto fa 3x3 e io ho risposto 9!' 'Ma è giusto!' 'Eh, ma poi mi ha chiesto quanto fa 9x9!'",
        "'Pierino, coniuga il verbo camminare.' 'Io cammino, tu cammini, egli cammina...' 'Più veloce!' 'Io corro, tu corri, egli corre!'",
        "La maestra: 'Pierino, dimmi il nome di cinque cose che contengono latte.' Pierino: 'Il formaggio, il burro, il gelato e... e... due mucche!'"
    ],
    "animali": [
        "Cosa dice un pesce quando sbatte contro il muro? DIGA!",
        "Perché i pesci non giocano a tennis? Perché hanno paura della rete!",
        "Due pulci escono dal cinema. Una dice all'altra: 'Andiamo a piedi o prendiamo un cane?'",
        "Cosa fa un gatto in un negozio di computer? Caccia i mouse!",
        "Perché le api hanno i capelli appiccicosi? Perché usano il miele gel!",
        "Un pesce va dallo psicologo e dice: 'Dottore, credo di avere un complesso!' Il dottore: 'Quale?' Il pesce: 'Quello di Nemo!'",
        "Due gatti si incontrano. Uno dice: 'Miao!' L'altro: 'Bau!' Il primo: 'Ma sei impazzito?' Il secondo: 'No, sto studiando le lingue straniere!'"
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    welcome_message = """🍒 **Benvenuto in BarzCerry!** 🍒

Il bot delle barzellette più dolce di Telegram!

Comandi disponibili:
• /barz - Barzelletta casuale
• /carabinieri - Barzelletta sui carabinieri  
• /scuola - Barzelletta sulla scuola
• /animali - Barzelletta sugli animali
• /help - Mostra questo messaggio

Divertiti con BarzCerry! 😄🍒"""
    
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    await start(update, context)

async def get_random_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /barz - barzelletta casuale"""
    # Scegli categoria casuale
    category = random.choice(list(JOKES.keys()))
    joke = random.choice(JOKES[category])
    
    message = f"🍒 **BarzCerry - {category.title()}**\n\n{joke}\n\n💡 Prova anche: /carabinieri /scuola /animali"
    await update.message.reply_text(message, parse_mode='Markdown')

async def carabinieri_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Barzelletta sui carabinieri"""
    joke = random.choice(JOKES['carabinieri'])
    message = f"🍒 **BarzCerry - Carabinieri** 👮‍♂️\n\n{joke}\n\n🎲 Prova: /barz per una casuale!"
    await update.message.reply_text(message, parse_mode='Markdown')

async def scuola_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Barzelletta sulla scuola"""
    joke = random.choice(JOKES['scuola'])
    message = f"🍒 **BarzCerry - Scuola** 🎓\n\n{joke}\n\n🎲 Prova: /barz per una casuale!"
    await update.message.reply_text(message, parse_mode='Markdown')

async def animali_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Barzelletta sugli animali"""
    joke = random.choice(JOKES['animali'])
    message = f"🍒 **BarzCerry - Animali** 🐶\n\n{joke}\n\n🎲 Prova: /barz per una casuale!"
    await update.message.reply_text(message, parse_mode='Markdown')

def main():
    """Avvia BarzCerry"""
    # Token del bot
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN non trovato!")
        return
    
    # Crea applicazione
    application = Application.builder().token(TOKEN).build()
    
    # Aggiungi comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("barz", get_random_joke))
    application.add_handler(CommandHandler("carabinieri", carabinieri_joke))
    application.add_handler(CommandHandler("scuola", scuola_joke))
    application.add_handler(CommandHandler("animali", animali_joke))
    
    logger.info("🍒 BarzCerry è partito!")
    
    # Usa solo polling (semplice!)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()