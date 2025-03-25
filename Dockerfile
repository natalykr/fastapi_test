FROM python:3.13-slim
COPY . .
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80"]