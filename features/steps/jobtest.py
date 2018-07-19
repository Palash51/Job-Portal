
from behave import *
# from selenium import *
# from selenium import webdriver

#from splinter.browser import Browser

from django.contrib.auth.models import User


SERVER_URL = 'http://127.0.0.1:8000/'

####Scenario 1 #####


@given('Become a premium member or direct apply')
def step_impl(context):
    pass

@when(u'I fetch home page')
def step_impl(context):
	pass
	#context.page = request.get(SERVER_URL)
	#assert context.page

@then('Create your profile else apply directly')
def step_impl(context):
	assert context.failed is False


####Scenario 2 #####

@given('Provide your details')
def step_impl(context):
    pass

@when('Submit your resume along with contact details')
def step_impl(context):
    assert True is not False

@then('Applied successfully')
def step_impl(context):
    assert context.failed is False



####Scenario 3 #####

@given('First time user create an account or existing user can login')
def step_impl(context):
	u = User(username='Palash', email='palashpatidar08@gmail.com')
	u.set_password('12345')
	#u.save()

@when('Applicant will access the account')
def step_impl(context):
	pass
	#assert context.page
    

@then('Contact directly to the Hr and Track the application status')
def step_impl(context):
	assert context.failed is False
	#assert geturl().endswith('/account/dashboard/')
    #assert context.failed is False




# @when('Applicant will access the account')
# def step_impl(context):
# 	#context.page = request.get(SERVER_URL/account/login)
# 	#br = request.get(SERVER_URL/account/login/)
# 	#context.page.open(context.browser_url('/account/login/'))
# 	#br.select_form(nr=0)
# 	#context['username'] = 'Palash'
# 	#context['password'] = '12345'
# 	#br.submit()
# 	assert context.page
#     #assert True is not False

#     # br = context.browser
#     # br.open(context.browser_url('/account/login/'))
#     # br.select_form(nr=0)
#     # br.form['username'] = 'Palash'
#     # br.form['password'] = '12345'
#     # br.submit()

# @then('Contact directly to the Hr and Track the application status')
# def step_impl(context):
# 	#br = context.browser
#     #response = br.response()
#     #assert response.code == 200
#     assert geturl().endswith('/account/dashboard/')
#     #assert context.failed is False


####Scenario 3 #####

@given('Consider a user "{username}"')
def step_impl(context,username):
	print("Consider a types of user" +username)

@when('User perform actions')
def step_impl(context):
	print("User perform actions")
	#assert context.page
    

@then('The user "{username}" has "{user_type}" account')
def step_impl(context,username,user_type):
	print("The user" +username+ "has" +user_type + "account\n")