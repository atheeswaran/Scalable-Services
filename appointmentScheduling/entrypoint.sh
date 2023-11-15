#!/bin/bash

# Start displaydoctors microservice
cd /app/displaydoctors && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 &

# Start appointmentscheduling microservice
cd /app/appointmentscheduling && python manage.py migrate && python manage.py runserver 0.0.0.0:8001 &

# Start notification microservice
cd /app/notification && python manage.py migrate && python manage.py runserver 0.0.0.0:8002

# Keep the script running
tail -f /dev/null
