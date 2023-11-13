# Generated by Django 4.2.3 on 2023-08-07 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_anime_created_alter_company_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('rate', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Рецензия к аниме',
                'verbose_name_plural': 'Рецензии к аниме',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MangaComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Комментарий к манге',
                'verbose_name_plural': 'Комментарии к манге',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MangaReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('rate', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Рецензия к манге',
                'verbose_name_plural': 'Рецензии к манге',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='review',
            name='anime',
        ),
        migrations.RemoveField(
            model_name='review',
            name='manga',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
        migrations.RemoveField(
            model_name='company',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='rating',
        ),
        migrations.AlterField(
            model_name='anime',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(default='images/default_images/image_missing.jpg', upload_to='images/content/anime'),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='image',
            field=models.ImageField(default='images/default_images/image_missing.jpg', upload_to='images/content/manga   '),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='images/default_icons/image_missing.jpg', upload_to='images/profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_anime_favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='anime_favorites', to='main.anime'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_manga_favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='manga_favorites', to='main.manga'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='mangareview',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manga'),
        ),
        migrations.AddField(
            model_name='mangareview',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile'),
        ),
        migrations.AddField(
            model_name='mangacomment',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manga'),
        ),
        migrations.AddField(
            model_name='mangacomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile'),
        ),
        migrations.AddField(
            model_name='animereview',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anime'),
        ),
        migrations.AddField(
            model_name='animereview',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile'),
        ),
        migrations.AddField(
            model_name='animecomment',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anime'),
        ),
        migrations.AddField(
            model_name='animecomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_anime_reviews',
            field=models.ManyToManyField(blank=True, null=True, related_name='anime_reviews', through='main.AnimeReview', to='main.anime'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_manga_reviews',
            field=models.ManyToManyField(blank=True, null=True, related_name='manga_reviews', through='main.MangaReview', to='main.manga'),
        ),
        migrations.AddConstraint(
            model_name='mangareview',
            constraint=models.CheckConstraint(check=models.Q(('rate__gte', 0), ('rate__lte', 10)), name='Оценка должна быть от 0 до 10'),
        ),
    ]
