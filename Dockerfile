# Agentic Turing Machine - Docker Image
# Multi-stage build for optimal size

# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
RUN pip install --no-cache-dir --user anthropic

# Stage 2: Runtime
FROM python:3.11-slim as runtime

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application files
COPY skills/ ./skills/
COPY run_with_skills.py .
COPY analyze_results_local.py .
COPY test_agent.py .
COPY input_data.txt .
COPY run_pipeline.sh .

# Make scripts executable
RUN chmod +x run_pipeline.sh

# Create output directory
RUN mkdir -p outputs

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default command - run the pipeline
CMD ["python", "run_with_skills.py", "--help"]

# Labels
LABEL org.opencontainers.image.title="Agentic Turing Machine"
LABEL org.opencontainers.image.description="Multi-agent translation pipeline with semantic drift analysis"
LABEL org.opencontainers.image.source="https://github.com/fouada/Assignment_3_Agentic-Turing-Machine-Development_-CLI-"

