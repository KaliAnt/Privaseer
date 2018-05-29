import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { EventProvider } from '../../providers/event/event';
import { AlertController } from 'ionic-angular';

/**
 * Generated class for the EventsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */


@Component({
  selector: 'page-events',
  templateUrl: 'events.html',
})
export class EventsPage {
  private eventList: any;

  constructor(public navCtrl: NavController,private alertCtrl:AlertController, private event:EventProvider, public navParams: NavParams) {
  }



  get_profiles() {
    
  }

  ionViewWillEnter() {
    this.event.getEventList().subscribe((result)=>{
      this.eventList = result;
      console.log(this.eventList);
    }, (err) =>{
      var alert = this.alertCtrl.create();
      alert.setTitle("Error");
      alert.setMessage("Unable to connect to server\n" + sessionStorage.getItem("server"));
      alert.addButton("OK");
      alert.present();
    });
  }

}
