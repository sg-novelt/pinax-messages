# Generated by Django 4.0.8 on 2023-01-18 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("people", "0001_initial"),
        ("pinax_messages", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ("sent_at",), "verbose_name": "message", "verbose_name_plural": "messages"},
        ),
        migrations.AlterModelOptions(
            name="thread",
            options={"verbose_name": "thread", "verbose_name_plural": "threads"},
        ),
        migrations.AlterModelOptions(
            name="userthread",
            options={"verbose_name": "user thread", "verbose_name_plural": "user threads"},
        ),
        migrations.AlterField(
            model_name="message",
            name="content",
            field=models.TextField(verbose_name="content"),
        ),
        migrations.AlterField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="sender",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="sent_at",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="sent at"),
        ),
        migrations.AlterField(
            model_name="message",
            name="thread",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="pinax_messages.thread",
                verbose_name="thread",
            ),
        ),
        migrations.AlterField(
            model_name="thread",
            name="subject",
            field=models.CharField(max_length=150, verbose_name="subject"),
        ),
        migrations.AlterField(
            model_name="thread",
            name="users",
            field=models.ManyToManyField(
                through="pinax_messages.UserThread", to=settings.AUTH_USER_MODEL, verbose_name="users"
            ),
        ),
        migrations.AlterField(
            model_name="userthread",
            name="deleted",
            field=models.BooleanField(default=False, verbose_name="deleted"),
        ),
        migrations.AlterField(
            model_name="userthread",
            name="thread",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pinax_messages.thread", verbose_name="thread"
            ),
        ),
        migrations.AlterField(
            model_name="userthread",
            name="unread",
            field=models.BooleanField(default=True, verbose_name="unread"),
        ),
        migrations.AlterField(
            model_name="userthread",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="user"
            ),
        ),
    ]
