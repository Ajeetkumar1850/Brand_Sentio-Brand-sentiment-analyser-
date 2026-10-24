# Brand Sentineo 🔍

Brand Sentineo is a Flask-based web application that analyzes brand sentiment by collecting public content from multiple online sources and using VADER sentiment analysis to estimate public opinion about a brand, product, or keyword.

## 🚀 Features

- 🔐 Google OAuth authentication
- 🔎 Search for brands, products, and keywords
- 📊 Sentiment analysis using VADER
- 🌐 Data collection from multiple platforms:
  - Reddit
  - NewsAPI
  - Event Registry
  - Tumblr
- ⚡ Parallel processing of source analyses
- 📈 Sentiment results displayed through a web interface
- 🖥️ Flask and Jinja2 templates for the user interface
- ☁️ Vercel deployment configuration

> **Note:** Sentiment scores are automated estimates and may not accurately represent the opinions of every user. Results depend on data availability, search terms, and API limitations.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Data Processing:** pandas
- **Sentiment Analysis:** VADER Sentiment
- **Data Collection:** PRAW, Requests, Beautiful Soup, lxml
- **Authentication:** Google OAuth
- **Frontend:** HTML, Jinja2
- **Deployment:** Vercel

## 📁 Project Structure

```text
brand-sentineo/
├── api/
│   └── index.py
├── templates/
│   ├── Admin_Dashboard.html
│   ├── login.html
│   ├── results.html
│   └── search.html
├── app.py
├── requirements.txt
├── vercel.json
├── wsgi.py
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configure the following variables in your environment:

| Variable | Description |
|---|---|
| `GOOGLE_CLIENT_ID` | Google OAuth client ID |
| `GOOGLE_CLIENT_SECRET` | Google OAuth client secret |
| `OAUTH_REDIRECT_URI` | OAuth callback URL |
| `FLASK_SECRET_KEY` | Secret key for Flask sessions |

You will also need valid credentials for the external data providers used by your application.

**Security:** Store all API keys and secrets in environment variables. Never commit private credentials to GitHub.

### 5. Run the Application

```bash
flask --app app run --debug
```

Open the application in your browser:

http://127.0.0.1:5000

## ☁️ Deployment

This project includes configuration files for deployment on Vercel.

1. Push your project to GitHub.
2. Import the repository into [Vercel](https://vercel.com/).
3. Configure the required environment variables in the Vercel dashboard.
4. Update your Google OAuth redirect URI to match your deployed domain.
5. Deploy the application.
6. Test authentication, searches, and sentiment results.

Deployment behavior may depend on external API availability, provider quotas, and serverless execution limits.

## 🔒 Security Best Practices

- Never publish API keys, OAuth secrets, or access tokens.
- Use environment variables for sensitive configuration.
- Generate a strong, unique Flask secret key for production.
- Rotate any credentials that have already been exposed.
- Review API provider rate limits and usage policies.
- Keep `.env` files and private credential files out of version control.

## 🐛 Troubleshooting

**Google OAuth is not working**
- Verify your client ID and client secret.
- Check that your redirect URI matches the Google Cloud Console configuration.

**No sentiment results are returned**
- Verify your API credentials.
- Check provider quotas and API availability.
- Try a different search keyword.

**Dependencies fail to install**
- Use a compatible Python version.
- Activate your virtual environment.
- Reinstall dependencies using `requirements.txt`.

**Vercel deployment fails**
- Review deployment logs.
- Verify environment variables and dependencies.
- Check serverless function execution limits.

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📄 License

No license was specified in the project files. Add a license before allowing others to reuse, modify, or distribute the project.
