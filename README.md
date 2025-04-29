# 🔍 BrandSentio - AI-Powered Brand Sentiment Analyzer

![Project Banner](https://via.placeholder.com/800x300?text=BrandSentio+Sentiment+Analysis) *(Replace with actual banner image)*

A powerful sentiment analysis tool that scans Reddit and news sources to measure public perception of your brand in real-time.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Reddit Analysis** | Track upvotes/downvotes and comments sentiment |
| 📰 **News Monitoring** | Analyze brand mentions across global news sources |
| 📈 **Smart Scoring** | Proprietary algorithm combines engagement & sentiment |
| 📉 **Interactive Visuals** | Beautiful charts and graphs for easy interpretation |
| 🌐 **Web Dashboard** | Clean, user-friendly interface |

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0-green?logo=flask)
![PRAW](https://img.shields.io/badge/PRAW-Reddit%20API-orange)
![VADER](https://img.shields.io/badge/VADER-Sentiment%20Analysis-yellowgreen)

```mermaid
graph TD
    A[User Input] --> B(Reddit API)
    A --> C(NewsAPI)
    B --> D[Sentiment Analysis]
    C --> D
    D --> E[Visualizations]
    D --> F[Performance Score]
