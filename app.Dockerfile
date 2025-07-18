FROM electropi_img:latest

WORKDIR /app

COPY app.py /app/
COPY plant_disease_model.onnx /app/
COPY plant_inference.py /app/
COPY images_preprocessing.py /app/
COPY data_warehouse.csv /app/

EXPOSE 8051

CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]