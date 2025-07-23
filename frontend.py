import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.title("E-commerce Data AI Agent")

st.write("Ask any question about your e-commerce data:")

question = st.text_input("Enter your question:")

if st.button("Ask"):
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
                        if "results" in data and data["results"]:
                            st.dataframe(data["results"])
                        else:
                            st.info("No results found.")
                        if "sql" in data:
                            st.caption("SQL Query used:")
                            st.code(data["sql"], language="sql")
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Request failed: {e}") 