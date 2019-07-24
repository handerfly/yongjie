from .home.models import Head_img

def head_img(request):
    head_img = Head_img.objects.all().first()
    return {"head_img":head_img.image}