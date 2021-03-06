import streamlit as st
import funcs
import pandas as pd

def reporting():
  st.title("Reporting/Classification Exercise")
  text = funcs.get_text_block("reporting.txt")
  st.markdown(text)
  st.image("..//pdac2021_res_est_course//images//res_table.jpg", use_column_width=True)
  
  st.markdown("## Answers")
  text = funcs.get_text_block("RPT_Answers.txt")
  st.markdown(text)
