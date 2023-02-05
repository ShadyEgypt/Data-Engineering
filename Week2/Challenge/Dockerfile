From python:3.9
COPY . /src
COPY ./requirements.txt /src/requirements.txt
WORKDIR /src
EXPOSE 8000:8000
RUN pip3 install --upgrade -r requirements.txt
CMD ["uvicorn", "webapp:app", "--host", "127.0.0.1", "--port", "8000"]