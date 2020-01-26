# Generated by Django 2.2.7 on 2020-01-25 20:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice1', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice1_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('dice2', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice2_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('dice3', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice3_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('dice4', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice4_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('dice5', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice5_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('dice6', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice6_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('date_created', models.DateTimeField()),
                ('allowReroll', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField()),
                ('is_winner', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('I', 'In-Progress')], max_length=1)),
                ('num_players', models.IntegerField()),
                ('player_position', models.IntegerField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('error', '1'), ('command', '1'), ('game', '1')], max_length=1)),
                ('message_string', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
                ('last_read_date', models.DateTimeField(auto_now_add=True)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_purchased', models.CharField(max_length=30)),
                ('card_used', models.CharField(max_length=30)),
                ('location', models.CharField(choices=[('T', 'In-Tokyo'), ('O', 'Outside-Tokyo')], max_length=1)),
                ('victory_points', models.IntegerField()),
                ('energy_cube', models.IntegerField()),
                ('life_points', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('dice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Dice')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.User')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.User'),
        ),
        migrations.AddField(
            model_name='dice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.User'),
        ),
    ]
