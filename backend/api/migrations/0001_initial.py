# Generated by Django 2.2 on 2019-04-01 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('url', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=1024, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True)),
                ('accuracy', models.DecimalField(blank=True, decimal_places=31, default=None, max_digits=32, null=True)),
                ('data_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DataType')),
            ],
        ),
        migrations.CreateModel(
            name='CredentialObjectStorage',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Project')),
                ('api_key', models.CharField(max_length=100)),
                ('instance_id', models.CharField(max_length=100)),
                ('bucket_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Data')),
                ('is_using', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
            options={
                'unique_together': {('label', 'project')},
            },
        ),
        migrations.AddField(
            model_name='data',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
        migrations.CreateModel(
            name='CredentialWA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=44)),
                ('url', models.CharField(max_length=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='CredentialVR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=44)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='CredentialNLC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=44)),
                ('url', models.CharField(max_length=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Data')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_train', models.NullBooleanField(default=None)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Label')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectHasUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(0, 'labeller'), (1, 'admin'), (2, 'owner')], default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('project', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Classifier',
            fields=[
                ('ibm_classifier_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('log_date', models.CharField(blank=True, max_length=255)),
                ('is_accuracy', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
            ],
            options={
                'unique_together': {('is_accuracy', 'project')},
            },
        ),
        migrations.CreateModel(
            name='PredictProba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proba', models.DecimalField(decimal_places=31, max_digits=32)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Label')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pool')),
            ],
            options={
                'unique_together': {('label', 'pool')},
            },
        ),
    ]