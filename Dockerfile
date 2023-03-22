FROM python:3.8

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python api.py