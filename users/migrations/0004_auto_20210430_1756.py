# Generated by Django 3.1.6 on 2021-04-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210430_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(choices=[('AEROSPACE_ENGINEERING', 'Aerospace Engineering'), ('AFRICAN_AMERICAN_AND_AFRICAN_STUDIES', 'African American and African Studies'), ('AMERICAN_STUDIES', 'American Studies'), ('ANTHROPOLOGY', 'Anthropology'), ('ARCHAEOLOGY', 'Archaeology'), ('ARCHITECTURAL_HISTORY', 'Architectural History'), ('ARCHITECTURE', 'Architecture'), ('ASTRONOMY', 'Astronomy'), ('BACHELOR_OF_INTERDISCIPLINARY_STUDIES', 'Bachelor of Interdisciplinary Studies'), ('BACHELOR_OF_PROFESSIONAL_STUDIES_IN_HEALTH_SCIENCES_MANAGEMENT', 'Bachelor of Professional Studies in Health Sciences Management'), ('BIOLOGY', 'Biology'), ('BIOMEDICAL_ENGINEERING', 'Biomedical Engineering'), ('CHEMICAL_ENGINEERING', 'Chemical Engineering'), ('CHEMISTRY', 'Chemistry'), ('CIVIL_ENGINEERING', 'Civil Engineering'), ('CLASSICS', 'Classics'), ('COGNITIVE_SCIENCE', 'Cognitive Science'), ('COMMERCE', 'Commerce'), ('COMPARATIVE_LITERATURE', 'Comparative Literature'), ('COMPUTER_ENGINEERING', 'Computer Engineering'), ('COMPUTER_SCIENCE', 'Computer Science'), ('DANCE', 'Dance'), ('DRAMA', 'Drama'), ('EAST_ASIAN_LANGUAGES_LITERATURES_AND_CULTURE', 'East Asian Languages, Literatures and Culture'), ('ECONOMICS', 'Economics'), ('ELECTRICAL_ENGINEERING', 'Electrical Engineering'), ('ENGINEERING_SCIENCE', 'Engineering Science'), ('ENGLISH', 'English'), ('ENVIRONMENTAL_SCIENCES', 'Environmental Sciences'), ('ENVIRONMENTAL_THOUGHT_AND_PRACTICE', 'Environmental Thought and Practice'), ('FIVE_YEAR_TEACHER_EDUCATION_PROGRAM', 'Five-Year Teacher Education Program'), ('FRENCH', 'French'), ('GERMAN', 'German'), ('GERMAN_STUDIES', 'German Studies'), ('GLOBAL_STUDIES', 'Global Studies'), ('GLOBAL_SUSTAINABILITY_MINOR', 'Global Sustainability Minor'), ('HISTORIC_PRESERVATION_MINOR', 'Historic Preservation Minor'), ('HISTORY', 'History'), ('HISTORY_OF_ART', 'History of Art'), ('HUMAN_BIOLOGY', 'Human Biology'), ('INTERDISCIPLINARY_MAJOR_OF_GLOBAL_STUDIES', 'Interdisciplinary Major of Global Studies'), ('JEWISH_STUDIES', 'Jewish Studies'), ('KINESIOLOGY', 'Kinesiology'), ('LANDSCAPE_ARCHITECTURE_MINOR', 'Landscape Architecture Minor'), ('LATIN_AMERICAN_STUDIES', 'Latin American Studies'), ('LINGUISTICS', 'Linguistics'), ('MATERIALS_SCIENCE_AND_ENGINEERING', 'Materials Science and Engineering'), ('MATHEMATICS', 'Mathematics'), ('MECHANICAL_ENGINEERING', 'Mechanical Engineering'), ('MEDIA_STUDIES', 'Media Studies'), ('MEDIEVAL_STUDIES', 'Medieval Studies'), ('MIDDLE_EASTERN_AND_SOUTH_ASIAN_LANGUAGES_AND_CULTURES', 'Middle Eastern and South Asian Languages and Cultures'), ('MUSIC', 'Music'), ('NEUROSCIENCE', 'Neuroscience'), ('NURSING', 'Nursing'), ('PHILOSOPHY', 'Philosophy'), ('PHYSICS', 'Physics'), ('POLITICAL_AND_SOCIAL_THOUGHT', 'Political and Social Thought'), ('POLITICAL_PHILOSOPHY_POLICY_AND_LAW', 'Political Philosophy, Policy, and Law'), ('POLITICS', 'Politics'), ('PSYCHOLOGY', 'Psychology'), ('RELIGIOUS_STUDIES', 'Religious Studies'), ('SLAVIC_LANGUAGES_AND_LITERATURES', 'Slavic Languages and Literatures'), ('SOCIOLOGY', 'Sociology'), ('SPANISH', 'Spanish'), ('SPEECH_COMMUNICATION_DISORDERS', 'Speech Communication Disorders'), ('STATISTICS', 'Statistics'), ('STUDIO_ART', 'Studio Art'), ('SYSTEMS_ENGINEERING', 'Systems Engineering'), ('URBAN_AND_ENVIRONMENTAL_PLANNING', 'Urban and Environmental Planning'), ('WOMEN_GENDER_AND_SEXUALITY', 'Women, Gender & Sexuality'), ('YOUTH_AND_SOCIAL_INNOVATION', 'Youth & Social Innovation'), ('OTHER', 'Other'), ('UNKNOWN', 'Undecided/Unknown')], default='UNKNOWN', max_length=70),
        ),
    ]