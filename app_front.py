import streamlit as st
import requests

st.set_page_config(page_title="🎬 Movie Success Forecaster", page_icon="🎥")

st.title("🎬 Movie Success Forecaster")
st.write("Enter a movie name and a user review to forecast its success!")

movie = st.text_input("Enter Movie Title")
review = st.text_area("Paste a User Review")

if st.button("Predict Success"):
    try:
        res = requests.post(
            "https://forecast-movie-success.onrender.com/",  # change to Render URL after deploy
            json={"movie": movie, "review": review},
        )
        if res.status_code == 200:
            result = res.json()
            st.success(
                f"**Movie:** {result['movie']}  \n"
                f"**Prediction:** {result['prediction']}  \n"
                f"**Confidence:** {result['confidence']}"
            )
        else:
            st.error(f"Server returned error code: {res.status_code}")
    except Exception as e:
        st.error(f"❌ Could not connect to backend API. Error: {e}")

