FROM python:3.6-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirement.txt

EXPOSE 5000
CMD ["python", "app.py"]
