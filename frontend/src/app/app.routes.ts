import { Routes } from '@angular/router';
import { MainLayout } from './layout/main-layout/main-layout';
import { authGuard, publicGuard } from './auth.guard';

export const routes: Routes = [
  { 
    path: 'login',    
    loadComponent: () => import('./pages/login/login').then(m => m.Login),    
    canActivate: [publicGuard] 
  },
  { 
    path: 'register', 
    loadComponent: () => import('./pages/register/register').then(m => m.Register), 
    canActivate: [publicGuard] 
  },
  {
    path: '',
    component: MainLayout,
    canActivate: [authGuard],
    children: [
      { path: 'dashboard',       loadComponent: () => import('./pages/dashboard/dashboard').then(m => m.Dashboard) },
      { path: 'products',        loadComponent: () => import('./pages/products/products').then(m => m.Products) },
      { path: 'categories',      loadComponent: () => import('./pages/categories/categories').then(m => m.Categories) },
      { path: 'warehouses',      loadComponent: () => import('./pages/warehouses/warehouses').then(m => m.Warehouses) },
      { path: 'inventory',       loadComponent: () => import('./pages/inventory/inventory').then(m => m.Inventory) },
      { path: 'stock-movements', loadComponent: () => import('./pages/stock-movements/stock-movements').then(m => m.StockMovements) },
      { path: 'orders',          loadComponent: () => import('./pages/orders/orders').then(m => m.Orders) },
      { path: 'customers',       loadComponent: () => import('./pages/customers/customers').then(m => m.Customers) },
      { path: 'suppliers',       loadComponent: () => import('./pages/suppliers/suppliers').then(m => m.Suppliers) },
      { path: 'purchase-orders', loadComponent: () => import('./pages/purchase-orders/purchase-orders').then(m => m.PurchaseOrders) },
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' }
    ]
  },
  { path: '404',  loadComponent: () => import('./pages/not-found/not-found').then(m => m.NotFound) },
  { path: '**',   loadComponent: () => import('./pages/not-found/not-found').then(m => m.NotFound) }
];
