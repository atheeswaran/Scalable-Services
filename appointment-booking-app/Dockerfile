# Use an official Node runtime as a parent image
FROM node:16.14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install Angular CLI and dependencies
RUN npm install -g @angular/cli
RUN npm install

# Install http-server globally
RUN npm install -g http-server

# Copy the rest of the application files to the working directory
COPY . .

# Build the Angular application
RUN ng build 

# Expose the port the app runs on
EXPOSE 80

# Start the Angular application
#CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "80"]

# Start the http-server when the container starts
CMD ["http-server", "-p", "80"]
