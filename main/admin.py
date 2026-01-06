from django.contrib import admin
from .models import Category,Size,Product,ProductImage,ProductSize



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
#В первую очередь я написал инлайны для того чтобы можно было делать добовлять изображениея к данному товару прямо из админки товара

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
# я написал инлайн продукт сайз для того чтобы можно было дабовлять размеры товара прямо из меню добавления товара в админке

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','color','price'] #лист фильтер я использовал для того чтобы показать тебе параметры которые нужны
    list_filter = ['category','color']
    search_fields = ['name','color','description']
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductImageInline,ProductSizeInline] # в поле inlines  я указал какие модели я хочу видеть в админке когда дабовляю товар



class CategoryAdmin(admin.ModelAdmin): #это отдельная модель для дабовления котегорий товарая
    list_display = ['name','slug'] #лист  дисплэй нужен для того чтобы я мог указать какие поля модели я хочу видеть в админке
    prepopulated_fields = {'slug':('name',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
     

admin.site.register(Category,CategoryAdmin) # вот тут я зарегистрировал модель и указал какие настройки должны быть у модели в админке
admin.site.register(Size,SizeAdmin)
admin.site.register(Product,ProductAdmin)