import { Component, EventEmitter, inject, Input, OnInit, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Auth } from '../../services/auth';

@Component({
  selector: 'app-topbar',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topbar.html',
  styleUrl: './topbar.scss'
})
export class Topbar implements OnInit {
  private authService = inject(Auth);

  @Input() isSidebarHidden = false;
  @Output() toggleSidebar = new EventEmitter<void>();

  currentUser: any = null;
  userInitials: string = 'U';

  ngOnInit() {
    this.authService.currentUser$.subscribe(user => {
      this.currentUser = user;
      if (user?.name) {
        this.userInitials = user.name
          .split(' ')
          .map((n: string) => n[0])
          .join('')
          .toUpperCase()
          .slice(0, 2);
      }
    });
  }

  onToggleSidebar() {
    this.toggleSidebar.emit();
  }
}
