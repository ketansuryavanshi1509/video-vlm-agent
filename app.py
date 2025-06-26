# app.py
import streamlit as st  # type: ignore
import os
from extract_frames import extract_frames
from vision_language_model import caption_image
from qa_agent import answer_question
from transcribe_audio import transcribe_audio
from export_utils import export_qa_log

# Streamlit setup
st.set_page_config(page_title="🎥 VLM QA Agent", layout="centered")
st.title("🎥 Vision-Language Video QA Agent")

# Upload UI
uploaded_file = st.file_uploader("📤 Upload a video", type=["mp4", "avi"])
question = st.text_input("🧠 Ask a question about the video")

# Ensure folders exist
os.makedirs("sample_videos", exist_ok=True)
os.makedirs("frames", exist_ok=True)

# Main logic
if uploaded_file and question:
    video_path = os.path.join("sample_videos", uploaded_file.name)

    # Save uploaded video
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.info("📸 Extracting frames...")
    extract_frames(video_path)

    st.info("🔊 Transcribing audio...")
    transcript = transcribe_audio(video_path)

    st.info("🧠 Describing each frame...")
    captions = {}
    for frame in sorted(os.listdir("frames")):
        path = os.path.join("frames", frame)
        caption = caption_image(path)
        captions[frame] = caption
        st.image(path, width=200, caption=caption)

    st.success("✅ Frames & Audio processed!")

    # Build combined context
    context = transcript + "\n" + "\n".join(captions.values())

    st.info("💬 Generating answer...")
    answer = answer_question(context, question)
    st.write("### 📝 Answer:")
    st.write(answer)

    export_qa_log(question, answer)
