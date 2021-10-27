from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Plan(models.Model):
    name = models.CharField(_("Plan Name"), max_length=50)
    price = models.DecimalField(_("Plan Price"), max_digits=5, decimal_places=2)
    desc = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    def __str__(self):
        return self.name