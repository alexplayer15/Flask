FROM python:3.10

WORKDIR /app

COPY dependencies.txt /app/

RUN pip install --no-cache-dir -r dependencies.txt

COPY /home/alex_player/Flask/main.py /app/
COPY /home/alex_player/Flask/templates /app/templates

EXPOSE 5001

CMD ["python", "main.py"]
