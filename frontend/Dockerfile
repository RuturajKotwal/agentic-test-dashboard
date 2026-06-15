# STAGE 1: Build the Vue application
FROM node:20-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# This compiles the app into the /app/dist folder
RUN npm run build

# STAGE 2: Serve with Nginx
FROM nginx:alpine as production-stage
# Copy the compiled files from Stage 1 to Nginx's public folder
COPY --from=build-stage /app/dist /usr/share/nginx/html
# Expose port 80
EXPOSE 80
# Start Nginx
CMD ["nginx", "-g", "daemon off;"]