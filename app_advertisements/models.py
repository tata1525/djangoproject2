from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
User=get_user_model()

def validate_title(title):
    if title.startswith('?'):
        raise ValidationError(
            _('The title cannot start with a question mark'),
        )



class Advertisement(models.Model):
    title=models.CharField("заголовок", max_length=128, validators=[validate_title])
    description=models.TextField("описание")
    price=models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction=models.BooleanField("торг", help_text="отметьте, если торг уместен")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image=models.ImageField('изображение', upload_to='advertisements/')



    class Meta:
        db_table='advertisements'

    def __str__(self):
        return f" id={self.id}, title={self.title}, price={self.price}"


