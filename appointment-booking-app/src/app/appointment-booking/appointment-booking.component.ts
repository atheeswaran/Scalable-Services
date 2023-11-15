import { Component } from '@angular/core';
import { AppointmentService } from '../appointment.service';
import { DoctorService } from '../doctor.service'; // Import the DoctorService
import { Doctor } from '../doctor.interace';
import { NotificationService } from '../notification.service';



@Component({
  selector: 'app-appointment-booking',
  templateUrl: './appointment-booking.component.html',
  styleUrls: ['./appointment-booking.component.css']
})
export class AppointmentBookingComponent {
  doctorId: number = 0;
  appointmentTime: string = '';
  doctorName: string = '';
  isAppointmentBooked: boolean = false;
  isDoctorAvailable: boolean = true;
  availableDoctors: Doctor[] = [];
  rabbitMQMessage: any;


  constructor( private doctorService: DoctorService, 
               private appointmentService: AppointmentService,
               private notificationService: NotificationService) { }
  
  ngOnInit(): void {
  this.fetchAvailableDoctors();
  //this.receiveMessage();
}

  fetchAvailableDoctors() {
    this.doctorService.getAvailableDoctors().subscribe(doctors => {
    this.availableDoctors = doctors;
  });
}              

  bookAppointment(): void {
    this.isAppointmentBooked = false;
    this.isDoctorAvailable = true;
    this.appointmentService.bookAppointment(this.doctorId,  this.doctorName, this.appointmentTime)
      .subscribe(
        response => {
          console.log('Appointment booked successfully:', response);
          this.isAppointmentBooked = true;
          // Handle success, e.g., show a success message
          this.receiveMessage();
        },
        error => {
          console.error('Error booking appointment:', error);
          this.isDoctorAvailable = false;
          // Handle error, e.g., show an error message
        }
      );
  }
  receiveMessage(): void {
    console.log('inside receiveMessage');
    this.notificationService.receiveRabbitMQMessage().subscribe(
      (data) => {
        this.rabbitMQMessage = data;
        console.log('Received RabbitMQ Message:', data);
      },
      (error) => {
        console.log('Error receiving RabbitMQ Message:', error);
      }
    );
  }

  
}


