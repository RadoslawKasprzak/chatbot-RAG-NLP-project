# Backend
FROM python:3.9-slim AS backend
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Frontend
FROM python:3.9-slim AS frontend
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "streamlit/app.py", "--server.port=8501"]
