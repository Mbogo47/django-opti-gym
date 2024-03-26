from . import models

def get_logo(request):
    logo = models.AppSetting.objects.first()
    if logo:
        data = {
            'logo': logo.image_tag
        }
    else:
        data = {
            'logo': None  # or any default value you want to assign
        }
    return data
