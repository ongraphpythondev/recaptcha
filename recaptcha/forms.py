from django import forms
from captcha.fields import ReCaptchaField

# import for ReCaptchaV3
# from captcha.widgets import ReCaptchaV3


class FormWithCaptcha(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    captcha = ReCaptchaField()

    # widget field for ReCaptchaV3
    # captcha = ReCaptchaField(widget=ReCaptchaV3)
