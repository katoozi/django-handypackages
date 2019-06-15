# Generated by Django 2.2.1 on 2019-06-12 07:57

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Text')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Time Create')),
                ('publish_time', models.DateTimeField(verbose_name='Publish Time')),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True, verbose_name='Slug')),
                ('disable', models.BooleanField(default=False, help_text='Prevent blog showing immediately', verbose_name='Disable')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
                ('tags', models.ManyToManyField(blank=True, to='tag.TagModel')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-publish_time',),
                'abstract': False,
            },
        ),
    ]
