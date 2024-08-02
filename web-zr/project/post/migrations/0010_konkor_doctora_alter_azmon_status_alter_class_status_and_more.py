# Generated by Django 5.0.3 on 2024-04-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_emtehan_nahaii_alter_jozve_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konkor_doctora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to='', verbose_name='تصویر')),
                ('news', models.TextField(verbose_name='اخبار')),
                ('video', models.FileField(blank=True, default=None, upload_to='', verbose_name='ویدیو خود را وارد کنید')),
            ],
        ),
        migrations.AlterField(
            model_name='azmon',
            name='status',
            field=models.CharField(choices=[('Ministry of Science 1', 'زیر گروه یک وزارت بهداشت'), ('Ministry of Science 2', 'زیر گروه دو وزارت بهداشت'), ('Ministry of Science 3', 'زیر گروه سه وزارت بهداشت'), ('Ministry of Science 3', '(رشته های شناور) وزارت بهداشت'), ('Ministry of Health 1', 'وزارت علوم'), ('doctora', 'دکتری'), ('experimental', 'تجربی'), ('Math', 'ریاضی'), ('Humanities', 'انسانی'), ('art field', 'هنر'), ('First high school', 'متوسطه اول'), ('second high school', 'متوسطه دوم')], default='تجربی', max_length=60, verbose_name='مشخصات گروه'),
        ),
        migrations.AlterField(
            model_name='class',
            name='status',
            field=models.CharField(choices=[('Ministry of Science 1', 'زیر گروه یک وزارت بهداشت'), ('Ministry of Science 2', 'زیر گروه دو وزارت بهداشت'), ('Ministry of Science 3', 'زیر گروه سه وزارت بهداشت'), ('Ministry of Science 3', '(رشته های شناور) وزارت بهداشت'), ('Ministry of Health 1', 'وزارت علوم'), ('doctora', 'دکتری'), ('experimental', 'تجربی'), ('Math', 'ریاضی'), ('Humanities', 'انسانی'), ('art field', 'هنر'), ('First high school', 'متوسطه اول'), ('second high school', 'متوسطه دوم')], default='تجربی', max_length=60, verbose_name='مشخصات گروه'),
        ),
        migrations.AlterField(
            model_name='jozve',
            name='status',
            field=models.CharField(choices=[('Ministry of Science 1', 'زیر گروه یک وزارت بهداشت'), ('Ministry of Science 2', 'زیر گروه دو وزارت بهداشت'), ('Ministry of Science 3', 'زیر گروه سه وزارت بهداشت'), ('Ministry of Science 3', '(رشته های شناور) وزارت بهداشت'), ('Ministry of Health 1', 'وزارت علوم'), ('doctora', 'دکتری'), ('experimental', 'تجربی'), ('Math', 'ریاضی'), ('Humanities', 'انسانی'), ('art field', 'هنر'), ('First high school', 'متوسطه اول'), ('second high school', 'متوسطه دوم')], default='تجربی', max_length=60, verbose_name='مشخصات گروه'),
        ),
        migrations.AlterField(
            model_name='moshavere',
            name='status',
            field=models.CharField(choices=[('Ministry of Science 1', 'زیر گروه یک وزارت بهداشت'), ('Ministry of Science 2', 'زیر گروه دو وزارت بهداشت'), ('Ministry of Science 3', 'زیر گروه سه وزارت بهداشت'), ('Ministry of Science 3', '(رشته های شناور) وزارت بهداشت'), ('Ministry of Health 1', 'وزارت علوم'), ('doctora', 'دکتری'), ('experimental', 'تجربی'), ('Math', 'ریاضی'), ('Humanities', 'انسانی'), ('art field', 'هنر'), ('First high school', 'متوسطه اول'), ('second high school', 'متوسطه دوم')], default='تجربی', max_length=60, verbose_name='مشخصات گروه'),
        ),
        migrations.AlterField(
            model_name='nafarat',
            name='status',
            field=models.CharField(choices=[('Ministry of Science 1', 'زیر گروه یک وزارت بهداشت'), ('Ministry of Science 2', 'زیر گروه دو وزارت بهداشت'), ('Ministry of Science 3', 'زیر گروه سه وزارت بهداشت'), ('Ministry of Science 3', '(رشته های شناور) وزارت بهداشت'), ('Ministry of Health 1', 'وزارت علوم'), ('doctora', 'دکتری'), ('experimental', 'تجربی'), ('Math', 'ریاضی'), ('Humanities', 'انسانی'), ('art field', 'هنر'), ('First high school', 'متوسطه اول'), ('second high school', 'متوسطه دوم')], default='تجربی', max_length=60, verbose_name='مشخصات گروه'),
        ),
    ]