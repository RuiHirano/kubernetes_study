FROM python:latest

# install python requirements
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD [ "bash"]
