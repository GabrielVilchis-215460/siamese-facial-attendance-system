# Este dockerfile tiene como funcionar fusionar en uno el frontend y el reverse proxy

# Etapa 1: compilar el frontend
FROM node:22-alpine AS frontend
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json* ./
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi
COPY frontend/ ./
RUN npm run build

# Etapa 2: Nginx con el sitio estático, proxy a /api y certificado autofirmado
FROM nginx:1.27-alpine
RUN apk add --no-cache openssl

#  Para acceder desde otro equipo de la red, pasa CERT_SAN con la IP del servidor.
ARG CERT_SAN="DNS:localhost,IP:127.0.0.1"
RUN mkdir -p /etc/nginx/certs && \
    openssl req -x509 -nodes -newkey rsa:2048 -days 365 \
      -keyout /etc/nginx/certs/server.key \
      -out /etc/nginx/certs/server.crt \
      -subj "/CN=localhost" \
      -addext "subjectAltName=${CERT_SAN}"

COPY nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY --from=frontend /app/dist /usr/share/nginx/html
