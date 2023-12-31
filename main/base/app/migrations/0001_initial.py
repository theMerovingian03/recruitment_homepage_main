# Generated by Django 4.2.3 on 2023-08-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="name", max_length=100)),
                ("firstName", models.CharField(default="", max_length=100)),
                ("lastName", models.CharField(default="", max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("option1", "Male"),
                            ("option2", "Female"),
                            ("option3", "Prefer not to say"),
                        ],
                        default="option1",
                        max_length=20,
                    ),
                ),
                ("email", models.EmailField(default="", max_length=254)),
                ("phoneNumber", models.CharField(default="", max_length=20)),
                ("address", models.TextField(default="")),
                ("position", models.CharField(default="", max_length=100)),
                (
                    "dropdown1",
                    models.CharField(
                        choices=[
                            ("ai", "Artificial Intelligence"),
                            ("web-dev", "Web Development"),
                            ("blockchain", "Blockchain"),
                        ],
                        default="ai",
                        max_length=50,
                    ),
                ),
                (
                    "dropdown2",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("beginner", "0-5 yrs"),
                            ("intermediate", "5-10 yrs"),
                            ("advanced", "10-20 yrs"),
                            ("master", "20+ yrs"),
                        ],
                        default="beginner",
                        max_length=50,
                    ),
                ),
                (
                    "dropdown3",
                    models.CharField(
                        choices=[
                            ("option1", "Offline"),
                            ("option2", "Online"),
                            ("option3", "Hybrid"),
                        ],
                        default="option1",
                        max_length=50,
                    ),
                ),
                ("fileUpload", models.FileField(upload_to="resumes/")),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
