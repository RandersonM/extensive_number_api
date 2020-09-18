FROM python:3.7-alpine
WORKDIR /extensive
ADD . /extensive
RUN apk add --no-cache gcc musl-dev linux-headers
EXPOSE 3000

RUN pip install -r requirements.txt
COPY . .
CMD ["python","app.py"]