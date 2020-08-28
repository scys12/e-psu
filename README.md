e-psu

## Test account ##
Run ```python manage.py shell```

```python
from account.models import Account
from django.utils import timezone
Account.objects.create_superuser(username='testing',password='testing',email='testing@testing.com')
```