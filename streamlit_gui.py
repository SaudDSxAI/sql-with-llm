import streamlit as st
import newF

# Set up page configuration
st.set_page_config(page_title="Retail Insight Generator", layout="wide")

# ---- Sidebar ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/833/833314.png", width=80)
    st.markdown("### 🛒 Retail Insight Generator")
    st.markdown("Convert natural language to SQL and gain insights from your retail data.")
    st.markdown("---")
    st.info("Enter a natural language query to generate SQL and view data insights.")

# ---- Header ----
st.markdown("<h1 style='text-align: center;'>🛍️ Retail Insight Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Ask business questions in plain English. We'll do the rest.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- Main Input Section ----
with st.container():
    st.subheader("🔍 Ask a Question")
    user_input = st.text_input(
        "Enter your query below:",
        placeholder="e.g. Show me the maximum sales in the last quarter",
        label_visibility="collapsed"
    )

    generate = st.button("🚀 Generate Insights", use_container_width=True)

    if generate:
        if user_input:
            with st.spinner("🔄 Converting to SQL and fetching data..."):
                sql_query = newF.planText_to_sql(user_input)
                result_df = newF.input_to_sql(sql_query)

                st.markdown("### 🧠 Generated SQL Query")
                st.code(sql_query, language="sql")

                st.markdown("### 📊 Query Results")
                st.dataframe(result_df, use_container_width=True)
        else:
            st.warning("⚠️ Please enter a query to proceed.")

# ---- Footer ----
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>Built with ❤️ using Streamlit | © 2025 Retail Insights</p>",
    unsafe_allow_html=True
)
