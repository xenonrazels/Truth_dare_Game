from django.contrib import admin
from .models import Players,TruthQuestion,DareQuestion,Game_board
# Register your models here.
admin.site.register(Players)
admin.site.register(TruthQuestion)
admin.site.register(DareQuestion)
admin.site.register(Game_board)