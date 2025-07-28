# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for PyMuPDF)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libxrender1 libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY ./src ./src
COPY ./input ./input
COPY ./output ./output
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "src/main.py"]
