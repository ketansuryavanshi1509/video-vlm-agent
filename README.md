

---

````markdown
# 🎥 Vision-Language Video QA Agent

This is a Streamlit-based AI-powered application that allows users to upload a video and ask questions about its visual and audio content. The system extracts frames, transcribes audio, generates image captions, and answers questions using vision-language models and large language models.

---

## 🔧 Features

- 📤 Upload videos (`.mp4`, `.avi`)
- 📸 Extracts frames from video
- 🔊 Transcribes audio using OpenAI Whisper
- 🧠 Captions frames using a Vision-Language model
- 💬 Answers user questions based on visual and audio context
- 📁 Logs Q&A interactions

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Image Captioning**: BLIP / Vision-Language Model
- **Audio Transcription**: Whisper
- **Question Answering**: LLMs (HuggingFace Transformers)
- **Video Frame Extraction**: OpenCV
- **Audio Extraction**: moviepy / ffmpeg

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ketansuryavanshi1509/video-vlm-agent.git
cd video-vlm-agent
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # for Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Make Sure `ffmpeg` Is Installed

Download and extract [FFmpeg](https://www.gyan.dev/ffmpeg/builds/).
Then, add the `bin` path to your system environment variables. Example:

```
C:\Users\<YourUsername>\Downloads\ffmpeg-7.1.1-essentials_build\bin
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 📂 Directory Structure

```
video-vlm-agent/
│
├── app.py
├── extract_frames.py
├── transcribe_audio.py
├── vision_language_model.py
├── qa_agent.py
├── export_utils.py
├── requirements.txt
├── frames/              # Extracted video frames
├── logs/                # Q&A logs
├── sample_videos/       # Uploaded videos
└── README.md
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by **Ketan Suryavanshi**
Feel free to contribute or raise issues!

````

