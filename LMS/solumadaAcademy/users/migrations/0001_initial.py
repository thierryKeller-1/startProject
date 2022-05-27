# Generated by Django 4.0.4 on 2022-05-25 18:42

from django.db import migrations, models
import users.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolumadaUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='user email')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('m_code', models.CharField(max_length=50, verbose_name='M Code')),
                ('num_user', models.CharField(max_length=50, verbose_name='Num Agent')),
                ('type_user', models.CharField(choices=[('admin', 'admin'), ('teacher', 'teacher'), ('participant', 'participant')], default='participant', max_length=50, verbose_name='type user')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'SolumadaUsers',
                'ordering': ['-date_joined'],
                'permissions': [('have_no_user_permissions', 'Have No Permissions on User'), ('all_user_permissions', 'Can Do everything to User')],
            },
            managers=[
                ('objects', users.manager.AccountManager()),
            ],
        ),
    ]