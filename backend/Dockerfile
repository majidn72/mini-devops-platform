FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --proxy http://192.168.100.6:10809 -r requirements.txt

COPY . .

CMD ["python", "app.py"]
