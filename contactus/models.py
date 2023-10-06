from django.db import models

class ContactUs(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    email=models.EmailField(max_length=300,verbose_name='ایمیل')
    fullname=models.CharField(max_length=300,verbose_name='نام و نام خانوادگی')
    message=models.TextField(verbose_name='متن پیام')
    createtd_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    response=models.TextField(verbose_name='متن پاسخ')
    is_read_by_admin=models.BooleanField(default=False,verbose_name='حوانده شده توسط ادمین')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='لیست تماس با ما '