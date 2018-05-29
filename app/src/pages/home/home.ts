import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { User } from '../../models/User';
import { UserProvider } from '../../providers/user/user';
import { AlertController } from 'ionic-angular';
/**
 * Generated class for the HomePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
})
export class HomePage {

  private userList: any;
  private selectedItem: any;

  constructor(private alertCtrl:AlertController, private user: UserProvider, public navCtrl: NavController, public navParams: NavParams) {

  }
   
  ionViewWillEnter() {
    this.user.getUserList().subscribe((result)=>{
      this.userList = result;
      console.log(this.userList);
    }, (err) =>{
      var alert = this.alertCtrl.create();
      alert.setTitle("Error");
      alert.setMessage("Unable to connect to server\n" + sessionStorage.getItem("server"));
      alert.addButton("OK");
      alert.present();
    });
  }

  selectItem(item) {
    if(this.selectedItem == item) {
      this.selectedItem = null;

    }
    else {
      this.selectedItem = item;
    }
  
  }


  showItem(item) {
    return this.selectedItem == item;
  }
  

  

}
