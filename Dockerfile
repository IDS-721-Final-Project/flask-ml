FROM python:3.6-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install flask

EXPOSE 5000
CMD ["python", "api.py"]
