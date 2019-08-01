# Generated by Django 2.1.5 on 2019-07-31 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=120)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('OrgLocation', models.CharField(max_length=120)),
                ('OrgSize', models.CharField(max_length=120)),
                ('OrgDomain', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category_name', models.CharField(default='default', max_length=120)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Wipro_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='questions_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=120)),
                ('question_name', models.CharField(max_length=120)),
                ('question_category_name', models.CharField(max_length=120)),
                ('assessment_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Wipro_app.Assessment')),
                ('question_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Wipro_app.Question')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='org_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Wipro_app.Organization'),
        ),
    ]
