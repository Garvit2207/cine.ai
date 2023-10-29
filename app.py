import streamlit as st

# Set a title for your app
st.title("Cine.ai")

# Add a heading
st.header("Movie Rating Predictor")

# Create a text input field
user_input = st.text_input("Please enter something about the movie eg.(Storyline,cast,genre) min 100chars")

# Create a submit button
if st.button("Submit"):
    st.write("You entered:", user_input)
