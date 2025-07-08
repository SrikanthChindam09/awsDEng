from datetime import datetime, timedelta
from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

# Define the function to be executed
def print_hello():
    print("✅ Hello from the PythonOperator task!")

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='trial_python_operator_dag',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    start_date=pendulum.datetime(2025, 7, 1, tz="UTC"),
    catchup=False,
    tags=['srikanth', 'python'],
) as dag:


    # Start and End tasks
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')


    # Create PythonOperator task
    task_hello = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello,
    )

    start >> task_hello >> end
