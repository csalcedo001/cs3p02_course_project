from python:3.7
RUN pip3 install --upgrade pip
RUN pip3 install numpy matplotlib
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
COPY ./src /pipelines/component/src
