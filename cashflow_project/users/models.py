from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомная модель пользователя, для возможного расширения в будущем."""
    
    def __str__(self):
        return self.username