FROM python:3.10
WORKDIR /app
EXPOSE 8000
COPY /fast/requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY /fast/main.py .
RUN mkdir /app/cache && chown nobody /app/cache
USER nobody
ENV TRANSFORMERS_CACHE=/app/cache
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
