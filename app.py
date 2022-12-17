# Core packages
# NLP packages
import nltk
import streamlit as st

from src.tf_idf import run_summarization_tf_idf
from src.word_frequency import run_summarization_wf

if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('stopwords')

    st.header("Legal Text Summarization")
    st.subheader("This app will summarize the long legal judgements to provide meaningful insights in order to speed up the legal process per case")

   st.sidebar.markdown(""" # **Step 1: Upload File**""")
   text=st.sidebar.file_uploader(label="",type="txt")
    if st.button("Summarize"):
        if text:
            summary_result = run_summarization_tf_idf(text)
            st.subheader("LEGAL SUMMARY")
            st.success(summary_result)
        else:
            st.error("Please Input .txt file for summarization")

