# CallWaiting.ai TTS API - Test Suite

import requests
import json
import time

def test_health_endpoint():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_tts_endpoint():
    """Test the TTS endpoint"""
    print("🔍 Testing TTS endpoint...")
    try:
        data = {
            "text": "Hello from CallWaiting.ai TTS API",
            "speaker": "male"
        }
        response = requests.post(
            "http://localhost:8000/tts",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            print("✅ TTS endpoint passed")
            print(f"   Response length: {len(response.text)} characters")
            return True
        else:
            print(f"❌ TTS endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ TTS endpoint error: {e}")
        return False

def test_performance():
    """Test API performance"""
    print("🔍 Testing API performance...")
    start_time = time.time()
    
    # Make 10 requests
    for i in range(10):
        response = requests.get("http://localhost:8000/health")
        if response.status_code != 200:
            print(f"❌ Performance test failed at request {i+1}")
            return False
    
    end_time = time.time()
    duration = end_time - start_time
    avg_time = duration / 10
    
    print(f"✅ Performance test passed")
    print(f"   10 requests in {duration:.2f}s")
    print(f"   Average response time: {avg_time:.3f}s")
    
    return avg_time < 1.0  # Should be under 1 second

def main():
    """Run all tests"""
    print("🧪 CallWaiting.ai TTS API Test Suite")
    print("=" * 50)
    
    tests = [
        ("Health Endpoint", test_health_endpoint),
        ("TTS Endpoint", test_tts_endpoint),
        ("Performance", test_performance),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"❌ {test_name} failed")
        except Exception as e:
            print(f"❌ {test_name} error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is ready for production.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
