principal = 1000
rate = 7/100

amount_after_10years = principal * (1 + rate)**10

amount_after_20years = principal * (1 + rate)**20

amount_after_30years = principal * (1 + rate)**30

after_10years = (round(amount_after_10years, 2))

after_20years = (round(amount_after_20years, 2))

after_30years = (round(amount_after_30years, 2))

print('$', after_10years)

print('$', after_20years)

print('$', after_30years)
