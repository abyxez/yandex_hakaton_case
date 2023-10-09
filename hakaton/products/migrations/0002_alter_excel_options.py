from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excel',
            options={'ordering': ('week',), 'verbose_name': 'Вывод статистики', 'verbose_name_plural': 'Вывод статистики'},
        ),
    ]
