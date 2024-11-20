import streamlit as st
import replicate

# Set Replicate API key (replace with your key)
replicate.Client(api_token="YOUR_REPLICATE_API_KEY")

# Streamlit page configuration
st.set_page_config(page_title="Text-to-Image Generator", page_icon="🖼️", layout="centered")

# Application title
st.title("Text-to-Image Generator with Stable Diffusion")

# Input for the text prompt
prompt = st.text_input("Enter a description for the image:")

# Button to generate the image
if st.button("Generate Image"):
    if prompt:
        try:
            # Call Replicate API to generate image from prompt
            model = replicate.models.get("stability-ai/stable-diffusion")
            version = model.versions.get("a0b1234")  # Specify the version of Stable Diffusion you want to use
            output = version.predict(prompt=prompt)
            
            # Display the generated image
            st.image(output[0], caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error generating image: {e}")
    else:
        st.error("Please enter a text description.")
