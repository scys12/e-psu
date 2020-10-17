## Install Dependency
Run ```pip install -r requirements.txt```.

## Test account ##
Run ```python manage.py shell```.

### Create Admin Kelola Account for SuperUser

```python
from account.models import Account
from django.utils import timezone
from admin_kelola.models import AdminKelola
account = Account.objects.create_superuser(username='kelola',password='kelola',email='kelola@kelola.com', user_type=1)
AdminKelola.objects.create(user=account, nama='kelola')
```

### Create Admin SKPD Account for SuperUser

```python
from account.models import Account
from django.utils import timezone
from admin_skpd.models import AdminSKPD
account = Account.objects.create_superuser(username='skpd',password='skpd',email='skpd@skpd.com', user_type=3)
AdminSKPD.objects.create(user=account, nama='skpd')
```