# 🍒 BarzCerry - Bot Telegram Semplice

Il bot delle barzellette più dolce e semplice di Telegram!

## 🚀 Comandi

- `/start` - Benvenuto
- `/barz` - Barzelletta casuale  
- `/carabinieri` - Barzellette sui carabinieri
- `/scuola` - Barzellette sulla scuola
- `/animali` - Barzellette sugli animali
- `/help` - Aiuto

## 📦 Deploy su Render (SUPER FACILE!)

### 1. Crea BarzCerry
1. Vai su [@BotFather](https://t.me/botfather)
2. `/newbot`
3. Nome: `BarzCerry`
4. Username: `BarzCerryBot`
5. Copia il **token**

### 2. Deploy su Render
1. Vai su [render.com](https://render.com)
2. "New +" → "Web Service"
3. Connetti GitHub e seleziona questo repo
4. Impostazioni:
   - **Name**: `barzcerry`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

### 3. Aggiungi Token
Nelle "Environment Variables" aggiungi:
- **Key**: `TELEGRAM_BOT_TOKEN`
- **Value**: Il token da BotFather

### 4. Deploy!
Clicca "Deploy" e aspetta. BarzCerry sarà pronto! 🍒

## 🔧 Test Locale

```bash
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN="tuo_token"
python bot.py
```

Fatto! Super semplice! 🍒😄