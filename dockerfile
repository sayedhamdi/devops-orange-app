# Step 1: Use an official Python base image
FROM python:3.11-slim

# Step 2: Set a working directory in the container
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Step 5: Copy the application code into the container
COPY . .

# Step 6: Expose the application port (Flask default is 5000)
EXPOSE 5000

# Step 7: Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 8: Run the application
CMD ["flask", "run"]
