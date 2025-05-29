# 🍒 BarzCerry - Bot Telegram per Barzellette

BarzCerry è il bot Telegram più dolce per barzellette! Racconta barzellette divertenti in tre categorie: carabinieri, scuola e animali.

## ✨ Funzionalità

- `/start` - Messaggio di benvenuto
- `/barz` - Barzelletta casuale con bottoni interattivi
- `/carabinieri` - Barzellette sui carabinieri
- `/scuola` - Barzellette sulla scuola
- `/animali` - Barzellette sugli animali
- `/help` - Mostra i comandi disponibili

## 🚀 Setup e Deploy su Render

### 1. Crea il Bot Telegram
1. Vai su [@BotFather](https://t.me/botfather) su Telegram
2. Invia `/newbot`
3. Scegli un nome e username per il bot
4. Salva il **token** che ricevi

### 2. Prepara il Repository
1. Crea un nuovo repository su GitHub
2. Carica tutti i file del progetto

### 3. Deploy su Render
1. Vai su [render.com](https://render.com) e registrati
2. Collega il tuo account GitHub
3. Crea un nuovo "Web Service"
4. Seleziona il repository del bot
5. Configura:
   - **Name**: telegram-joke-bot (BarzCerry)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

### 4. Configura le Variabili d'Ambiente
Aggiungi queste variabili in Render:
- `TELEGRAM_BOT_TOKEN`: Il token del tuo bot
- `WEBHOOK_URL`: L'URL del tuo servizio Render (es: https://telegram-joke-bot.onrender.com)
- `PORT`: 10000 (già configurato)

### 5. Test
Dopo il deploy, cerca il tuo bot su Telegram e prova i comandi!

## 🛠️ Sviluppo Locale

```bash
# Installa le dipendenze
pip install -r requirements.txt

# Crea file .env con il token
echo "TELEGRAM_BOT_TOKEN=tuo_token_qui" > .env

# Avvia il bot
python bot.py
```

## 📁 Struttura del Progetto

```
telegram-joke-bot/
├── bot.py              # Codice principale del bot
├── jokes.json          # Database delle barzellette
├── requirements.txt    # Dipendenze Python
├── render.yaml        # Configurazione Render
├── README.md          # Questo file
└── .env              # Variabili d'ambiente (locale)
```

## 🔧 Personalizzazione

Per aggiungere nuove categorie di barzellette:
1. Modifica `jokes.json` aggiungendo la nuova categoria
2. Aggiungi il comando nel file `bot.py`
3. Aggiorna i bottoni inline se necessario

## 📝 Note

- Il bot usa webhook in produzione su Render
- In sviluppo locale usa polling
- Le barzellette sono salvate in JSON per facilità di modifica
- Gestione errori robusta e logging inclusi