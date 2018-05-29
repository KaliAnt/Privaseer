import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../../models/User';

/*
  Generated class for the UserProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class UserProvider {
  

  constructor(public http: HttpClient) {
    
  }



  getUserList() {
    var url:string = sessionStorage.getItem("server");

    return this.http.get(url + "/profiles");
  }
}
