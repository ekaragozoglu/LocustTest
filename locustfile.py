from locust import HttpUser, task, between, events
import json
from datetime import datetime
import random

class SearchBehavior(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.n11.com"  # Temel URL burada belirtilir

    @task(1)
    def search_products(self):
        search_term = random.choice(["laptop", "phone", "tablet", "headphones", "watch"])
        response = self.client.get(f"/arama?q={search_term}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Arama isteği yapıldı: '{search_term}'. Response kodu: {response.status_code}. İşlem saati: {timestamp}"
        print(log_message)

        if response.status_code == 200:
            print(f"Arama sonuçları başarıyla alındı. Status kodu: {response.status_code}")
            self.list_search_results(response.json())
        else:
            print(f"Arama başarısız oldu. Status kodu: {response.status_code}")

    def list_search_results(self, response_json):
        results = response_json.get('results', [])
        if results:
            print(f"Arama sonuçları: {len(results)} ürün bulundu.")
            for result in results:
                print(f"Ürün: {result.get('name')}, Fiyat: {result.get('price')}")
        else:
            print("Arama sonuçları boş.")

    def on_start(self):
        print("Arama testi başlıyor.")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Test tamamlandı.")
