from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(res):
	if res.method == "POST":
		form = RegisterForm(res.POST)
		if form.is_valid():	
			form.save()
			return redirect("http://localhost:3000")

		return redirect("#")
	form = RegisterForm()
	params = {
		"form": form
	}

	return render(res, "register/register.html", params)