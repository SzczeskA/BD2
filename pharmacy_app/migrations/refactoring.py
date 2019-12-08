from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Klient_Apteka', 'KlientApteka'),
        migrations.RenameModel('Sub_czynna', 'SubstancjaCzynna'),
        migrations.DeleteModel('Sub_czynna_Lek'),
        migrations.DeleteModel('Pracownik_Apteka')
    ]
