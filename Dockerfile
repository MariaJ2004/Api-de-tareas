FROM python:3.11-slim
WORKDIR /app
RUN pip install uvicorn fastapi
COPY ApiTareas.py .
CMD ["uvicorn","ApiTareas:app","--host","0.0.0.0","--port","8000"]
