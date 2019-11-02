import { Component, OnInit } from '@angular/core';
import { DiaryService } from '../../service/diary.service';

@Component({
  selector: 'app-diary-content',
  templateUrl: './diary-content.component.html',
  styleUrls: ['./diary-content.component.styl']
})
export class DiaryContentComponent implements OnInit {

  constructor(private service: DiaryService) { 
  }

  ngOnInit() {

    this.service.fetch()
  }

}
