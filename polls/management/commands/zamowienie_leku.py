@transaction.atomic
def wykonaj_zamowienie(zamowienie):
    klient = Klient.objects.get(pk=zamowienie.klient.pk)
    koszyki = Koszyk.objects.filter(klient=klient)
    for koszyk in koszyki:
        opakowania_apteki = OpakowaniaApteki.object.get(opakowanie=koszyk.opakowanie, apteka=koszyk.apteka)
        if opakowania_apteki.ilosc < koszyk.ilosc_opakowan:
            raise ZamowienieError('Brak produktu' + opakowania_apteki.opakowanie)
        opakowania_apteki.ilosc -= koszyk.ilosc_opakowan
        opakowania_apteki.save()

