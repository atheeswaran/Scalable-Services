# Scalable-Services Assignment

**Name: M. ATHEES WARAN => Group 24 => BITS ID: 2022mt93200 (2022mt93200@wilp.bits-pilani.ac.in)**

               **HealthCare : Appointment Scheduling microservices App**
**Prerequisites:**

**Install Django/DRF:** Install Django by using pip install django & pip install djangorestframework.

**Install MySQL:** Install MySQL using pip install mysql

**Install Docker:** Make sure you have Docker installed on your system. You can download it from the official Docker website.

**Install Minikube:** Install Minikube to create a local Kubernetes cluster. You can find the installation instructions on the Minikube GitHub repository.

**Install kubectl:** Kubectl is the command-line tool for interacting with your Kubernetes cluster. Install it according to the official Kubernetes documentation.

**Code Repos:**

**Important diagrams:**

**Application Architecture:**

![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/65ed8d00-a1fd-482a-b17b-dd62e7ee818f)

**Application Frontend - 3 micorservices (display/appointment/notification):**

![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/485654b6-9731-4f74-9a3d-d5a6c4b10bc0)

**HIGH LEVEL FLOW DIAGRAM:**

![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/81725fd0-cde4-426c-8ef9-ff2f9a8273f0)

**Detailed Steps:**

**Step 1.** Create a Microservices based application with at least 3 microservices. Each service should be maintained as a separate code repository so that it can be developed, deployed, and tested independently.

**Application Description:**

Appointment Scheduling application assists patients :
1) Check Available doctors
2) Book appointment with the available doctor with convinient time
3) Patients are notified with a message (doctor info, appointment time) once appointment is booked successfully.

Implemented microservices:
1) Display doctors
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/30755776-1f96-4493-8059-35ea1add7c3d)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/d92adc7a-5b1d-4730-85d8-d51c0c89328a)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/c4ef113c-9bae-4f3d-98b4-6a2c0f518593)
2) Scheduling Appointment
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/9881f09b-666e-4761-9edd-6002341d1188)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/e8ba3f20-c5bc-43b7-a363-1617be4ab1fa)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/181d74af-66aa-4970-9054-490b3ad2d33c)   
3) Notification
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/5c05aae9-0d13-4c6f-a1ff-c841c7d501ee)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/ba38c1c5-84c7-456a-92cc-2839e41e8693)
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/229c2c6d-5fa5-4ab0-acc9-c19799b09dc9)
4) Appointmentbookingapp - Frontend angular service:
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/35bfc31b-0110-4b2b-9853-0794fb9261a1)

=> Each Microservice has their own code repo with seperate Databases.
=> Front end is developed in Angular and microservices are developed usign Django REST Framework (DRF)

**Step 2.** Use a suitable database and database related pattern for these services

   => each microservice (display doctors, appointmentscheduling, notification) uses seperate databases
   1) displaydoctorsdb
      ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/be5a6df3-d9df-40c2-91a7-f20900455616)
   2) appointmentSchedulingdb
      ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/727525c2-7812-4e6c-9601-874316ebae21)
   3) Notificationdb
      ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/7857afd3-38a9-4740-8741-78ee54733577)
  
   => MySQL Database is used for all three microservices (Check respective settings.py in repo)
   
**Step 3.** Use a suitable approach for the communication between these services (avoid high coupling between these services)

   1) **REST API**
      
      => From Frontend UI, REST endpoints are used to call below services:
      1) Displaydoctors => http://localhost:8000/doctors/
         => to display the available doctors
      2) Appointment Scheduling => http://localhost:8001/api/book-appointment/
         => to book the appointment on specified time with selected doctor
      3) Notification  => http://localhost:8002/receive_rabbitmq_message/
         => to receive the message from RabbitMQ service once appointment is booked successfully and display to patient
      
   2) **Messaging channel - RabbitMQ**
      
      1) Between appointmentscheduling and notification microservices, RabbitMQ is used to receive the messages.
      2) this ensures there is **NO high coupling** between the services
      3) Start RabbitMQ => docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq
    ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/11d72061-e727-469c-8392-86e59d53c814)

      

**Step 4.** Deploy all services on a single docker container

**Step 5.** Deploy each service on separate docker containers

Below Docker commands are used to deploy each microservice on seperate containers (Refer Dockerfile and requirements.txt in respective GITHubRepo)

1) Database container - mysql:
   1) docker exec -it mysql1 bash
   2) mysql -u athish -p
   3) show databases
   4) use registerusersdb
   5) INSERT INTO displaydoctors_doctor (id, name) VALUES (1, 'athish');

2) MQ Container - RabbitMQ:
   1) docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq

3) Display Doctors container:
   1) docker run -d --name mysql1 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=registerusersdb -e MYSQL_USER=athish -e MYSQL_PASSWORD=test -p 3307:3307 mysql:latest
   2) docker build -t athishwaran/display:0.0.1 .
   3) docker exec -it 7be653a929ec python manage.py migrate
   4) docker run -d -p 8000:8000 --link mysql1:mysql athishwaran/display:0.0.1

5) Appointmentscheduling container:
   1) docker run -d --name mysql2 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=appointmentdb -e MYSQL_USER=athish -e MYSQL_PASSWORD=test -p 3308:3308 --network notify mysql:latest
   2) docker build -t athishwaran/appointment:0.0.3 .
   3) docker run -d -p 8001:8001 --link mysql2:mysql athishwaran/appointment:0.0.2
   4) docker exec -it 5862df6fb4c9 python manage.py migrate

4) Notification container:
   1) docker build -t athishwaran/notification:0.0.1 .
   2) docker run -d -p 8002:8002 athishwaran/notification:0.0.1


**Step 6.** Run a minikube cluster on your local machine and explore various options in this. Try deployment of your application on this.
   
   Kubectl Options
   ![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/56facfac-8ac6-4e82-886d-60038393b812)
![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/07e34437-0b47-4b93-9360-75cda8cd0d5c)
![image](https://github.com/atheeswaran/Scalable-Services/assets/19812046/c8a2fea3-11cf-46d7-9723-480ad6a2a4a2)




