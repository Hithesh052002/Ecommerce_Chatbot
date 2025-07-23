# 🛒 E-commerce Data Visualization AI Agent

This project builds an **AI-powered agent** capable of answering natural language questions related to e-commerce sales data. It can process queries like:

- "What is my total sales?"
- "Which product had the highest CPC?"
- "Calculate the RoAS (Return on Ad Spend)"

…and return human-readable answers, SQL queries, and even visualizations!

---

## 📊 Datasets Used

We used the following datasets provided:

1. **Product-Level Eligibility Table**
2. **Product-Level Ad Sales and Metrics**
3. **Product-Level Total Sales and Metrics**

All datasets were cleaned, normalized, and imported into a MySQL database.

---

## 🚀 Tech Stack

| Component        | Description                                                   |
|------------------|---------------------------------------------------------------|
| **FastAPI**      | Backend API that receives questions and routes them to LLM     |
| **MySQL**        | SQL database storing all e-commerce metrics                    |
| **Google Gemini API** | Used to generate SQL queries from natural language questions |
| **Streamlit**    | Frontend UI for querying, displaying answers & charts          |
| **pandas**       | Data handling and manipulation                                 |
| **matplotlib**   | Data visualization (bar, pie, line charts)                     |
| **requests**     | To interact with Gemini API from FastAPI backend               |

---

## 🧠 AI Agent Workflow

1. **User Input**: A question is asked via API or Streamlit frontend.
2. **Query Generation**: Gemini API converts the question into an SQL query.
3. **SQL Execution**: The query is executed on the MySQL database.
4. **Answer Generation**: The result is formatted and optionally visualized.
5. **Response**: Final answer (text + optional chart) is returned.

---


