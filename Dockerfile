# Use a specific Python version as the base image
FROM python:3.9

# Install distutils and SQLite
RUN apt-get update && apt-get install -y python3-distutils sqlite3

# Set the working directory in the container
WORKDIR /

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install "fastapi[standard]" \
    && pip install masonite-orm
    
# Copy the rest of the application code to the container
COPY . .

# Once files for migrations and database configurations are copied, run the migrations
RUN masonite-orm migrate

# Expose the port that the FastAPI application will be running on
EXPOSE 8000

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]