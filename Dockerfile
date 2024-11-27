# Backend
FROM python:3.9-slim AS backend
WORKDIR /app
COPY ./api /app
RUN pip install -r /app/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Frontend
FROM python:3.9-slim AS frontend
WORKDIR /app
COPY ./frontend /app
RUN pip install -r /app/requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
