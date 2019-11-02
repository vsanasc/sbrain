import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MainDashboardComponent } from './main-dashboard/main-dashboard.component';
import { FinanceTableComponent } from './finance-table/finance-table.component';
import { DiaryContentComponent } from './diary-content/diary-content.component';

const components = [MainDashboardComponent, FinanceTableComponent, DiaryContentComponent]

@NgModule({
  declarations: components,
  exports: components,
  providers: [],
  imports: [
    CommonModule
  ]
})
export class PageModule { }
