world_population = 8005176000
growth_rate = 0.0085
increase = 0
world_population2 = 8005176000
double = world_population * world_population
quad = world_population * world_population * world_population * world_population

print(f'{'number':>4} \t {'world population':>20} \t {'increase':>20}')
print()

for number in range(1, 101):
 increase = world_population * growth_rate 
 world_population += increase
 print(f'{number:>4} \t {int(world_population):>20,} \t {int(increase):>20,}')
 if world_population2 == double:
  print(number)
 if world_population2 == quad:
  print(number)
 

 