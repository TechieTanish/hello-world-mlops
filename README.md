#\Project-Botanica--ML

This repository demonstrates a tiny reproducible MLOps flow:
1. Train a small model (`train.py`) — writes `artifacts/model.pkl` and `artifacts/metrics.json`
2. Run predictions from the command line with `run_model.py --input "[5.1,3.5,1.4,0.2]"`
3. Start a minimal Flask app with `python src/app.py` that serves `/predict`
4. Build a Docker image with `docker build -t hello-mlops .`
5. CI trains the model and uploads artifacts

## Quick start (local)
1. Create and activate a venv (example using python 3.13 or 3.11):
    python3 -m venv .venv
    source .venv/bin/activate

2. Install dependencies:
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt

3. Train the model:
    python train.py

4. Run a single prediction from CLI:
    python run_model.py --input "[5.1, 3.5, 1.4, 0.2]"

5. Start the API:
    python src/app.py
   Then test:
    curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"features":[5.1,3.5,1.4,0.2]}'

🔗 Blog

👉 Day 2: End-to-End Machine Learning Workflow — ML, ML Engineering, and MLOps
    {https://tanish-mlops-zero-to-hero.hashnode.dev/day-2-how-ml-ml-engineering-and-mlops-work-together?showSharer=true}

📌 What I Learned Today (In Short)

Understood the difference and collaboration between Data Science, ML Engineering, and MLOps.

Learned how an ML model moves from training → saving → inference → API exposure.

Implemented a Flask-based ML API with /predict and /health endpoints.

Practiced CLI and API inference for the same trained model.

Gained clarity on how MLOps automates workflows using CI/CD to save time and effort.

Revisited model containerization concepts as the first step toward deployment.

🧠 Role Clarity (Quick)

Data Scientist: Builds and trains the model.

ML Engineer: Integrates the model with APIs for application use.

MLOps Engineer: Automates training, testing, and deployment using CI/CD, Docker, and infrastructure tools.


🙏 Note

This learning is based on hands-on practice and explanations from Abhishek Sir, with gratitude to divine energy.

![CLI Prediction Output](docs/images/prediction_ml.png)

![API Output](docs/images/api_predict.png)


@Tanish