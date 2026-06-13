import requests

def test_metrics_integration():
    # Делаем 3 запроса к /time
    for i in range(3):
        resp = requests.get('http://localhost:5000/time')
        assert resp.status_code == 200
    
    # Проверяем /metrics
    resp = requests.get('http://localhost:5000/metrics')
    data = resp.json()
    
    # Проверяем, что поле count существует и оно не меньше 3
    assert 'count' in data, "Response must have 'count' field"
    assert data['count'] >= 3, f"Count should be at least 3, got {data['count']}"
    
    print(f"Test PASSED! Count = {data['count']}")

if __name__ == '__main__':
    test_metrics_integration()
