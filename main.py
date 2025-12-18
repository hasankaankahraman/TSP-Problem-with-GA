# main.py
import matplotlib.pyplot as plt
from data import berlin52_coords
from models import City
import core

def main():
    print("Gezgin Satıcı Problemi:")
    
    # Veri Setini Yükle ve Nesneye Çevir
    city_list = []
    for i, coord in enumerate(berlin52_coords):
        city_list.append(City(x=coord[0], y=coord[1], id=i))
    
    print(f"Veri Seti: Berlin52 ({len(city_list)}")

    # Popülasyon Oluştur
    pop_size = 5
    print(f"Başlangıç Popülasyonu Oluşturuluyor (Boyut: {pop_size})...")
    
    population = core.initial_population(pop_size, city_list)

    # Sonuçları Analiz Et
    print("\n--- İlk Rastgele Çözümlerin Analizi ---")
    for i, route in enumerate(population):
        dist = core.calculate_total_distance(route)
        fitness = core.calculate_fitness(route)
        print(f"Aday {i+1} Mesafe: {dist:.2f} | Fitness: {fitness:.6f}")

    # Görselleştirme (İlk rotayı çiz)
    visualize_route(population[0], city_list)

def visualize_route(route, all_cities):
    x_coords = [c.x for c in route]
    y_coords = [c.y for c in route]
    # Başlangıca dön
    x_coords.append(route[0].x)
    y_coords.append(route[0].y)

    plt.figure(figsize=(10, 8))
    
    # Önce tüm şehirleri nokta olarak koy
    all_x = [c.x for c in all_cities]
    all_y = [c.y for c in all_cities]
    plt.plot(all_x, all_y, 'ro', markersize=6, label='Şehirler')

    # Rotayı çizgi olarak çiz
    plt.plot(x_coords, y_coords, 'b-', linewidth=1, alpha=0.7, label='Aday Rota')
    
    plt.title("Berlin52")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()