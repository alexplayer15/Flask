FROM python:3.10

WORKDIR /app

COPY dependencies.txt /app/

RUN pip install --no-cache-dir -r dependencies.txt

COPY /home/alex_player/Flask /app/

EXPOSE 5001

CMD ["python3", "main.py"]
