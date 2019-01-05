FROM python:alpine
COPY . .
RUN pip install pymysql
CMD ["python", "app.py"]
