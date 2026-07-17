from django.contrib import admin
from .models import Topic, Entry

# 在这里注册你的模型
admin.site.register(Topic)
admin.site.register(Entry)
