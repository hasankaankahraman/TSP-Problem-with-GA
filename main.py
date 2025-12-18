import matplotlib.pyplot as plt
from data import berlin52_coords, kroA100_coords
from models import City
import core 

def main():
    pop_size = 100
    elite_size = 20
    mutation_rate = 0.01
    generations = 1000 
        
    # Veri Seti Secimi
    dataset_name = "berlin52" 

    if dataset_name == "berlin52":
        coords = berlin52_coords
    else:
        coords = kroA100_coords

    city_list = []
    for i, coord in enumerate(coords):
        city_list.append(City(x=coord[0], y=coord[1], id=i))
    
    print(f"Calisilan Veri Seti: {dataset_name} ({len(city_list)} sehir)")

    population = core.initial_population(pop_size, city_list)
    print(f"Baslangic Mesafesi: {core.calculate_total_distance(population[0]):.2f}")

    print("Evrim basladi...")
    
    progress = []
    
    for i in range(0, generations):
        population = core.next_generation(population, elite_size, mutation_rate)
        
        best_route = population[0]
        dist = core.calculate_total_distance(best_route)
        progress.append(dist)
        
        if i % 50 == 0:
            print(f"Nesil {i}: Mesafe = {dist:.2f}")

    best_route = population[0]
    final_dist = core.calculate_total_distance(best_route)
    print(f"--- Bitti ---\nFinal Mesafe: {final_dist:.2f}")

    # Gorsellestirme
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    x_coords = [c.x for c in best_route]
    y_coords = [c.y for c in best_route]
    x_coords.append(best_route[0].x)
    y_coords.append(best_route[0].y)

    all_x = [c.x for c in city_list]
    all_y = [c.y for c in city_list]

    ax1.plot(all_x, all_y, 'ro', markersize=4)
    ax1.plot(x_coords, y_coords, 'b-', linewidth=1)
    ax1.set_title(f"En Iyi Rota ({dataset_name}) - Mesafe: {final_dist:.0f}")

    ax2.plot(progress)
    ax2.set_ylabel('Mesafe')
    ax2.set_xlabel('Nesil')
    ax2.set_title('Ilerleme')

    plt.show()

if __name__ == "__main__":
    main()