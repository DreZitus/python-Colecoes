#Operações com Sets no Python
bandas_rock_alternativo = {"Red Hot Chili Peppers", "Muse", "The Killers"}
bandas_indie_rock = {"The Killers", "Muse", "The Strokes"}

# União
print("União - Todas as bandas (Únicas) ")
print(bandas_rock_alternativo | bandas_indie_rock) #{'The Killers', 'Red Hot Chili Peppers', 'The Strokes', 'Muse'}
print("==========================================================")

# Interseção
print("Interseção - Bandas em comum no rock alternativo e indie rock")
print(bandas_rock_alternativo & bandas_indie_rock) #{'The Killers', 'Muse'}
print("==========================================================")

# Diferença
print("Diferença - Banda que está no rock alternativo mas não está no indie rock")
print(bandas_rock_alternativo - bandas_indie_rock) #{'Red Hot Chili Peppers'}
print("==========================================================")

# Diferença Simétrica
print("Diferença Simétrica - Bandas que estão apenas em rock alternativo ou apenas em indie rock")
print(bandas_rock_alternativo ^ bandas_indie_rock) #{'The Strokes', 'Red Hot Chili Peppers'}
print("==========================================================")