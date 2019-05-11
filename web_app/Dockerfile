FROM python:3
LABEL maintainer='Zoe Statman-Weil <zstatmanweil@gmail.com>'

# The copy compan below files from the source's filesystem to the container's filesystem.
# The second compand changes the directory to it for the rest of the build
COPY ./ ./app
WORKDIR ./app

# Installs requirements into the app directory
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080 

CMD ["python", "app.py"] 
