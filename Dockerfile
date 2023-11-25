# Stage 1: Build Stage
FROM python:3.9-alpine AS builder

WORKDIR /app

# Copy just the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3.9-alpine

WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY src /app/src
COPY utils /app/utils

# Set the command to run
CMD ["python", "src/cli.py", "file", "utils/anagrams.txt"]
