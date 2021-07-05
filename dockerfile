FROM python:3.8
WORKDIR /var/www
COPY . /var/www
RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
CMD ["python", "api.py"]

