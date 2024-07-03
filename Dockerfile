# Use the official Python image from the slim variant
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Update apt-get, install dependencies, and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the Streamlit app code to the container
COPY . /app

# Expose the Streamlit port
EXPOSE 8501

USER 1001

# Command to run the Streamlit app
# CMD ["streamlit", "run", "main2.py"]

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "main2.py", "--server.port=8501", "--server.address=0.0.0.0"]