FROM jupyter/datascience-notebook
USER root
RUN apt-get update
RUN pip install lxml html5lib beautifulsoup4
RUN apt-get install -y python-dev default-libmysqlclient-dev
RUN pip install mysqlclient
RUN pip install jupyterlab
RUN conda install keras
RUN pip uninstall -y numpy
RUN pip install numpy==1.16.4
RUN jupyter serverextension enable --py jupyterlab
