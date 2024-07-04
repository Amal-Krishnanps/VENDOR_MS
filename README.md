# Vendor Management System with Performance Metrics
This Django REST framework project will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Setup Instructions
**1. Clone the Repository**

    git clone https://github.com/Amal-Krishnanps/VENDOR_MS.git
    
    cd vendor_management

**2. Create a Virtual Environment**
   
     python -m venv venv
   
 **3. Activate the Virtual Environment**
 
      On Windows:
      venv\Scripts\activate
     
      On macOS/Linux:
      source venv/bin/activate
   
**4. Install Dependencies**

      pip install -r requirements.txt

**5. Apply Migrations**

     python manage.py migrate

**6. Create Superuser**

     python manage.py createsuperuser

**7. Run the Development Server**

     python manage.py runserver

Visit http://127.0.0.1:8000/ to view the API.

### API Endpoints

**1. Vendor Profile Management**
   
   **Create Vendor**
    
    Method: POST
    URL: /api/vendors/
    Payload: Provide vendor details in the request body.

  **List All Vendors**

    Method: GET
    URL: /api/vendors/

  **Retrieve Vendor Details**

    Method: GET
    URL: /api/vendors/{vendor_id}/

  **Update Vendor Details**

    Method: PUT
    URL: /api/vendors/{vendor_id}/
    Payload: Provide updated vendor details in the request body.

  **Delete Vendor**

    Method: DELETE
    URL: /api/vendors/{vendor_id}/

  **Retrieve Vendor Performance Metrics**
  
    Method: GET
    URL: /api/vendors/{vendor_id}/performance/
    
**2. Purchase Order Tracking**

  **Create Purchase Order:**
  
      Method: POST
      URL: /api/purchase_orders/
      Payload: Provide purchase order details in the request body.

  **List All Purchase Orders**
  
      Method: GET
      URL: /api/purchase_orders/

  **Retrieve Purchase Order Details**
  
      Method: GET
      URL: /api/purchase_orders/{po_id}/

  **Update Purchase Order**
  
      Method: PUT
      URL: /api/purchase_orders/{po_id}/
      Payload: Provide updated purchase order details in the request body.

  **Delete Purchase Order**
  
      Method: DELETE
      URL: /api/purchase_orders/{po_id}/

**3. Historical Performance**

  **Retrieve Historical Performance**
  
    Method: GET
    URL: /api/vendors/historical_performance/

  **Authentication**

Authentication is required for certain endpoints. Use the credentials of the superuser created during setup.



