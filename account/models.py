from django.db import models
from django.contrib.auth import models as auth_models


class StudyGroup(models.Model):
    name = models.CharField(max_length=20)


class User(auth_models.AbstractUser):
    """
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    """

    active_test = models.PositiveIntegerField(blank=True, null=True)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True)


def __str__(self):
    return self.title
