FROM jupyter/datascience-notebook
USER root
RUN apt-get update
RUN pip install lxml html5lib beautifulsoup4
RUN apt-get install -y python-dev default-libmysqlclient-dev
RUN pip install mysqlclient
RUN pip install jupyterlab
RUN conda install keras
RUN jupyter serverextension enable --py jupyterlab
