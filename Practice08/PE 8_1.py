bruin = ['Boxtel','Best','Beukenlaan',"Helmond 't Houd", 'Helmond', 'Helmond Brouwhuis', 'Deurne']
groen = ['Boxtel','Best','Beukenlaan','Geldrop','Heeze','Weert']
bruintotaal = set(bruin)
groentotaal = set(groen)

print('Deze stations zitten in beide trajecten {}'.format(bruintotaal.intersection(groentotaal)))
print('Deze stations komen wel voor in bruin en niet in groen',bruintotaal.difference(groentotaal))
print('Alle stations zijn',set(groen+bruin))
