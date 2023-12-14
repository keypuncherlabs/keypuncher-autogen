FROM python:3.11.5

WORKDIR /app

COPY . /app

RUN mkdir -p /generated

RUN pip install -r /app/requirements.txt
RUN pip install pyautogen

# Entrypoint to trigger main.py
CMD ["python", "main.py"]