import streamlit as st
import random

st.title("💸 Who's Paying?")

names = st.text_input("Enter names separated by commas:")

if st.button("Pick a Victim"):
    if names:
        name_list = [n.strip() for n in names.split(",") if n.strip()]
        payer = random.choice(name_list)
        st.balloons()
        st.success(f"🎉 The person paying is: **{payer}**")
    else:
        st.error("Please enter some names first!")