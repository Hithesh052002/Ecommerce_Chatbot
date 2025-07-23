# Ecommerce_Chatbot
E-commerce Data Visualization AI Agent
An AI-powered system that lets users ask natural language questions about their e-commerce data and receive answers — including visualizations, SQL queries, and human-readable responses.

🚀 Project Title
Build an AI Agent to Answer E-commerce Data Questions

📊 Datasets Used
✅ Product-Level Eligibility Table (mapped)

📈 Product-Level Ad Sales and Metrics (mapped)

💰 Product-Level Total Sales and Metrics (mapped)

🎯 Objective
Build an intelligent agent that can:

✅ Answer any question related to the datasets.

✅ Receive questions via API endpoints.

✅ Convert questions into SQL queries using LLM.

✅ Query MySQL database and return accurate answers.

✅ Return both SQL and human-readable responses.

🌟 (Bonus) Visualize results for supported queries.

🌟 (Bonus) Simulate live typing response (event streaming).

🛠️ Tech Stack
Tool	Purpose
FastAPI	Backend API to handle user questions
MySQL	Database holding structured e-commerce data
Streamlit	Frontend interface for question/answer & charts
Google Gemini API	Convert natural language → SQL
pandas	Data handling and manipulation
matplotlib	Visualization (bar, pie, line charts, etc.)
requests	Communicate with Gemini via REST API

📂 Folder Structure
bash
Copy
Edit
.
├── data/
│   └── *.csv                         # Your mapped datasets
├── llm/
│   └── llm.py                        # Handles prompt → SQL using Gemini
├── db/
│   └── mysql_setup.sql               # Table creation and data insertion
├── api/
│   └── main.py                       # FastAPI app
├── ui/
│   └── dashboard.py                  # Streamlit interface
├── requirements.txt
└── README.md
✅ Features
Ask questions like:

“What is my total sales?”

“Which product had the highest CPC?”

“Calculate my RoAS.”

Get:

🧠 Gemini-generated SQL queries

📋 SQL result as plain text

📊 Visual charts (bar, pie, line)

Modular & extendable architecture

🧠 How It Works
User asks a question via FastAPI or Streamlit.

LLM (Gemini API) converts the question into an SQL query.

Query is executed on MySQL database.

Result is returned in:

Text (natural language)

SQL query

(Bonus) Matplotlib visual

🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/ecommerce-ai-agent.git
cd ecommerce-ai-agent
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Setup MySQL
Run the SQL script to create tables and import CSVs:

bash
Copy
Edit
mysql -u root -p < db/mysql_setup.sql
Update your .env or config in code with:

env
Copy
Edit
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=ecommerce
4. Add Gemini API Key
Visit: https://aistudio.google.com/apikey

Add your key in llm/llm.py

python
Copy
Edit
GEMINI_API_KEY = "your-api-key"
▶️ Run the App
Start FastAPI Backend
bash
Copy
Edit
cd api
uvicorn main:app --reload
Start Streamlit Frontend
bash
Copy
Edit
cd ui
streamlit run dashboard.py
