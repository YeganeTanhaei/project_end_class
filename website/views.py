from django.db.models import Avg, Max, Min
from django.shortcuts import get_object_or_404, render

from .models import Product


def product_List(request):
    all_product = Product.objects.all().order_by('-price')
    number_of_product=all_product.count()
    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))
    return render(request, 'website/product_list.html', {'all_product': all_product,
                                                       'number_of_product':number_of_product,
                                                       'average':info})
#or
# class Product_List(ListView):
#     model = Product
#     template_name = 'blogs/product_list.html'
#     context_object_name = 'all_product'

def product_detail(request,slug):
    # try:
    #     products = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    products =get_object_or_404(Product,slug=slug)
    return render(request, 'website/product_detail.html',context={'product': products})