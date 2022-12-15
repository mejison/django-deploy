from django.contrib import admin

from .models import Product
from .models import Auction
from .models import Question
from .models import Answers
#from .models import NewUser
# Register your models here.

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Question)
admin.site.register(Answers)
#admin.site.register(NewUser)