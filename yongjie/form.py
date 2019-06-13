from django import forms
from django.forms import  widgets
from django.core.exceptions import ValidationError
import re

class PriceForm(forms.Form):

    def mobile_validate(value):
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(value):
            raise ValidationError('手机号码格式错误')

    area = forms.CharField(
            max_length=12,
            widget=widgets.TextInput(),
            error_messages={'required':'车间面积不能为空',
                            'max_length':'最大不得超过1000000',
                            })

    level = forms.IntegerField(
            widget=widgets.TextInput(),
            error_messages={'required': '净化级别不能为空',})

    name = forms.CharField(
        max_length=12,
        widget=widgets.TextInput(),
        error_messages={'required': '姓名不能为空',
                        'max_length': '最大长度不能超过30个字符',
                        })

    sex = forms.IntegerField(
        widget=widgets.TextInput(),
        error_messages={'required': '性别', })

    mobile = forms.CharField(
        validators=[mobile_validate, ],
        max_length=12,

        widget=widgets.TextInput({'placeholder': '填写手机号码', }),
        error_messages={'required': '用户名不能为空',
                        'max_length': '最大长度不得超过12个字符',
                        })
