# Generated by Django 4.2.3 on 2023-07-17 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='icons/default_icons/image_missing.jpg', upload_to='icons')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('actors', models.ManyToManyField(blank=True, to='main.actor')),
            ],
            options={
                'verbose_name': 'Аниме',
                'verbose_name_plural': 'Аниме',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автор',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='icons/default_icons/image_missing.jpg', upload_to='icons')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='icons/default_icons/image_missing.jpg', upload_to='icons')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author')),
                ('categories', models.ManyToManyField(blank=True, to='main.category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='icons/default_icons/image_missing.jpg', upload_to='icons')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(default='icons/default_icons/image_missing.jpg', upload_to='icons/profile')),
                ('user_anime_favorites', models.ManyToManyField(blank=True, to='main.anime')),
                ('user_manga_favorites', models.ManyToManyField(blank=True, to='main.manga')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('anime', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.anime')),
                ('manga', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.manga')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile')),
            ],
            options={
                'verbose_name': 'Рецензия',
                'verbose_name_plural': 'Рецензии',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.anime')),
                ('manga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.manga')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author'),
        ),
        migrations.AddField(
            model_name='anime',
            name='categories',
            field=models.ManyToManyField(blank=True, to='main.category'),
        ),
        migrations.AddField(
            model_name='anime',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company'),
        ),
        migrations.AddField(
            model_name='anime',
            name='original',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.manga'),
        ),
        migrations.AddConstraint(
            model_name='comment',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('anime__isnull', True), ('manga__isnull', False)), models.Q(('anime__isnull', False), ('manga__isnull', True)), _connector='OR'), name='One content required for single comment'),
        ),
    ]
