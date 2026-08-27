from airflow import DAG
from airflow.operators.python import PythonOperator 
from datetime import datetime

# Define our first task
def preprocess_data():
    print("Preprocessing data...")

# Define our second task
def train_model():
    print("Training model...")

# Define our third task
def evaluate_model():
    print("Evaluating model...")

# Define the DAG
with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2025, 6, 15),
    schedule="@weekly",  # ✅ updated for Airflow 2.9+
    catchup=False        # optional but recommended to avoid backfill
) as dag:
    
    # Define the tasks
    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data
    )
    
    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model
    )
    
    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model
    )

    # Set the dependencies (order)
    preprocess >> train >> evaluate
