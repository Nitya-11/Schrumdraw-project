# base image
FROM python:3.9-slim
# workdir
WORKDIR /app 

# copy
COPY . /app
# run
RUN pip install --no-cache-dir -r requirements.txt

# port

# command
CMD ["python", "substation_sld.py"]