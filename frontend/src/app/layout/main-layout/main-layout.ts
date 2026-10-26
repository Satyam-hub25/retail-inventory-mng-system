import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { Sidebar } from '../sidebar/sidebar';
import { Topbar } from '../topbar/topbar';

@Component({
  selector: 'app-main-layout',
  standalone: true,
  imports: [CommonModule, RouterOutlet, Sidebar, Topbar],
  templateUrl: './main-layout.html',
  styleUrl: './main-layout.scss'
})
export class MainLayout implements OnInit {
  isSidebarHidden = false;

  ngOnInit() {
    const saved = localStorage.getItem('sidebar_hidden');
    if (saved !== null) {
      this.isSidebarHidden = saved === 'true';
    }
  }

  toggleSidebar() {
    this.isSidebarHidden = !this.isSidebarHidden;
    localStorage.setItem('sidebar_hidden', String(this.isSidebarHidden));
  }
}
