# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Expose port if you want to run an API later
EXPOSE 8000

# Command to run tests (or run app)
CMD ["pytest", "-v"]
