# Scalable-Services Assignment

**Name: M. ATHEES WARAN => Group 24 => BITS ID: 2022mt93200 (2022mt93200@wilp.bits-pilani.ac.in)**

               **HealthCare : Appointment Scheduling microservices App**
**Prerequisites:**

**Install Django/DRF:** Install Django by using pip install django & pip install djangorestframework.

**Install MySQL:** Install MySQL using pip install mysql

**Install Docker:** Make sure you have Docker installed on your system. You can download it from the official Docker website.

**Install Minikube:** Install Minikube to create a local Kubernetes cluster. You can find the installation instructions on the Minikube GitHub repository.

**Install kubectl:** Kubectl is the command-line tool for interacting with your Kubernetes cluster. Install it according to the official Kubernetes documentation.

**Detailed Steps:**

**Step 1.** Create a Microservices based application with at least 3 microservices. Each service should be maintained as a separate code repository so that it can be developed, deployed, and tested independently.

**Application Description:**

Appointment Scheduling application assists patients :
a) Check Available doctors
b) Book appointment with the available doctor with convinient time
c) Patients are notified with a message (doctor info, appointment time) once appointment is booked successfully.

Implemented microservices:
1) Display doctors
2) Scheduling Appointment
3) Notification

=> Each Microservice has their own code repo with seperate Databases.
=> Front end is developed in Angular and microservices are developed usign Django REST Framework (DRF)

**Application Architecture:**

![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/2ad5b1e2-a7cd-4789-9a69-21bfebfbbf66)

**Step 2.** Use a suitable database and database related pattern for these services

   => each microservice (display doctors, appointmentscheduling, notification) uses seperate databases
   1) displaydoctorsdb
   2) appointmentSchedulingdb
   3) Notificationdb
  
   => MySQL Database is used for all three microservices
   
**Step 3.** Use a suitable approach for the communication between these services (avoid high coupling between these services)

   1) **REST API**
      => From Frontend UI, REST endpoints are used to call below services:
         a) Displaydoctors => http://localhost:8000/doctors/
            => to display the available doctors
         b) Appointment Scheduling => http://localhost:8001/api/book-appointment/
            => to book the appointment on specified time with selected doctor
         c) Notification  => http://localhost:8002/receive_rabbitmq_message/
            => to receive the message from RabbitMQ service once appointment is booked successfully and display to patient
      
   2) **Messaging channel - RabbitMQ**
      => Between appointmentscheduling and notification microservices, RabbitMQ is used to receive the messages.
      => this ensures there is **NO high coupling** between the services
      

**Step 4.** Deploy all services on a single docker container
**Step 5.** Deploy each service on separate docker containers


**Step 6.** Run a minikube cluster on your local machine and explore various options in this. Try deployment of your application on this.
   
   Kubectl Options
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/56facfac-8ac6-4e82-886d-60038393b812)
![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/07e34437-0b47-4b93-9360-75cda8cd0d5c)
![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/c8a2fea3-11cf-46d7-9723-480ad6a2a4a2)




