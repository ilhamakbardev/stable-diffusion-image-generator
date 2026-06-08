import streamlit as st
import torch
import numpy as np
import logic
from PIL import Image, ImageDraw, ImageOps, ImageFilter

# Config
st.set_page_config(page_title="StudioAI", layout="wide", page_icon="")

# Load Model
@st.cache_resource
def get_models():
    return logic.load_model()

try:
    pipe_txt2img = get_models()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

st.title("StudioAI: Creating Image with Stable Diffusion")

with st.sidebar:
    st.header("Parameters")
    steps = st.slider("Quality Steps", 15, 50, 30)
    cfg = st.slider("Creativity (CFG)", 1.0, 20.0, 7.5)
    seed = st.number_input("Seed Control", value=42)

[tab_gen] = st.tabs(["GENERATE"])

# Tab Generate
with tab_gen:
    c1, c2 = st.columns([1, 1], gap="large")

    # Input
    with c1:
        st.subheader("Input")
        with st.form(key="gen_form"):
            prompt = st.text_area("Prompt", "a cute robot in a futuristic city, 8k, masterpiece", height=150)
            neg_prompt = st.text_input("Negative Prompt", "blurry, bad anatomy, worst quality")

            submit_gen = st.form_submit_button("Initialize Generation", type="primary")

        if submit_gen:
            with st.spinner("Processing Image"):
                generated_list = logic.generate_image(
                    pipe_txt2img, prompt, neg_prompt, seed, steps, cfg
                )

                st.session_state['generated_images'] = generated_list

                if generated_list:
                    st.session_state['current_image'] = generated_list[0]

            st.rerun()

    with c2:
        st.subheader("Output")

        if 'generated_images' in st.session_state:
            imgs = st.session_state['generated_images']

            st.image(imgs[0], caption="Result", use_container_width=True)

        else:
            st.info("Masukkan prompt di panel kiri dan tekan Generate.")