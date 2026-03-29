<div align="center">
  <img src="https://img.shields.io/badge/Fintech-Hackathon%20Ready-blueviolet?style=for-the-badge&logo=codeforces" alt="Hackathon Ready" />
  <img src="https://img.shields.io/badge/Python-Django-092E20?style=for-the-badge&logo=django" alt="Django Backend" />
  <img src="https://img.shields.io/badge/AI-Groq%20Llama%203-F55036?style=for-the-badge&logo=meta" alt="Groq AI" />
  
  <br />
  <br />

  <h1>💸 AI Money Mentor 💸</h1>
  <p>
    <strong>A high-speed, intelligent personal finance assistant built for everyday individuals to score their financial health, automate SIP investing, and chat natively with cutting-edge AI.</strong>
  </p>
</div>

<hr />

## 🚀 Overview

**AI Money Mentor** removes the complexity of personal finance by providing a sleek, unified dashboard. In seconds, users can calculate their personalized **Money Health Score**, generate logical Systematic Investment Plan (SIP) mapping via the 30% rule, and ask tailored financial questions to an AI advisor powered by **Groq**'s ultra-fast Llama 3 models.

It is designed with a mobile-first, responsive Glassmorphism UI built on Tailwind CSS, running securely inside a robust Django/PostgreSQL backend infrastructure to protect sensitive financial inputs.

---

## ✨ Core Features

* 📊 **Automated Money Health Score**: Instantly gauge your financial habits. The system analyzes your Income-to-Savings ratio and outputs a strict logic-based health metric out of 100.
* 💰 **SIP Recommendation Engine**: Stop guessing how much to invest. We compute exactly how much of your disposable income should be safely routed into index funds using proven financial heuristics.
* 🤖 **Native AI Advisor Chat**: A WhatsApp-style, instantaneous AI chat window. Ask complex financial literacy questions and get beginner-friendly, secure, state-of-the-art responses powered by the Groq API.
* ⚡ **Ultra-Fast & Secure Backend**: Driven by Django REST Framework and a remote Supabase PostgreSQL database.

---

## 🛠️ Technology Stack

| Component         | Technology Used                                                                      |
| ----------------- | ------------------------------------------------------------------------------------ |
| **Backend API**   | Django, Django REST Framework, Python 3.10+                                          |
| **Database**      | PostgreSQL (Hosted on [Supabase](https://supabase.com/))                             |
| **AI Engine**     | [Groq Cloud](https://console.groq.com) (`llama-3.3-70b-versatile`)                   |
| **Frontend UI**   | HTML5, Vanilla JavaScript, Tailwind CSS (Design System generated via Stitch)         |
| **Deployment**    | [Render.com](https://render.com/) (Gunicorn & WhiteNoise)                            |

---

## 💻 Local Developer Setup

To run this project locally on your machine, follow these steps:

### 1. Clone & Environment Activation
```bash
git clone https://github.com/your-username/ai-money-mentor.git
cd ai-money-mentor
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a new file named `.env` in the root folder (next to `manage.py`) and supply your external API credentials:
```env
# Create a free PostgreSQL database on Supabase
DATABASE_URL=postgresql://postgres:<password>@<host>:6543/postgres

# Create a free API key on Groq Console
GROQ_API_KEY=gsk_your_api_key_here

SECRET_KEY=dev-secret-key-123
DEBUG=True
```

### 4. Migrate & Run
```bash
python manage.py migrate
python manage.py runserver
```

> Open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the app!

---

## ☁️ Deployment (Render)

This repository includes a `render.yaml` configuration blueprint, making it 1-click deployable.

1. Create a [Render.com](https://dashboard.render.com/) account.
2. Select **New Blueprint Instance**.
3. Link this exact GitHub repository.
4. Render will seamlessly build the Python environment using the included `build.sh` script.
5. Provide your `DATABASE_URL` and `GROQ_API_KEY` in the **Environment** tab of the newly created Web Service.

<div align="center">
  <br />
  <i>Built rapidly for Hackathons.</i>
</div>
