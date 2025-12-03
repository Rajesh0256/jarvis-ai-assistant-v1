"""
Internet Speed Test Module for Jarvis AI
Checks download speed and ping using simple HTTP requests
"""

import requests
import time
import threading


def CheckInternetSpeed():
    """
    Check internet speed (download speed and ping)
    Returns formatted string with results
    """
    try:
        print("Starting internet speed test...")
        
        # Test ping to Google DNS
        print("Testing ping...")
        ping_url = "https://www.google.com"
        ping_times = []
        
        for i in range(3):
            start = time.time()
            try:
                requests.get(ping_url, timeout=5)
                ping_time = (time.time() - start) * 1000  # Convert to ms
                ping_times.append(ping_time)
            except:
                pass
        
        avg_ping = round(sum(ping_times) / len(ping_times), 2) if ping_times else 0
        
        # Test download speed
        print("Testing download speed...")
        # Download a test file (approximately 5MB)
        test_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
        
        # Download multiple times to get better measurement
        total_downloaded = 0
        total_time = 0
        
        for i in range(3):
            start_time = time.time()
            response = requests.get(test_url, timeout=15)
            elapsed_time = time.time() - start_time
            
            total_downloaded += len(response.content)
            total_time += elapsed_time
        
        # Calculate average speed in Mbps
        speed_mbps = round((total_downloaded * 8) / (total_time * 1_000_000), 2)
        
        # Determine quality
        if speed_mbps > 50:
            quality = "excellent"
        elif speed_mbps > 20:
            quality = "good"
        elif speed_mbps > 5:
            quality = "moderate"
        else:
            quality = "slow"
        
        result_text = f"""Internet Speed Test Results:

Download Speed: {speed_mbps} Mbps
Ping: {avg_ping} ms

Your internet connection is {quality}."""
        
        print("Speed test completed!")
        return result_text
        
    except requests.exceptions.Timeout:
        return "The speed test took too long. Your connection might be slow."
    except requests.exceptions.ConnectionError:
        return "I couldn't connect to the test server. Please check your internet connection."
    except Exception as e:
        print(f"Error checking internet speed: {e}")
        return f"I couldn't check the internet speed. Please make sure you're connected to the internet."


def CheckInternetSpeedQuick():
    """
    Quick internet speed check (ping only)
    Faster but less comprehensive
    """
    try:
        print("Starting quick speed test...")
        
        # Test ping only for quick check
        ping_url = "https://www.google.com"
        ping_times = []
        
        for i in range(3):
            start = time.time()
            try:
                requests.get(ping_url, timeout=5)
                ping_time = (time.time() - start) * 1000
                ping_times.append(ping_time)
            except:
                pass
        
        avg_ping = round(sum(ping_times) / len(ping_times), 2) if ping_times else 0
        
        # Quick download test
        test_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
        
        start_time = time.time()
        response = requests.get(test_url, timeout=10)
        elapsed_time = time.time() - start_time
        
        total_size = len(response.content)
        speed_mbps = round((total_size * 8) / (elapsed_time * 1_000_000), 2)
        
        quality = "excellent" if speed_mbps > 50 else "good" if speed_mbps > 20 else "moderate" if speed_mbps > 5 else "slow"
        
        result_text = f"""Quick Speed Test:

Download Speed: {speed_mbps} Mbps
Ping: {avg_ping} ms

Your connection is {quality}."""
        
        return result_text
        
    except Exception as e:
        print(f"Error in quick speed test: {e}")
        return "I couldn't check the internet speed. Please check your connection."


def CheckInternetSpeedAsync(callback=None):
    """
    Run speed test in background thread
    callback: function to call with result when done
    """
    def run_test():
        result = CheckInternetSpeed()
        if callback:
            callback(result)
        return result
    
    thread = threading.Thread(target=run_test, daemon=True)
    thread.start()
    return thread


if __name__ == "__main__":
    print("Testing Internet Speed Module\n")
    print("=" * 70)
    
    # Test full speed check
    result = CheckInternetSpeed()
    print(result)
