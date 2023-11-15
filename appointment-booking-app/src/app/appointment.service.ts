import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AppointmentService {
  private apiUrl = 'http://localhost:8001/api/book-appointment/';

   constructor(private http: HttpClient) { }

  bookAppointment(doctorId: number, doctorName: string, appointmentTime: string): Observable<any> {
    const body = { doctor_id: doctorId, doctor_name: doctorName, appointment_time: appointmentTime };
    return this.http.post<any>(this.apiUrl, body);
  }
}


