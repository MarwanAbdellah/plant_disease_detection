FROM python:3.11

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install onnxruntime
RUN pip install numpy
RUN pip install pandas
RUN pip install gdown
RUN pip install streamlit
RUN pip install importnb