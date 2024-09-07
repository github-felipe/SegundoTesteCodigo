Estados = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total = 0

for estado in Estados:
    total = total + Estados[estado]
for estado in Estados:
    representa = (Estados[estado] / total) * 100
    print(f'O estado "{estado}" representa um total de {representa}% no faturamento.')
