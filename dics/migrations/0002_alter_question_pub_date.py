from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]