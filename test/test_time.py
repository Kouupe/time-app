import requests
import json

def test_time_not_zero():
    response = requests.get('http://localhost:5000/time')
    data = response.json()
    
    # Проверяем, что время не 0
    assert data['time'] != 0, "ERROR: time is 0!"
    print(f"OK: time = {data['time']}")

if __name__ == '__main__':
    test_time_not_zero()
