# lang.py
import os

LANG = os.getenv("LANG", "en").lower()

translations = {
    "fr": {
        # French translations
        # Start.py
        "no_session": "🔐 Aucune SESSION_STRING trouvée dans .env.",
        "generate_session": "➡️ Lancement du script de génération de session...",
        "session_found": "✅ SESSION_STRING détectée.",
        "launch_main": "🚀 Lancement du script principal...",

        # Generate_session.py
        "connect": "📱 Connexion à Telegram...",
        "connected": "✅ Connexion réussie ! Voici ta StringSession :",
        "copy_session": "🛡️ Copie-la dans un endroit sécurisé.",
        "paste_session": "➡️ Ensuite, colle-la dans le fichier .env sous la variable SESSION_STRING.",
        "restart_script": "🔄 Relance le script pour continuer.",

        # main.py
        "mode_dev": "🧪 Mode développement activé.",
        "mode_prod": "🚀 Mode production activé.",
        "select_channel": "== Sélectionne un canal à surveiller ==",
        "channel_selected": "Canal sélectionné",
        "source_found": "Canal source trouvé",
        "source_not_found": "Canal avec cet ID introuvable dans vos dialogues :",
        "new_message": "📩 Nouveau message détecté.",
        "forwarded": "🔁 Message transféré vers",
        "downloading": "📥 Téléchargement de",
        "saved": "✅ Fichier sauvegardé dans",
        "choose_channel": "Numéro du canal à écouter :",
        "listening": "🔍 En écoute... Ctrl+C pour quitter.",

    },
    "en": {
        # English translations
        # Start.py
        "no_session": "🔐 No SESSION_STRING found in .env.",
        "generate_session": "➡️ Running the session generation script...",
        "session_found": "✅ SESSION_STRING detected.",
        "launch_main": "🚀 Launching the main script...",

        # Generate_session.py
        "connect": "📱 Connecting to Telegram...",
        "connected": "✅ Successfully connected! Here is your StringSession:",
        "copy_session": "🛡️ Copy it to a safe place.",
        "paste_session": "➡️ Then paste it in the .env file under the SESSION_STRING variable.",
        "restart_script": "🔄 Restart the script to continue.",

        # main.py
        "mode_dev": "🧪 Development mode activated.",
        "mode_prod": "🚀 Production mode activated.",
        "select_channel": "== Select a channel to monitor ==",
        "channel_selected": "Selected channel",
        "source_found": "Source channel found",
        "source_not_found": "Channel with this ID not found in your dialogs:",
        "new_message": "📩 New message detected.",
        "forwarded": "🔁 Message forwarded to",
        "downloading": "📥 Downloading",
        "saved": "✅ File saved in",
        "choose_channel": "Channel number to monitor:",
        "listening": "🔍 Listening... Press Ctrl+C to quit.",

    }
}

T = translations.get(LANG, translations["fr"])
