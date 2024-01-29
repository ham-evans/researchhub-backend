# Generated by Django 4.1 on 2024-01-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("researchhub_document", "0056_alter_unifieddocumentconcepts_concept"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchhubpost",
            name="document_type",
            field=models.CharField(
                choices=[
                    ("DISCUSSION", "DISCUSSION"),
                    ("ELN", "ELN"),
                    ("HYPOTHESIS", "HYPOTHESIS"),
                    ("NOTE", "NOTE"),
                    ("PAPER", "PAPER"),
                    ("QUESTION", "QUESTION"),
                    ("PREREGISTRATION", "PREREGISTRATION"),
                ],
                default="DISCUSSION",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="researchhubunifieddocument",
            name="document_type",
            field=models.CharField(
                choices=[
                    ("DISCUSSION", "DISCUSSION"),
                    ("ELN", "ELN"),
                    ("HYPOTHESIS", "HYPOTHESIS"),
                    ("NOTE", "NOTE"),
                    ("PAPER", "PAPER"),
                    ("QUESTION", "QUESTION"),
                    ("PREREGISTRATION", "PREREGISTRATION"),
                ],
                default="PAPER",
                help_text="Papers are imported from external src. Posts are in-house",
                max_length=32,
            ),
        ),
    ]
