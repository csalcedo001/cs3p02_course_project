from python:3.7
RUN pip3 install --upgrade pip
RUN pip3 install numpy matplotlib
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 install tqdm

# This line makes the following lines not to be cached...
ADD http://date.jsontest.com /etc/builddate

# ...so that updates in src/ are reflected in the docker image
COPY ./src /pipelines/component/src
