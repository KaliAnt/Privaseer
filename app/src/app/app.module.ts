import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { AlertController } from 'ionic-angular';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';

import { MyApp } from './app.component';
import { MainPage } from '../pages/main/main';
import { HomePage } from '../pages/home/home';
import { TabsPage } from '../pages/tabs/tabs';
import { SettingsPage } from '../pages/settings/settings';
import { EventsPage } from '../pages/events/events';

import { HttpClientModule } from '@angular/common/http';


import { UserProvider } from '../providers/user/user';
import { EventProvider } from '../providers/event/event';



@NgModule({
  declarations: [
    MyApp,
    MainPage,
    HomePage,
    TabsPage,
    SettingsPage,
    EventsPage
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    MainPage,
    HomePage,
    TabsPage,
    SettingsPage,
    EventsPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    { provide: ErrorHandler, useClass: IonicErrorHandler },
    UserProvider,
    AlertController,
    EventProvider
  ]
})
export class AppModule {}
