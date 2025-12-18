import random
from models import City 

def calculate_total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += from_city.distance(to_city)
    
    # Başlangıca dönüş
    total += route[-1].distance(route[0])
    return total

def calculate_fitness(route):
    dist = calculate_total_distance(route)
    if dist == 0: return float('inf') 
    return 1 / dist

def create_route(city_list):
# Permütasyon Kodlama (Tamsayı)
    route = random.sample(city_list, len(city_list))
    return route

def initial_population(pop_size, city_list):
    population = []
    for i in range(pop_size):
        population.append(create_route(city_list))
    return population