import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.title("🧠 Smart Drift – Reality Drift AI")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API key not found. Check .env file.")
else:
    client = OpenAI(api_key=api_key)

    text = st.text_area("Paste text here", height=200)

    if st.button("Generate Summary"):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            with st.spinner("AI is summarizing..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Summarize clearly and simply."},
                        {"role": "user", "content": text}
                    ]
                )
                st.subheader("Summary")
                st.write(response.choices[0].message.content)