FROM python:3.10
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY fill_mask.py .
CMD ["streamlit", "run", "fill_mask.py"]
