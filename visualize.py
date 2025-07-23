import streamlit as st
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://localhost:8000/ask"

# --- Custom CSS for background and style ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #3b82f6;
        text-align: center;
        margin-bottom: 0.2em;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #6366f1;
        text-align: center;
        margin-bottom: 2em;
    }
    .stTextInput > div > div > input {
        border: 2px solid #6366f1;
        border-radius: 8px;
        font-size: 1.1rem;
        padding: 0.5em;
    }
    .stButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #3b82f6 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        font-size: 1.1rem;
        padding: 0.5em 2em;
        margin-top: 0.5em;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #6366f1;
        color: white;
        text-align: center;
        padding: 0.5em 0;
        font-size: 1rem;
        opacity: 0.95;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo and Title ---
st.markdown('<div style="text-align:center;"><img src="https://cdn-icons-png.flaticon.com/512/891/891462.png" width="80" style="margin-bottom: 0.5em;"/></div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🛒 E-commerce Data Visualization AI Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions about your e-commerce data and get instant answers with beautiful charts! 📊✨</div>', unsafe_allow_html=True)

question = st.text_input("🔎 Enter your question:")

if st.button("Ask and Visualize 🚀"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"question": question})
                if response.status_code == 200:
                    data = response.json()
                    if "error" in data:
                        st.error(f"Error: {data['error']}")
                        if "sql" in data:
                            st.code(data["sql"], language="sql")
                    else:
                        st.success("Answer:")
                        # Live typing effect for answer
                        answer_placeholder = st.empty()
                        answer_text = "Here are your results:"
                        for i in range(1, len(answer_text) + 1):
                            answer_placeholder.markdown(f'<span style="font-size:1.2rem; color:#3b82f6;">{answer_text[:i]}</span>', unsafe_allow_html=True)
                            time.sleep(0.03)
                        # Show results as table
                        if "results" in data and data["results"]:
                            df = pd.DataFrame(data["results"])
                            st.dataframe(df)
                            # Enhanced Visualization Logic
                            numeric_cols = df.select_dtypes(include='number').columns.tolist()
                            categorical_cols = df.select_dtypes(include='object').columns.tolist()
                            # 1. Line chart if 'date' column exists
                            if 'date' in df.columns and numeric_cols:
                                st.markdown("#### 📈 Trends over Time")
                                fig, ax = plt.subplots()
                                for col in numeric_cols:
                                    ax.plot(df['date'], df[col], marker='o', label=col)
                                ax.set_xlabel('Date')
                                ax.set_ylabel('Value')
                                ax.set_title('Trends over Time')
                                ax.legend()
                                plt.xticks(rotation=45)
                                st.pyplot(fig)
                            # 2. Scatter plot if two numeric columns and no date
                            elif len(numeric_cols) == 2:
                                st.markdown(f"#### 🔵 Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
                                fig, ax = plt.subplots()
                                ax.scatter(df[numeric_cols[0]], df[numeric_cols[1]], color='#6366f1')
                                ax.set_xlabel(numeric_cols[0])
                                ax.set_ylabel(numeric_cols[1])
                                ax.set_title(f'{numeric_cols[1]} vs {numeric_cols[0]}')
                                st.pyplot(fig)
                            # 3. Bar chart if one categorical and one numeric column
                            elif len(numeric_cols) == 1 and categorical_cols:
                                st.markdown(f"#### 🟪 Bar Chart: {numeric_cols[0]} by {categorical_cols[0]}")
                                fig, ax = plt.subplots()
                                df.groupby(categorical_cols[0])[numeric_cols[0]].sum().plot(kind='bar', ax=ax, color='#3b82f6')
                                ax.set_xlabel(categorical_cols[0])
                                ax.set_ylabel(numeric_cols[0])
                                ax.set_title(f'{numeric_cols[0]} by {categorical_cols[0]}')
                                st.pyplot(fig)
                            # 4. Fallback: show all numeric columns as bar chart
                            elif numeric_cols:
                                st.markdown("#### 🟦 Bar Chart of Numeric Columns")
                                st.bar_chart(df[numeric_cols])
                        else:
                            st.info("No results found.")
                        if "sql" in data:
                            st.caption("SQL Query used:")
                            st.code(data["sql"], language="sql")
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Request failed: {e}")

# --- Footer ---
st.markdown('<div class="footer">Made with ❤️ by Hithesh &middot; Powered by Streamlit &middot; 2025</div>', unsafe_allow_html=True) 