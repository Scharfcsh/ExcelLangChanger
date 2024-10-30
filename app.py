import streamlit as st
import pandas as pd
from googletrans import Translator

# Initialize translator
translator = Translator()

def translate_to_english(df):
    """Translate all Chinese text in a DataFrame to English."""
    translated_df = df.copy()
    for col in df.columns:
        translated_df[col] = df[col].apply(lambda x: translator.translate(str(x), dest='en').text if pd.notnull(x) else x)
    return translated_df

# Streamlit UI
st.title("Chinese to English Excel Translator")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.write("Original Data:")
    st.dataframe(df)

    # Translate to English
    translated_df = translate_to_english(df)

    st.write("Translated Data:")
    st.dataframe(translated_df)

    # Download the translated Excel file
# output = pd.ExcelWriter("translated.xlsx", engine='openpyxl')
# translated_df.to_excel(output, index=False, sheet_name='Translated')
# output.save()
    output = pd.ExcelWriter("translated.xlsx", engine='openpyxl')
    print(output)
    translated_df.to_excel(output, index=False, sheet_name='Translated')
    # output.save()

    with open("translated.xlsx", "rb") as file:
        st.download_button(
            label="Download Translated Excel",
            data=file,
            file_name="translated.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
