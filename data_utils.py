import pandas as pd
import streamlit as st

def read_uploaded_file(uploaded_file):
    try:
        if uploaded_file.name.endswith(('xlsx','xls')):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('csv'):
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Unsupported file type.")
            return None
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

def make_context_from_rows(df, row_indices):
    if len(row_indices)==0: return ""
    return df.iloc[row_indices].to_string(index=False)

def all_row_texts(df):
    # For Chroma: store each row as a nicely concatenated string for embedding
    return [', '.join(str(val) for val in row) for row in df.values]