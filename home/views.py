from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import comment,product_details
# Create your views here.

def sell(request):
    if request.method == 'POST':

        product_name1=request.POST.get('product_name')
        short_des1=request.POST.get('product_short')
        long_des1=request.POST.get('product_des')
        product_condition1=request.POST.get('product_condition')
        seller_type1=request.POST.get('seller_type')
        seller_department1=request.POST.get('seller_department')
        borrow_amount1=request.POST.get('borrow_amount')
        buy_amount1=request.POST.get('buy_amount')
        seller_comment1=request.POST.get('seller_comment')
        seller_name1=request.POST.get('seller_name')
        seller_mail1=request.POST.get('seller_mail')
        product_img1=request.POST.get('product_url')
        obj = product_details(product_name=product_name1,short_des=short_des1,long_des=long_des1,product_condition=product_condition1,seller_type=seller_type1,seller_department=seller_department1,borrow_amount=borrow_amount1,buy_amount=buy_amount1,seller_comment=seller_comment1,seller_name=seller_name1,seller_mail=seller_mail1,product_img=product_img1,product_views=1,interactions=0)
        
        try:
            obj.save()
        except:
            print("some error occured")
    return render(request,'Form.html')
def calculate_similarity2(str1, str2):
    new_str1 = (str1.replace(" ", "")).lower()
    new_str2 = (str2.replace(" ", "")).lower()
    len_str1 = len(new_str1)
    if new_str1 in new_str2:
        return 0
    count = 0
    for i in range(0,len_str1):
        for j in range(i+1,len_str1):
            if new_str1[i:j] in new_str2:
                count = max(count,j-i)
    return (count/len_str1)*100
def calculate_similarity(str1, str2):
    new_str1 = (str1.replace(" ", "")).lower()
    new_str2 = (str2.replace(" ", "")).lower()
    if new_str1 in new_str2:
        return 100
    return 0
def searched(request):
    if request.method == 'POST':
        # if request.method == "POST":
        search_text=request.POST.get('search_text','')
        all_products = product_details.objects.all()
        matching_products = [product for product in all_products if calculate_similarity(search_text, product.product_name) >= 50]
        matching_products.extend([product for product in all_products if calculate_similarity2(search_text, product.product_name) >= 40])
        return render(request,'search_template.html',{"all_products":matching_products})
    return HttpResponse("page couldn't be loaded directly")

def index(request):
    p = product_details.objects.all()
    obj = {
        "all_products":p
    }
    return render(request,'index.html',obj)
def product(request,pk):
    if request.method=="POST":
        comment1 = request.POST.get('comment1')
        pr_n = request.POST.get('pr_name')
        comment2 = comment(comment = comment1,date=datetime.today(),pr_name=pr_n)
        comment2.save()
        c = comment.objects.all()
        temp = product_details.objects.all()
        for i in temp:
            if i.product_name==pr_n:
                i.interactions += 1
                i.save()
                context = {
                    "product_name":i.product_name,
                    "short_des":i.short_des,
                    "long_des":i.long_des,
                    "product_condition":i.product_condition,
                    "seller_type":i.seller_type,
                    "seller_department":i.seller_department,
                    "borrow_amount":i.borrow_amount,
                    "buy_amount":i.buy_amount,
                    "seller_comment":i.seller_comment,
                    "seller_name":i.seller_name,
                    "seller_mail":i.seller_mail,
                    "product_img":i.product_img,
                    'comm':c,
                    "test":i
                }
                return render(request,'base.html',context)
    c = comment.objects.all()
    i = product_details.objects.get(pk=pk)
    
    i.product_views += 1
    
    i.save()
    context = {
        "product_name":i.product_name,
        "short_des":i.short_des,
        "long_des":i.long_des,
        "product_condition":i.product_condition,
        "seller_type":i.seller_type,
        "seller_department":i.seller_department,
        "borrow_amount":i.borrow_amount,
        "buy_amount":i.buy_amount,
        "seller_comment":i.seller_comment,
        "seller_name":i.seller_name,
        "seller_mail":i.seller_mail,
        "product_img":i.product_img,
        'comm':c,
        "test":i,
    }
    return render(request,'base.html',context)
def trending(request):
    p = product_details.objects.all().order_by('-product_views')[:4]
    obj = {
        "all_products":p
    }
    return render(request,'trending.html',obj)

    

