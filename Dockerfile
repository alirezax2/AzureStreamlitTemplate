# Use the official Python image from the slim variant
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Update apt-get and install necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code to the container
COPY . /app

# Expose the Streamlit port
EXPOSE 8501

USER 1001

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py"]
