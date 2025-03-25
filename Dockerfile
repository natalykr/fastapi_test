FROM python:3.13-slim
EXPOSE 80
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD python -m uvicorn main:app --host 0.0.0.0 --port 80