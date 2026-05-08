Deepfake Guardian: Real-Time AI Detection System
Deepfake Guardian is a full-stack end-to-end solution designed to detect facial manipulations in videos. Using state-of-the-art computer vision and deep learning, the system extracts facial features from video frames and classifies them as authentic (Real) or manipulated (Fake) using a custom-trained Convolutional Neural Network (CNN).

🚀 Features
Automated Preprocessing: Robust pipeline using OpenCV and MTCNN for face detection, cropping, and normalization.

Deep Learning Engine: Trained on the industry-standard FaceForensics++ dataset.

High Performance: Backend powered by FastAPI for low-latency asynchronous processing.

User-Friendly Interface: Modern React.js dashboard for video uploads and real-time result visualization.

Error Resilient: Preprocessing scripts designed with built-in error handling for corrupted video frames.

Dockerized: Fully containerized for consistent deployment across different environments.

🛠️ Tech Stack
Frontend: React.js, Tailwind CSS, Zustand (State Management)

Backend: FastAPI (Python), Uvicorn

AI/ML: TensorFlow/Keras (or PyTorch), MTCNN, NumPy

Computer Vision: OpenCV

DevOps: Docker, GitHub Actions

📂 Project Structure
Plaintext
deepfake-guardian/
├── backend/
│   ├── venv/                   # Virtual Environment
│   ├── preprocess.py           # Data extraction script
│   ├── train.py                # Model training script
│   ├── main.py                 # FastAPI application
│   └── models/                 # Saved .h5 or .pth models
├── frontend/
│   ├── src/                    # React components
│   └── public/                 # Static assets
└── Face-Dataset/               # Local storage for processed faces
    ├── preprocessed_faces/
    │   ├── real/
    │   └── fake/
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/your-username/deepfake-guardian.git
cd deepfake-guardian
2. Backend Setup
Bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
3. Data Preprocessing
Ensure your dataset paths are updated in preprocess.py, then run:

Bash
python preprocess.py
4. Frontend Setup
Bash
cd ../frontend
npm install
npm run dev
📊 Dataset Information
This project utilizes the FaceForensics++ dataset, specifically focusing on:

Original Sequences: High-quality YouTube footage.

Manipulated Sequences: DeepFake, FaceSwap, and Face2Face forgeries.

🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Acknowledgments
The FaceForensics++ team for providing the benchmark dataset.

The developers of MTCNN for the robust face detection implementation.
