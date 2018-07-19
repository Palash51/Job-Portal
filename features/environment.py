
# from splinter.browser import Browser

# def before_all(context):
#     context.browser = Browser()

# def after_all(context):
#     context.browser.quit()
#     context.browser = None










# from selenium import webdriver
# # from short.models import Entry


# def before_all(context):
#     context.browser = webdriver.Chromium(executable_path=r'geckodriver.exe')
#     context.browser.implicitly_wait(3)
#     context.HOMEPAGE = 'http://127.0.0.1:8000/'

# #    Entry.objects.create(
# #                    url="http://pythonhosted.org/behave/tutorial.html#python-step-implementations")
# #    Entry.objects.create(
# #                    url="http://selenium-python.readthedocs.org/en/latest/getting-started.html")


# def after_all(context):
#     context.browser.quit()


# def before_feature(context, feature):
#     pass












# from splinter.browser import Browser

# def before_all(context):
#     context.browser = Browser()

# def after_all(context):
#     context.browser.quit()
#     context.browser = None













# from __future__ import absolute_import
# import os
# import django
# from django.conf import settings
# from django.test.utils import get_runner


# os.environ['DJANGO_SETTINGS_MODULE'] = 'behave_dj.settings'


# def before_all(context):
#     if not settings.configured:
#         # from behave_dj import settings as _settings
#         settings.configure(DEBUG=True)
#     django.setup()
#     context.runner = get_runner(settings)()


# def before_scenario(context, scenario):
#     #context.runner.setup_test_environment()
#     context.old_db_config = context.runner.setup_databases()
#     from django.test import Client
#     context.browser = Client()


# def after_scenario(context, scenario):
#     context.runner.teardown_databases(context.old_db_config)
#     context.runner.teardown_test_environment()