from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

# Create your models here.
class App(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)
    name = models.CharField(_("App Name"), max_length=100, unique=True)
    desc = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ("user", "name")
    