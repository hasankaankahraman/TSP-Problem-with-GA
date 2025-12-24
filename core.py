import random
from models import City 

def calculate_total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += from_city.distance(to_city)
    total += route[-1].distance(route[0])
    return total

def calculate_fitness(route):
    dist = calculate_total_distance(route)
    if dist == 0: return float('inf') 
    return 1 / dist


def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route

def initial_population(pop_size, city_list):
    population = []
    for i in range(pop_size):
        population.append(create_route(city_list))
    return population

# SEÇİM Rastgele birey seçer ve en iyisini döndürür
def selection(population, k=3):
    selection_pool = random.sample(population, k)
    # Fitness değerine göre sırala ve en iyisini al
    best_individual = max(selection_pool, key=calculate_fitness)
    return best_individual

# Standart crossover TSPde çalışmaz şehir tekrarı olur Order crossover kullanırız
def crossover(parent1, parent2):
    size = len(parent1)
    
    # 1. Babadan rastgele bir parça seç
    start, end = sorted(random.sample(range(size), 2))
    
    # Çocuğu boş (-1) olarak başlat
    child = [-1] * size
    
    # Babanın parçasını çocuğa aynen kopyala (Aynı konuma)
    child[start:end] = parent1[start:end]
    
    # 2. Anne'den kalanları sırayla doldur
    # Anne'nin genlerini sırayla gez
    current_pos = end # Doldurmaya babanın parçasının bittiği yerden başla
    
    for i in range(size):
        # Anne'nin i. şehri (sırayla bakıyoruz)
        city = parent2[(end + i) % size] 
        
        # Eğer bu şehir babadan aldığımız parçada YOKSA, ekle
        if city not in child[start:end]:
            if current_pos >= size: # Liste sonuna geldik mi?
                current_pos = 0     # Başa dön (Döngüsel yapı)
            
            child[current_pos] = city
            current_pos += 1
            
    return child
# MUTASYON
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(route))
            
            city1 = route[i]
            city2 = route[swap_with]
            
            route[i] = city2
            route[swap_with] = city1
    return route

# EVRİM FONKSİYONU

def next_generation(current_gen, elite_size, mutation_rate):
    new_population = []
    
    # Elitizm En iyi bireyleri koru
    ranked_pop = sorted(current_gen, key=calculate_fitness, reverse=True)
    
    for i in range(elite_size):
        new_population.append(ranked_pop[i])
        
    # 2. Geriye kalan nüfus için Crossover boşlukları doldur
    for i in range(len(current_gen) - elite_size):
        parent1 = selection(current_gen)
        parent2 = selection(current_gen)
        
        child = crossover(parent1, parent2)
        
        child = mutate(child, mutation_rate)
        
        new_population.append(child)
        
    return new_population