FROM python:3.14-slim-bookworm

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
COPY . .

RUN npm run build
RUN mkdir -p static/css static/js \
 && rm -rf static/css/* static/js/* \
 && cp -r build/static/css/* static/css/ \
 && cp -r build/static/js/* static/js/

RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]