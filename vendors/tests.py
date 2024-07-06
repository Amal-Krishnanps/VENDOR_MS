from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Vendor, PurchaseOrder, HistoricalPerformance


class VendorManagementTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.vendor_data = {
            'name': 'Test Vendor',
            'contact_details': 'test@example.com',
            'address': '123 Test St',
            'vendor_code': 'VEND123'
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.purchase_order_data = {
            'po_number': 'PO123',
            'vendor': self.vendor,
            'order_date': '2023-01-01T00:00:00Z',
            'delivery_date': '2023-01-10T00:00:00Z',
            'items': {'item1': 10, 'item2': 20},
            'quantity': 30,
            'status': 'pending',
            'issue_date': '2023-01-01T00:00:00Z'
        }
        self.purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)

    def test_create_vendor(self):
        url = reverse('vendor_list_create')
        data = {
            'name': 'New Vendor',
            'contact_details': 'new@example.com',
            'address': '456 New St',
            'vendor_code': 'VEND456'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_list_vendors(self):
        url = reverse('vendor_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_vendor(self):
        url = reverse('vendor_detail', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.vendor.name)

    def test_update_vendor(self):
        url = reverse('vendor_detail', kwargs={'pk': self.vendor.pk})
        data = {'name': 'Updated Vendor'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, 'Updated Vendor')

    def test_delete_vendor(self):
        url = reverse('vendor_detail', kwargs={'pk': self.vendor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)
        
        
    def test_create_purchase_order(self):
        url = reverse('purchase_order_list_create')
        data = {
            'po_number': 'PO456',
            'vendor': self.vendor.pk,
            'order_date': '2023-02-01T00:00:00Z',
            'delivery_date': '2023-02-10T00:00:00Z',
            'items': {'item1': 'test item'},
            'quantity': 20,
            'status': 'pending',
            'issue_date': '2023-02-01T00:00:00Z'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)

    def test_list_purchase_orders(self):
        url = reverse('purchase_order_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_purchase_order(self):
        url = reverse('purchase_order_detail', kwargs={'pk': self.purchase_order.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['po_number'], self.purchase_order.po_number)

    def test_update_purchase_order(self):
        url = reverse('purchase_order_detail', kwargs={'pk': self.purchase_order.pk})
        data = {'status': 'Completed'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertEqual(self.purchase_order.status, 'Completed')

    def test_delete_purchase_order(self):
        url = reverse('purchase_order_detail', kwargs={'pk': self.purchase_order.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
