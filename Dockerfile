from tensorflow/tensorflow:latest-gpu-py3

RUN pip --no-cache-dir install prettytensor
RUN pip --no-cache-dir install tqdm
RUN pip --no-cache-dir install h5py

WORKDIR "/"
