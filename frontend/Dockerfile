FROM nginx:alpine
# Copy the pre-built Angular app to Nginx's web root
COPY html /usr/share/nginx/html
# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
