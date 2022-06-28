from python:3.7
RUN pip install --upgrade pip
RUN pip install numpy matplotlib
COPY ./src /pipelines/component/src
