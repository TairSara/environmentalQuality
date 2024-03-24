from django.contrib import admin
from .models import User, products, usersContacts, usersrecycling,userpoint

# admin.site.register(website_products)
class ProductAdmin(admin.ModelAdmin):
  list_display = ("product_name", "Product_type", "value", "bin_type",)

class usersContactsAdmin(admin.ModelAdmin):
  list_display = ("id", "creationDT", "user", "content", "status",)

class usersAdmin(admin.ModelAdmin):
  list_display = ("id", "username", "user_type", "location", "is_superuser")

class usersrecyclingAdmin(admin.ModelAdmin):
  list_display = ("creationDT", "user", "product", "userImg", "status",)

class userpointAdmin(admin.ModelAdmin):
  list_display = ("id", "user", "points")

admin.site.register(products, ProductAdmin)
admin.site.register(User, usersAdmin)
admin.site.register(usersContacts, usersContactsAdmin)
admin.site.register(usersrecycling, usersrecyclingAdmin)
admin.site.register(userpoint, userpointAdmin)

