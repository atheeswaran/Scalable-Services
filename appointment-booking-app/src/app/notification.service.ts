// notification.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class NotificationService {
  private apiUrl = 'http://localhost:8002/receive_rabbitmq_message/';

  constructor(private http: HttpClient) {}

  receiveRabbitMQMessage(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
