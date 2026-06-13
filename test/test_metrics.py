import requests

def test_metrics_count():
    # Делаем 5 запросов к /time
    for i in range(5):
        response = requests.get('http://localhost:5000/time')
        assert response.status_code == 200
    
    # Проверяем /metrics
    response = requests.get('http://localhost:5000/metrics')
    data = response.json()
    
    # Счетчик должен быть 5
    assert data['count'] == 5, f"ERROR: expected 5, got {data['count']}"
    print(f"OK: count = {data['count']}")

if __name__ == '__main__':
    test_metrics_count()
