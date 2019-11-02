import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { AppLayoutComponent } from './app-layout/app-layout.component';
import { AppHeaderComponent } from './app-header/app-header.component';
import { AppFooterComponent } from './app-footer/app-footer.component';
import { AppSidebarComponent } from './app-sidebar/app-sidebar.component';
import { AppNavbarComponent } from './app-navbar/app-navbar.component';

@NgModule({
  declarations: [
    AppLayoutComponent, 
    AppHeaderComponent, 
    AppFooterComponent, 
    AppSidebarComponent, AppNavbarComponent
  ],
  imports: [
    CommonModule,
    RouterModule
  ],
  exports: [
    AppLayoutComponent, 
    AppHeaderComponent, 
    AppFooterComponent, 
    AppSidebarComponent
  ]
})
export class LayoutModule { }
