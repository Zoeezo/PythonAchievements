appelbomen = 333
schaduwBomen = (appelbomen / 3) * 2
zonBomen = appelbomen - schaduwBomen

print('Totale bomen: ' + str(appelbomen))
print('Schaduw bomen: ' + str(schaduwBomen))
print('Zon bomen: ' + str(zonBomen) + '\n')

zonAppels = 146
schaduwAppels = zonAppels * 0.8

print('Schaduw appels: ' + str(schaduwAppels))
print('Zon appels: ' + str(zonAppels) + '\n')

totaleAppels = (zonBomen * zonAppels) + (schaduwBomen * schaduwAppels)
persoonlijkeAppels = totaleAppels % 4


print('Totale appels: ' + str(totaleAppels))
print('Persoonlijke appels: ' + str(persoonlijkeAppels) + '\n')

print('Je mag ' + str(persoonlijkeAppels) + ' appels verkopen.')
