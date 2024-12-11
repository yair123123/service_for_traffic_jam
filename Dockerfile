FROM python:3.10

WORKDIR /app

# התקנת הסביבה הווירטואלית
RUN python -m venv .venv

# התקנת התלויות
COPY requirements.txt .
RUN ./.venv/bin/pip install --upgrade pip && ./.venv/bin/pip install -r requirements.txt

# העתקת הקבצים
COPY . .

EXPOSE 5005

# הרצה מתוך הסביבה הווירטואלית
CMD ["/app/.venv/bin/python", "-m", "app.main"]






































