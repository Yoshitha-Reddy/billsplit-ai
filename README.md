
# 🧾 BillSplit – AI Receipt & Expense Tracker

BillSplit is an AI-powered Receipt & Expense Tracker that makes splitting bills quick and easy.

Simply upload a photo of a receipt, and AI reads the items, prices, and total amount. You can then enter the number of people and instantly calculate how much each person should pay.

The project is built using Python, Streamlit, Google Gemini AI, and Twilio WhatsApp.

---

## 🚀 Features

- 📸 Upload a receipt image
- 🤖 AI-powered receipt analysis using Google Gemini
- 🧾 Extract item names and prices automatically
- 💰 Calculate the total bill
- 👥 Split the bill equally between multiple people
- 📱 Send the bill summary through WhatsApp using Twilio
- 🎨 Clean and modern dark-themed interface
- ⚡ Simple and easy-to-use interface

---

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Streamlit** – Web application framework
- **Google Gemini AI** – Reads and understands receipt images
- **Twilio** – WhatsApp messaging
- **HTML/CSS** – Custom UI styling
- **Git & GitHub** – Version control and project hosting

---

## 📂 Project Structure

```text
receipt-expense-tracker/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── venv/
│
├── app.py
├── models.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── README.md
````

---

## ⚙️ How It Works

```text
Upload Receipt
      ↓
Google Gemini AI
      ↓
Read Items & Prices
      ↓
Calculate Total
      ↓
Enter Number of People
      ↓
Calculate Individual Share
      ↓
Send Summary to WhatsApp
```

---

## 🧠 AI Receipt Analysis

The application sends the uploaded receipt image to Google Gemini.

Gemini extracts structured information such as:

* Item name
* Item price
* Total amount
* Currency

The extracted information is then displayed in the Streamlit application.

---

## 💰 Bill Splitting

Users can select the number of people sharing the bill.

For example:

```text
Total Bill: ₹1200

Number of People: 4

Each Person Pays: ₹300
```

The application calculates the amount automatically.

---

## 📱 WhatsApp Integration

BillSplit uses Twilio to send the bill summary to WhatsApp.

A typical message contains:

```text
🧾 BillSplit Summary

Total: ₹1200
People: 4
Each person pays: ₹300

Thank you for using BillSplit!
```

The WhatsApp integration uses Twilio's WhatsApp testing environment during development.

---

## 🔐 API Keys and Security

API keys and secret credentials should NOT be stored directly in the source code.

For local development, Streamlit secrets can be stored in:

```text
.streamlit/secrets.toml
```

Example:

```toml
GEMINI_API_KEY = "your_gemini_api_key"

TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_FROM = "your_twilio_whatsapp_number"
```

⚠️ Never upload your real `secrets.toml` file to GitHub.

Add it to `.gitignore`.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/receipt-expense-tracker.git
```

### 2. Open the project

```bash
cd receipt-expense-tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

### Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Keys

Create:

```text
.streamlit/secrets.toml
```

Add your Gemini and Twilio credentials.

Do not share these credentials publicly.

---

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example

### Input

Upload a receipt such as:

```text
Pizza       ₹300
Burger      ₹200
Drinks      ₹100
----------------
Total       ₹600
```

### Output

```text
Total: ₹600

Number of People: 3

Each Person Pays: ₹200
```

---

## 🎯 Project Objective

The main objective of BillSplit is to simplify receipt processing and bill splitting.

Instead of manually reading every item from a receipt and calculating everyone's share, users can upload a receipt and let AI extract the information automatically.

---

## 🌟 Future Improvements

Possible future features include:

* 👤 Split bills by individual items
* 📊 Expense history and tracking
* 📅 Monthly expense reports
* 👥 Group expense management
* 💳 Multiple payment options
* 📧 Email bill summaries
* 📱 Telegram integration
* 💾 Database storage
* 📈 Expense analytics
* 🌐 Deployment as a public web application

---

## 📚 Learning Outcomes

Through this project, I learned:

* How to build a Streamlit application
* How to use Google Gemini with Python
* How to process images using AI
* How to extract structured data from receipts
* How to calculate and split expenses
* How to integrate Twilio with a Python application
* How to use environment variables and secrets
* How to manage a project using Git and GitHub

---

## 👩‍💻 Author

**Yoshitha Reddy**

B.Tech Student

---

## 📄 Project Type

**AI + Python + Streamlit + Computer Vision + WhatsApp Automation**

---

## ⭐ Acknowledgement

This project was developed as part of an AI application development workshop and is based on the Receipt & Expense Tracker / Bill Splitter project concept.

````

### One important thing before you push to GitHub ⚠️

Your GitHub repository should **NOT** contain your real:

```text
.streamlit/secrets.toml
````

The workshop guide also specifically says not to commit the real secrets file; use a `secrets.toml.example` instead. 

So your GitHub project should eventually look like:

```text
receipt-expense-tracker/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example   ✅
│
├── app.py
├── models.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── README.md
```

