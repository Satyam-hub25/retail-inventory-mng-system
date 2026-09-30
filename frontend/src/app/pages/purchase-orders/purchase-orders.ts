import { Component, OnInit , ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PurchaseOrderService } from '../../services/purchase-order';
import { ToastService } from '../../services/toast';

@Component({
  selector: 'app-purchase-orders',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './purchase-orders.html',
  styleUrls: ['./purchase-orders.scss']
})
export class PurchaseOrders implements OnInit {
  purchaseOrders: any[] = [];
  loading = false;
  saving = false;
  error = '';

  showForm = false;
  editingPO: any = null;
  formData: any = { supplierId: null, orderDate: '', status: 'PENDING', totalAmount: 0 };
  formError = '';

  deleteTarget: any = null;
  deleteConfirming = false;

  constructor(private poService: PurchaseOrderService, private toast: ToastService, private cdr: ChangeDetectorRef) {}

  ngOnInit() { this.loadPOs(); }

  loadPOs() {
    this.loading = true;
    this.error = '';
    this.poService.getAll().subscribe({
      next: (data) => { this.purchaseOrders = data; this.loading = false; this.cdr.detectChanges(); },
      error: (err) => {
        this.error = 'Failed to load purchase orders.';
        this.loading = false; this.cdr.detectChanges(); this.toast.error(this.error);
      }
    });
  }

  openAddForm() {
    this.editingPO = null;
    this.formData = { supplierId: null, orderDate: new Date().toISOString().slice(0,10), status: 'PENDING', totalAmount: 0 };
    this.formError = '';
    this.showForm = true; this.cdr.detectChanges(); }

  editPO(po: any) {
    this.editingPO = po;
    this.formData = { ...po };
    this.formError = '';
    this.showForm = true; this.cdr.detectChanges(); }

  closeForm() {
    this.showForm = false; this.cdr.detectChanges(); this.editingPO = null;
    this.formError = '';
  }

  savePO() {
    this.saving = true;
    this.formError = '';
    const action = this.editingPO
      ? this.poService.update(this.editingPO.id, this.formData)
      : this.poService.create(this.formData);

    action.subscribe({
      next: () => {
        this.toast.success(this.editingPO ? 'Purchase Order updated!' : 'Purchase Order created!');
        this.loadPOs();
        this.closeForm();
        this.saving = false; this.cdr.detectChanges(); },
      error: (err) => {
        this.formError = err.error?.message || 'Failed to save purchase order.';
        this.toast.error(this.formError);
        this.saving = false; this.cdr.detectChanges(); }
    });
  }

  confirmDelete(po: any) {
    this.deleteTarget = po;
    this.deleteConfirming = true; this.cdr.detectChanges(); }

  cancelDelete() {
    this.deleteTarget = null; this.cdr.detectChanges(); this.deleteConfirming = false; this.cdr.detectChanges(); }

  executeDelete() {
    if (!this.deleteTarget) return;
    this.poService.delete(this.deleteTarget.id).subscribe({
      next: () => {
        this.toast.success('Purchase Order deleted successfully.');
        this.loadPOs();
        this.cancelDelete();
      },
      error: (err) => {
        this.toast.error('Failed to delete purchase order.');
        this.cancelDelete();
      }
    });
  }
}
