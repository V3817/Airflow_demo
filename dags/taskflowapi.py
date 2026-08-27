from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="math_sequence_dag_with_taskflow",
    start_date=datetime(2025, 6, 15),
    schedule="@once",
    catchup=False,
) as dag:

    @task
    def start_number():
        initial_number = 10
        print(f"Starting Number : {initial_number}")
        return initial_number

    @task
    def add_five(number):
        new_number = number + 5
        print(f"ADD 5 : {number} + 5 = {new_number}")
        return new_number

    @task
    def multiply_by_two(number):
        new_number = number * 2
        print(f"Multiply by 2 : {number} * 2 = {new_number}")
        return new_number

    @task
    def subtract_by_three(number):
        new_number = number - 3
        print(f"Subtract by 3 : {number} - 3 = {new_number}")
        return new_number

    @task
    def square(number):
        new_number = number * number
        print(f"Square : {number} * {number} = {new_number}")
        return new_number

    # Task chaining
    start_value = start_number()
    added_value = add_five(start_value)
    multiplied_value = multiply_by_two(added_value)
    subtracted_value = subtract_by_three(multiplied_value)
    result = square(subtracted_value)
