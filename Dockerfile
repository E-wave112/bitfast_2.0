FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# install c++ compiler dependencies
RUN apt-get update && apt-get install -y build-essential

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app/

CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000","--reload"]