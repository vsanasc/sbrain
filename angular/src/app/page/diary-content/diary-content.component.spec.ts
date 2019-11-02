import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DiaryContentComponent } from './diary-content.component';

describe('DiaryContentComponent', () => {
  let component: DiaryContentComponent;
  let fixture: ComponentFixture<DiaryContentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DiaryContentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DiaryContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
