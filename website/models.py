from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='سایز')

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = ' اطلاعات تکمیلی'
        verbose_name_plural = 'لیست اطلاعات تکمیلی'


class ProductTag(models.Model):
    tag = models.CharField(max_length=200, verbose_name='عنوان تگ')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, verbose_name='سته بندی ')
    product_info = models.OneToOneField(ProductInformation, null=True, blank=True, verbose_name='اطلاعات تکمیلی',
                                        related_name='product_info', on_delete=models.CASCADE)
    product_tag = models.ManyToManyField(ProductTag, verbose_name='عنون محصول')
    title = models.CharField(max_length=50, verbose_name='Tutorial name')
    price = models.IntegerField(verbose_name='Tutorial price')
    description = models.CharField(max_length=300, verbose_name='Tutorial description')
    is_active = models.BooleanField(verbose_name='active/notactive')
    ratings = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)],
                                  verbose_name='rating product')
    slug = models.SlugField(max_length=400, unique=True, default='', null=False, db_index=True,
                            verbose_name='title in url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}---{self.price}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('product-detail', args={self.slug})

# class Karbaran(models.Model):
#     name = models.CharField(max_length=20)
#     family = models.CharField(max_length=20)
#     age = models.IntegerField()
#     # emailk=models.EmailField()
#     is_active = models.BooleanField()
