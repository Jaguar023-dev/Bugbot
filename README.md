# 🤖 Nyxora AI - Ultimate WhatsApp Bot

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/nyxora-ai)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen.svg)](https://nodejs.org)
[![TypeScript](https://img.shields.io/badge/typescript-%5E5.0-blue.svg)](https://www.typescriptlang.org)

Nyxora AI is a production-ready, enterprise-grade WhatsApp bot with 257+ commands, featuring AI integration, media processing, group management, and a web dashboard.

## ✨ Features

### Core Features
- 🚀 **257+ Commands** across 15 categories
- 🤖 **Multi-Provider AI** (OpenAI, Gemini, Groq, Perplexity)
- 📥 **Media Downloads** (YouTube, TikTok, Instagram, Facebook, Twitter)
- 🎨 **Media Processing** (Stickers, Images, Video, Audio)
- 👥 **Group Management** (Welcome, Anti-spam, Moderation)
- 💰 **Payment Integration** (MPesa, Stripe, PayPal ready)
- ⚽ **Live Football** Scores & Statistics
- 🎮 **Interactive Games** (Trivia, Quiz, Truth/Dare)
- 🎵 **Audio Effects** (Nightcore, Bass, Reverse, Slow)
- 🔍 **Search** (Google, Images, Lyrics, Weather, Movies)
- 🎨 **Logo Maker** (Professional logo generation)
- 📊 **Analytics Dashboard** with web interface
- 🔐 **Multi-level Permission System**
- 🌍 **Multi-language Support**
- ⚡ **High Performance** with caching
- 🔄 **Auto-reconnect** & Session Management
- 📱 **WhatsApp Channels** Support

### Technical Features
- Clean Architecture (SOLID principles)
- TypeScript with strict mode
- Modular plugin system
- Automatic command loader
- SQLite/PostgreSQL support
- Redis caching
- Professional logging with Winston
- Docker support
- PM2 process management
- Comprehensive error handling
- Rate limiting & cooldowns
- Automated backups
- Self-update capability

## 📋 Prerequisites

- **Node.js** >= 18.0.0
- **npm** >= 9.0.0
- **FFmpeg** (for media processing)
- **Git** (for updates)

## 🚀 Quick Start

### Method 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/nyxora-ai.git
cd nyxora-ai

# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Edit .env with your settings
nano .env

# Build the project
npm run build

# Start the bot
npm start