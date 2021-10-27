from django.db import models
from apps.models import App
from plans.models import Plan
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Subscription(models.Model):
    app = models.OneToOneField(App, verbose_name=_("App"), on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, verbose_name=_("Plan"), on_delete=models.CASCADE)
    active = models.BooleanField(_("Is Active"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    def __str__(self):
        return self.app.name
    