FROM python:3.8

ADD scanner.py .

CMD ["python3", "./scanner.py"]

