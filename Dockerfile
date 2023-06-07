# Downloading the Image From Docker Registry
FROM python:latest

# Create app directory
WORKDIR /app

# Install app dependencies files
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Bundle app source
COPY . .

# Execution
ENTRYPOINT ["python"]
CMD ["app.py"]
