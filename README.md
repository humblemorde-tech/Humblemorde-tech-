# Humblemorde-tech-
Don't interfere with the park# WhatsApp Bot - Pairing Code Session

Lightweight WhatsApp bot using Baileys with pairing code auth. One-click deploy to Heroku, Render, and Railway.

**Owner**: [slomo254](https://facebook.com/slomo254)

## Features
- **Pairing Code Login**: No QR scan needed. Click to generate code and link WhatsApp
- **Session Generator**: Creates `creds.json` / session string automatically  
- **Deploy Ready**: Supports Heroku, Render, Railway with one-click buttons
- **Auto Reconnect**: Handles disconnects and keeps bot alive

## Quick Deploy

| Platform | Deploy |
| --- | --- |
| Heroku | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) |
| Render | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy) |
| Railway | [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new) |

## Setup - Pairing Code Method

1. **Deploy** using any button above
2. **Open app logs** in your platform dashboard
3. **Visit the pairing URL**: `https://your-app-name.herokuapp.com/pair` 
4. **Enter your WhatsApp number** with country code, no `+`. Example: `254712345678`
5. **Click Generate Code** and you’ll get an 8-digit code
6. **On WhatsApp**: `Linked Devices` > `Link a Device` > `Link with phone number instead` > Enter the code

Bot will print
