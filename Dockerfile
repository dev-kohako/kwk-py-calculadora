FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY calculadora.py .

RUN echo '#!/bin/bash\nxvfb-run -a python calculadora.py' > run.sh && chmod +x run.sh

CMD ["./run.sh"]