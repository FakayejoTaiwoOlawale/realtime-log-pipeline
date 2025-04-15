# Step 1: Base image (Python)
FROM python:3.10-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy all files from current folder to container
COPY . .

# Step 4: Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Run the Python script
CMD ["python", "consumer.py"]
