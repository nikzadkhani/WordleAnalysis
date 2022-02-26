from python:3.10.2-slim-bullseye

# Use /app as working directory
WORKDIR  /app/

# Copy all files
COPY . .

# Install wordle package and its dependencies
RUN pip install .

ENTRYPOINT [ "python3" "/app/main.py" ]