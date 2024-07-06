FROM python

# Environment
#RUN mkdir /app
WORKDIR /app

COPY . .
#COPY /srv/dev-disk-by-uuid-bdf9cd33-6edc-4ad0-b5df-86d76c4e2a1e/docker/src/filer/filer.py /app

#ENV WATCH_DIRECTORIES="/MediaJellyfinDB/4K-output,/MediaJellyfinDB/1080p-output"
#ENV SLEEP_TIMER=10


CMD ["python", "/filer.py"]
