dia, mês, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
         'agosto','setembro','outubro','novembro','dezembro']
print('Voce nascem em: %s de %s de %s' %(dia, meses[int(mês)-1], ano))
