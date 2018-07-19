# from behave import given, when, then

# @given('a user')
# def step_impl(context):
#     from django.contrib.auth.models import User
#     u = User(username='Palash', email='palashpatidar08@gmail.com')
#     u.set_password('12345')

# @when('I log in')
# def step_impl(context):
#     br = context.browser
#     br.open(context.browser_url('/account/login/'))
#     br.select_form(nr=0)
#     br.form['username'] = 'Palash'
#     br.form['password'] = '12345'
#     br.submit()

# @then('I see my Dashboard ')
# def step_impl(context):
#     br = context.browser
#     response = br.response()
#     assert response.code == 200
#     assert br.geturl().endswith('/account/dashboard/')