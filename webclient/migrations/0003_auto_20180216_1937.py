# Generated by Django 2.0.1 on 2018-02-16 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '0002_categorytype_label_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelShapes', models.TextField(max_length=10000)),
                ('categoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.CategoryType')),
            ],
        ),
        migrations.RenameField(
            model_name='imagelabel',
            old_name='labelShapes',
            new_name='combined_labelShapes',
        ),
        migrations.RemoveField(
            model_name='imagelabel',
            name='categoryType',
        ),
        migrations.AddField(
            model_name='categorylabel',
            name='parent_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.ImageLabel'),
        ),
    ]
