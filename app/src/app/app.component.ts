import { Component, ViewChild } from '@angular/core';
import { Nav, Platform } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { Config } from 'ionic-angular';
import { MainPage } from '../pages/main/main';
import { EventsPage } from '../pages/events/events';


@Component({
  templateUrl: 'app.html' 
})
export class MyApp {
  rootPage:any = MainPage;

  @ViewChild(Nav) nav: Nav;

  constructor(platform: Platform, statusBar: StatusBar, splashScreen: SplashScreen) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      statusBar.styleDefault();
      splashScreen.hide();
      sessionStorage.setItem("server", "http://192.168.43.65:5000");
    });
  }
}

