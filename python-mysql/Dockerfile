FROM python:3.9

RUN pip install mysql-connector-python pandas

RUN apt-get install git -y

RUN git clone https://github.com/vishnubob/wait-for-it.git 

COPY . .

CMD ["miniproject.py"]

ENTRYPOINT ["python"]