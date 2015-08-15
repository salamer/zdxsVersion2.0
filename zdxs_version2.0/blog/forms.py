#-*- coding: UTF-8 -*- 
from django import forms

class BlogForm(forms.Form):
	title=forms.CharField(label="your title",
				required=True,
				error_messages={'required':'请写一个正确的主题'},
				widget=forms.TextInput(attrs={"class":'form-control',"placeholder":"在这里写下你博客的主题"}))
	body=forms.CharField(label="body",
					required=True,
					error_messages={'required':'请写一个正确的博客主体'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"在这里写下你博客的主体","style":"height:400px;"})
				)
	summury=forms.CharField(label="summury",
					required=True,
					error_messages={'required':'简要是必须要的哦'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"请在这里写下你博客的简要","style":"height:200px;"})
				)


	def cleaned_body(self):
		body=self.cleaned_data['body']
		lgt=len(body)
		if lgt<15:
			raise forms.ValidationError("博客必须要长于15个字符")
		return body

class CommentForm(forms.Form):
	comment=forms.CharField(label="comment",
					required=True,
					error_messages={'required':'comment is needed'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"write your comment here","style":"height:150px;"})
				)


	def cleaned_comment(self):
		body=self.cleaned_data['comment']
		lgt=len(body)
		if lgt<5:
			raise forms.ValidationError("body must be more than 5 characters")
		return body
