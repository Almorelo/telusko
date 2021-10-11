FROM python:3
ENV PYTHONUNBUFFERED 1

# Vytvoříme složku
RUN mkdir /app

# Nastavíme pracovní složku
WORKDIR /app

# Zkopírujeme requirements.txt do pracovní složky
COPY requirements.txt /app

# Stáhneme vše z requirements
RUN pip install -r requirements.txt

# Zkopírujeme celý projekt do /app
COPY . /app

