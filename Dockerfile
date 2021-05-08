# NOTE: paths are relative to the project root since the build context we specify is the project root

FROM puckel/docker-airflow:1.10.1
USER root


COPY requirements-airflow.txt requirements.txt
RUN pip3 install -r requirements.txt
