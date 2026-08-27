📊 Airflow ML Pipeline Demo
This is a simple demo project using Apache Airflow to orchestrate a basic machine learning workflow consisting of preprocessing, training, and evaluation stages. It serves as a practical introduction to scheduling and managing ML tasks using Airflow.

📁 Project Structure
bash
Copy
Edit
airflow_demo/
├── dags/
│   └── mlpipeline.py       # Main DAG script
├── airflow.cfg             # Airflow configuration (if customized)
└── README.md               # You're here!
🛠️ Requirements
Python 3.8+

Apache Airflow 2.x

Docker (optional, but recommended)

VS Code / Terminal with WSL or Linux shell (if using Windows)

🔁 DAG Overview
The pipeline consists of the following tasks:

Preprocessing Data

Training the Model

Evaluating the Model

Tasks are executed in sequence using Airflow’s PythonOperator.

🚀 How to Run the Demo
1. Initialize Airflow
bash
Copy
Edit
airflow db init
2. Start Airflow Services
bash
Copy
Edit
airflow webserver --port 8080
airflow scheduler
(If using Docker, run docker-compose up with a proper docker-compose.yaml.)

3. Place Your DAG
Copy mlpipeline.py into the dags/ folder of your Airflow home directory (usually ~/airflow/dags/).

4. Access the UI
Visit http://localhost:8080 and activate the DAG named ml_pipeline.

🧠 DAG Code Summary (mlpipeline.py)
python
Copy
Edit
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def preprocess_data():
    print("Preprocessing Data...")

def train_model():
    print("Training Model...")

def evaluate_model():
    print("Evaluating Model...")

with DAG("ml_pipeline", start_date=datetime(2025, 6, 15), schedule_interval="@weekly", catchup=False) as dag:
    preprocess = PythonOperator(task_id="preprocess_task", python_callable=preprocess_data)
    train = PythonOperator(task_id="train_task", python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task", python_callable=evaluate_model)

    preprocess >> train >> evaluate
✅ Output
Once the DAG is triggered (either manually or on schedule), you’ll see the tasks executed in the correct order with success status in the UI.

📌 Notes
This is a minimal demo — real ML code can be substituted in place of print() statements.

Use logging for better visibility inside tasks.

Customize your Airflow config if needed via airflow.cfg.

🤝 Contribution
Feel free to fork this project and expand it with:

Real model training

Data versioning (e.g., DVC)

GitHub/DagsHub integration

Dockerized Airflow setup

📜 License
This project is licensed under the MIT License.