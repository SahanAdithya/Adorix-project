# Adorix: The Intelligent AI Kiosk System

> "Ads that look back at you."

Adorix transforms static advertising screens into intelligent, responsive agents. By combining real-time computer vision, voice interaction, and dynamic content delivery, Adorix creates a personalized bridge between brands and customers.

---

## 🚀 Overview

Adorix is a next-generation kiosk platform that moves beyond passive displays. It uses a three-stage intelligent flow to engage users:

1.  **Stage 1: Attract (Loop View)** – High-quality video advertisements play in a continuous loop to capture attention.
2.  **Stage 2: Personalize (Personalized View)** – Using privacy-first computer vision, Adorix detects the viewer's presence and demographics to serve tailored content.
3.  **Stage 3: Interact (Interaction View)** – A voice-activated AI Assistant (Avatar) engages the user in a natural conversation to answer questions, provide information, or assist with services.

---

## ✨ Key Features

-   **🎙️ Wake Word Detection**: Hands-free activation using the "Adorix" wake word (powered by Porcupine).
-   **🤖 Dynamic AI Avatar**: A responsive 3D/Video avatar with multiple emotional states (Idle, Listening, Thinking, Talking).
-   **💬 Intelligent Interaction Loop**: Seamless Speech-to-Text (STT) -> LLM Processing -> Text-to-Speech (TTS) workflow.
-   **📊 Real-time Analytics**: Tracks attention, engagement duration, and demographic data without compromising privacy.
-   **🎬 Campaign Studio**: A central dashboard to manage advertisements, interaction rules, and kiosk deployment.
-   **🔌 Real-time Sync**: WebSocket-based communication between the AI core and the frontend HUD.

---

## 🛠️ Tech Stack

### Frontend
-   **Framework**: [React](https://reactjs.org/) + [Vite](https://vitejs.dev/)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/)
-   **Animations**: [Framer Motion](https://www.framer.com/motion/)
-   **Icons**: [Lucide React](https://lucide.dev/)

### Backend (Core Controller)
-   **Language**: [Python 3.10+](https://www.python.org/)
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Real-time**: [WebSockets](https://websockets.readthedocs.io/)
-   **Services**: Async interaction management and state synchronization.

### AI & Audio
-   **Wake Word**: [Picovoice Porcupine](https://picovoice.ai/platform/porcupine/)
-   **LLM**: OpenAI GPT-4o / Local LLM Integration
-   **TTS**: pyttsx3 / gTTS
-   **STT**: SpeechRecognition / OpenAI Whisper

---

## 📂 Project Structure

```text
ADORIXI-NTEGRATED/
├── core_controller/    # Backend: FastAPI server & WebSocket hub
├── frontend/           # Frontend: React HUD & Kiosk Views
│   ├── src/views/      # LoopView, PersonalizedView, InteractionView
│   └── public/avatar/  # Avatar .webm animation files
├── services/           # AI services (Wake Word, Interaction Manager)
├── shared/             # Shared utilities and configurations
├── run_adorix.py       # Unified system launcher
└── requirements.txt    # Python dependencies
```

---

## ⚡ Quick Start

### 1. Prerequisites
-   Python 3.10 or higher
-   Node.js 18+ and npm
-   Microphone and Speakers

### 2. Backend Setup
```bash
# Navigate to root
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

### 4. Running the System
Adorix comes with a unified launcher that starts both the backend and frontend simultaneously:

```bash
python run_adorix.py
```

-   **ADORIX Web**: https://www.adorixit.com/

---

## 🔐 Privacy Commitment

Adorix is built with **Privacy by Design**. Demographic analysis is performed on the edge; no personal identifiable information (PII) or video feeds are stored or transmitted to the cloud. Only anonymous metadata is used to improve the engagement experience.

---


© 2024 Adorix IT Solutions. All rights reserved.
