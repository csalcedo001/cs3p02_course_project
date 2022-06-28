from python:3.7
RUN pip install --upgrade pip
RUN pip install numpy matplotlib
RUN pip install torch torchvision torchaudio
COPY ./src /pipelines/component/src
