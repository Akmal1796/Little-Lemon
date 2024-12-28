API ENDPOINTS

GET /menu/ for listing all menu items.
POST /menu/ with a JSON payload to create a new menu item.
GET /menu/<id>/ to retrieve a single menu item by ID.
PUT /menu/<id>/ to update an existing menu item.
DELETE /menu/<id>/ to delete a menu item.

admin/
[name='home']
about/ [name='about']
book/ [name='book']
reservations/ [name='reservations']
menu/ [name='menu']
menu_item/<int:pk>/ [name='menu_item']
bookings [name='bookings']
api-token-auth/ [name='api_token_auth']
auth/
auth/
