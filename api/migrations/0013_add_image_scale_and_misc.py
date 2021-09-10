# Generated by Django 3.1.8 on 2021-09-09 16:06

import django.db.models.deletion
from django.db import migrations, models

import api.models.long_running_job


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_add_favorite_min_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image_scale",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="albumdate",
            name="location",
            field=models.JSONField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="face",
            name="image",
            field=models.ImageField(null=True, upload_to="faces"),
        ),
        migrations.AlterField(
            model_name="face",
            name="photo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="faces",
                to="api.photo",
            ),
        ),
        migrations.AlterField(
            model_name="longrunningjob",
            name="job_type",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Scan Photos"),
                    (2, "Generate Event Albums"),
                    (3, "Regenerate Event Titles"),
                    (4, "Train Faces"),
                    (5, "Delete Missing Photos"),
                    (7, "Scan Faces"),
                    (6, "Calculate Clip Embeddings"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="longrunningjob",
            name="result",
            field=models.JSONField(
                default=api.models.long_running_job.get_default_longrunningjob_result
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="captions_json",
            field=models.JSONField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="exif_json",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="geolocation_json",
            field=models.JSONField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="image_paths",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
