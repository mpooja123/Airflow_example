# NOTE: paths are relative to the project root since the build context we specify is the project root


RUN pip install apache-airflow-providers-sqlite==1.0.0
USER root


COPY requirements-airflow.txt requirements.txt
RUN pip install -r requirements.txt
