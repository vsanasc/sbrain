import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DiaryService {

  private httpOptions: any;
  public errors: any = [];

  constructor(private http: HttpClient) { 
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    }
  }
  fetch() {
    this.http.get(
      'http://localhost:8000/api-diary/date/2019/10/05/', 
      this.httpOptions
    ).subscribe( data => {
      console.log(data) 
    })
  }
}
