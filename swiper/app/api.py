from swiper.app.models import User
from swiper.common import errors
from swiper.lib.http import render_json
from swiper.lib.sms import send_verify_code, check_code


def get_ventify_code(request):
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, errors.OK)


def login(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if not check_code(phonenum, vcode):
        user = User.objects.get_or_create(phonenum=phonenum)
        return render_json()
    else:
        return render_json(None, errors.VCODEERROR)


def show_profile(request):
    return render_json()