from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {

    }
    return render(request,'pages/index.html',datas)
def blog(request):
    datas = {

    }
    return render(request,'pages/blog.html',datas)
def blog_details(request):
    datas = {

    }
    return render(request,'pages/blog-details.html',datas)
def club(request):
    datas = {

    }
    return render(request,'pages/club.html',datas)
def contact(request):
    datas = {

    }
    return render(request,'pages/contact.html',datas)
def main(request):
    datas = {

    }
    return render(request,'pages/main.html',datas)
def result(request):
    datas = {

    }
    return render(request,'pages/result.html',datas)
def schedule(request):
    datas = {

    }
    return render(request,'pages/schedule.html',datas)
