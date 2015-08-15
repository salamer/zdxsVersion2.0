#-*- coding: UTF-8 -*- 

from django import forms
from django.contrib.auth.models import User
import re

class LoginForm(forms.Form):
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上你的正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"placeholder":"邮箱"}))
	password=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你正确的密码'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"密码"})
				)
		

class RegisterForm(forms.Form):
	name=forms.CharField(label="your name",
				max_length=100,
				required=True,
				error_messages={'required':'请写上名字!'},
				widget=forms.TextInput(attrs={'class':"form-control","placeholder":"写下你的姓名"}))
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"placeholder":"写下你的邮箱，邮箱用来登录"}))
	password1=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你的密码'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"你的密码"})
				)
	password2=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请再输入一次'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"检查密码"})
				)

	def clean_name(self):
		name=self.cleaned_data['name']
		if ' ' in name:
			raise forms.ValidationError('不能有空格')
		if not re.search(r'^\w+$',name):
			raise forms.ValidationError('名字只能是字母或数字')
		return name

	def clean_password1(self):
		password=self.cleaned_data['password1']
		cha_num=len(password)
		if cha_num<6:
			raise forms.ValidationError("密码应该大于6个字符")
		return password

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			user=User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('该邮箱已经被注册了')

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
			raise forms.ValidationError('两次密码输入不一致')
		
