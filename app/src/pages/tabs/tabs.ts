import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomePage } from '../../pages/home/home';
import { SettingsPage } from '../../pages/settings/settings';
import { EventsPage } from '../../pages/events/events'

/**
 * Generated class for the TabsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-tabs',
  templateUrl: 'tabs.html',
})
export class TabsPage {

  private tab1Root = HomePage;
  private tab2Root = EventsPage;
  private tab3Root = SettingsPage;
  private tab1Name: string = "Home";
  private tab2Name: string = "Events";
  private tab3Name: string = "Settings";

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }



}
