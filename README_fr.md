# Relaygram
Relaygram is a Telegram relay bot that forwards messages from one channel to another and saves attached files locally.

## 🧠 Objectif

Ce projet permet de surveiller automatiquement un canal Telegram pour :
- Télécharger les fichiers envoyés
- Transférer tous les nouveaux messages (fichiers ou non) vers un autre canal

Le tout est automatisé via un script Python utilisant la librairie Telethon, et fonctionnant en environnement Docker.

---

## 🔐 Authentification avec Telegram

Avant toute chose, il faut générer une **session Telegram persistante**.

### Étapes :
1. Aller sur [https://my.telegram.org](https://my.telegram.org)
2. Créer une application pour obtenir un `API_ID` et un `API_HASH`
3. Au premier lancement le script génère une `StringSession` :
    - Tu entres ton numéro de téléphone
    - Tu reçois un code par SMS ou Telegram
    - Une `StringSession` est générée que tu pourras réutiliser sans te reconnecter
    - Copier la chaine de caractère générer dans `SESSION_STRING`
     
Cette session est réutilisée automatiquement à chaque lancement.

---

## ⚙️ Modes de fonctionnement

Le système supporte deux modes d'exécution, configurables via la variable `MODE` dans le fichier `.env`.

### 🧪 Mode Développement (`dev`)
- Affiche un menu dans le terminal avec la liste de tes canaux
- Tu choisis manuellement le canal source à surveiller
- Le canal de destination est défini dans `.env`

### 🚀 Mode Production (`prod`)
- Le canal source et le canal destination sont définis dans `.env`
- Aucun menu ou interaction n’est nécessaire
- Idéal pour un déploiement automatisé sur un serveur

---

## 📁 Structure du projet

Le projet est organisé comme suit :

- `app/` : contient le script principal
- `downloads/` : fichiers téléchargés depuis Telegram
- `.env` : configuration environnementale (non versionnée)
- `.env.example` : modèle de configuration
- `Dockerfile` : image Docker pour exécuter le projet
- `docker-compose.yml` : conteneurisation et exécution simplifiée
- `README.md` : documentation complète

---

## ⚙️ Variables d'environnement (.env)

Le fichier `.env` doit contenir les éléments suivants :

- `API_ID` : identifiant de ton app Telegram
- `API_HASH` : hash de ton app Telegram
- `SESSION_STRING` : session persistante pour se connecter automatiquement
- `MODE` : `dev` ou `prod`
- `SOURCE_CHANNEL_ID` : identifiant du canal source (utilisé en prod uniquement)
- `TARGET_CHANNEL_ID` : identifiant du canal cible (toujours utilisé)

---

## 🐳 Commandes Docker utiles

### 🔧 Construction de l'image Docker

Utilise cette commande une seule fois (ou après modification du Dockerfile) :
- `docker compose build`

### ▶️ Lancement interactif (dev)

Permet de tester et choisir un canal via menu :
- `docker compose run --rm telegram-downloader`

### 🚀 Lancement automatique (prod)

Exécute le service avec la config `.env` sans interaction :
- `docker compose up -d`

---

## 📝 Remarques finales

- L'authentification ne se fait **qu'une seule fois** : la session est sauvegardée.
- Tu dois être **membre des deux canaux** (source et destination).
- Seuls les **nouveaux messages** sont pris en compte, pas l'historique.
