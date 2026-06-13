import requests

def test_metrics_works():
    # Делаем 3 запроса к /time
    for i in range(3):
        r = requests.get('http://localhost:5000/time')
        assert r.status_code == 200
    
    # Проверяем /metrics
    r = requests.get('http://localhost:5000/metrics')
    data = r.json()
    
    assert 'count' in data, "No 'count' field in response"
    assert data['count'] == 3, f"Expected 3, got {data['count']}"
    print(f"Metrics test PASSED: count = {data['count']}")

if __name__ == '__main__':
    test_metrics_works()
