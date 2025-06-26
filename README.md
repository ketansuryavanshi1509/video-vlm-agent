


### 🗂️ 1. Project Structure


video-vlm-agent/
│
├── app.py
├── extract_frames.py
├── transcribe_audio.py
├── vision_language_model.py
├── qa_agent.py
├── export_utils.py
├── test_moviepy.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── frames/                 # auto-generated
│   └── frame_0.jpg, ...
├── logs/                   # auto-generated logs
│   └── log_2025-06-26_xx.txt
├── sample_videos/
│   └── 15sec_input_720p.mp4
```


# 🎥 Vision-Language Video QA Agent

This is a Streamlit-based app that lets you ask questions about a video using vision-language techniques (frame captioning + audio transcription + LLM-based QA).

---

## 🚀 Features

- Upload a video (MP4, AVI)
- Extracts key frames using OpenCV
- Transcribes audio using Whisper
- Describes video frames using an image captioning model
- Generates answers using a language model

---

## 🧠 Tech Stack

- `Streamlit` for UI
- `OpenCV` for frame extraction
- `MoviePy` for audio extraction
- `Whisper` for transcription
- `HuggingFace Transformers` for captioning + QA
- `Python 3.10+`

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/ketansuryavanshi1509/video-vlm-agent.git
cd video-vlm-agent
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (Required for Whisper)

Download FFmpeg and add its `bin` path to your system’s environment variables.

[Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📌 Sample Question Examples

* "How many players are visible?"
* "Who scored the goal?"
* "Is the match in a stadium?"

````

---

### 📦 3. `requirements.txt`

Ensure it includes:
```txt
streamlit
opencv-python
moviepy
transformers
torch
whisper
````

(✅ You’ve already added this)

---

### ⚙️ 4. `.gitignore`

Make sure this exists to ignore `venv`, `__pycache__`, `logs`, etc.

```gitignore
venv/
__pycache__/
*.pyc
logs/
frames/
sample_videos/
```

---

### ☁️ 5. GitHub Repo

Push to GitHub:
**Repo Link:** `https://github.com/ketansuryavanshi1509/video-vlm-agent`

Double check that:

* Code is clean ✅
* `.venv` is not uploaded ✅
* README is present ✅
* All necessary `.py` files are committed ✅

---

### 🌐 6. (Optional) Deploy to Streamlit Cloud

If allowed in the assignment:

* Create a **new Streamlit Cloud app**
* Connect to your GitHub repo
* Set `app.py` as the entry point

Deploy it here: [https://share.streamlit.io/](https://share.streamlit.io/)



## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by **Ketan Suryavanshi**
Feel free to contribute or raise issues!

````

