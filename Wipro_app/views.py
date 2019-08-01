from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Category, Question, Organization, Assessment, questions_list
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from django.contrib.auth.models import AbstractUser

def login(request):
	return render(request, 'registration/login.html')


def AddOrg(request):
	if request.method == 'POST':
		if request.POST.get('orgname') and request.POST.get('businessID')and request.POST.get('location'):
			org = Organization()
			org.name = request.POST.get('orgname')
			org.OrgID = request.POST.get('businessID')
			org.OrgLocation = request.POST.get('location')
			org.OrgSize = request.POST.get('size_dd')
			org.OrgDomain = request.POST.get('domain_dd')
			org.save()

			return render(request, 'registration/AddOrg.html')

	else:
		return render(request, 'registration/AddOrg.html')


def MyHistory(request):
	return render(request, 'registration/MyHistory.html')


def ColleagueHistory(request):
	return render(request, 'registration/ColleagueHistory.html')


def home(request):
	if request.user.new == 'True':
		return change_password(request)
	else:
		return render(request, 'home.html')


def Profile(request):
	return render(request, 'registration/Profile.html')


def ForgetPassword(request):
	return render(request, 'registration/ForgetPassword.html')

def add_category(request):
	if request.method == 'POST':
		if request.POST.get('category_name'):
			cat = Category()
			cat.name = request.POST.get('category_name')
			cat.save()
	return render(request, 'add_category.html')

def add_question(request):
	item = Category.objects.all()
	if request.method == 'POST':
		selected_item = get_object_or_404(Category, pk=request.POST.get('item_id'))
		if request.POST.get('question_name','item_id'):
			cat = Question()
			cat.name = request.POST.get('question_name')
			cat.category = selected_item
			cat.category_name = selected_item.name
			cat.save()
	return render(request, 'add_question.html', {'item': item})

def assessment(request):
	questions = Question.objects.all()
	item = Organization.objects.all()
	if request.method == 'POST':

		if request.POST.get('item_id'):
			cat = Assessment()
			mouse = questions_list()
			# cat.org_ID = selected_item
			# cat.user_ID = request.user.id
			# mouse.assessment_ID = cat.id
			# mouse.rating = request.POST.get('item_id')
			# mouse.question_ID =
			# mouse.question_name =
			# mouse.question_category_name =
			mouse.save( )
			# cat.save()
	return render(request, 'registration/Assessment.html',{'item': item,'questions': questions})


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			request.user.new = 'False'
			request.user.save()
			return redirect('login')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'registration/change_password.html', {
		'form': form
	})
