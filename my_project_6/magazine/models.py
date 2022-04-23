from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    title = models.CharField('Категория', max_length=64)
    description = models.TextField('Описание Категории', max_length=256)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'category'

    def __str__(self):
        return self.title

class Name(models.Model):
    mod_name = models.CharField('Модель товара', max_length=64)
    price=models.PositiveIntegerField('Цена', help_text='Цена товара', blank=True, null=True) 
    mod_detail = models.TextField('Описание Товара', max_length=256)
    mod_date = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория',
        help_text='Выберите категорию',
        related_name='category_name'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='magazine/',
        blank=True
    )

    class Meta:
        verbose_name = 'Молель товара'
        verbose_name_plural = 'Модели товаров'
        default_related_name = 'item_model'

    def __str__(self):
        return self.mod_name

class Item(models.Model):
    STATUS = [
        ('Magaz', 'Magazine'),
        ('Store', 'Store'),
        ('in_magaz', 'From store in magazine'),
        ('wait', 'Purchased and wait in magazine'),
        ('sold', 'Sold in magazine'),
    ]
    # name = models.TextField('Название товара', help_text='Введите название товара', max_length=256)
    name = models.ForeignKey(
        Name,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Модель',
        help_text='Модель товара',
        related_name='model_items'
    )

    serial_num=models.CharField('Серийный номер', max_length=12, blank=True, null=True, unique=True)
    status= models.CharField('Место нахожднения/Статус', max_length=32, choices=STATUS, default='Store')
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null = True,
        verbose_name='Автор',
        related_name='items'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.name.mod_name
