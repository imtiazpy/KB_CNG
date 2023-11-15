from django.shortcuts import render


data = [
    {
      "id": 1,
      "title": "Solid Octane",
      "content": "Our services redefine the fueling experience. With 24/7 accessibility, cutting-edge technology, and a commitment to environmental responsibility, Khan Brothers CNG Station ensures your journey is not just fueled but elevated. From premium oils to real-time monitoring with current meters, we cater to your vehicle's every need. Choose us for a seamless blend of reliability, innovation, and eco-friendly efficiency that goes beyond ordinary fueling stations.",
      "img_path": "img/icon/1.png"
    },
    {
      "id": 2,
      "title": "Pure Diesel",
      "content": "Experience the purity of power with our premium diesel services. Khan Brothers CNG Station delivers quality fuel round the clock, ensuring optimal engine performance and reliability. Drive with confidence, powered by the excellence of Pure Diesel.",
      "img_path": "img/icon/5.png"
    },
    {
      "id": 3,
      "title": "Light Petrol",
      "content": "Ignite your journey with Light Petrol excellence at Khan Brothers CNG Station. Our top-grade fuel ensures a smooth and efficient ride, 24/7. Trust us to fuel your adventures with quality and reliability, every time you choose Light Petrol.",
      "img_path": "img/icon/4.png"
    },
    {
      "id": 4,
      "title": "CNG Gas",
      "content": "Embrace the future of eco-friendly fueling with CNG Gas at Khan Brothers CNG Station. With our state-of-the-art facilities, experience clean and efficient energy for your vehicle. Drive sustainably with our commitment to environmental stewardship.",
      "img_path": "img/icon/3.png"
    },
    {
      "id": 5,
      "title": "Car Cleaning",
      "content": "Beyond fueling, we pamper your ride with our professional Car Cleaning services. At Khan Brothers CNG Station, treat your vehicle to a thorough cleaning, leaving it refreshed and ready for the road. Choose us for a comprehensive fuel and care experience.",
      "img_path": "img/icon/2.png"
    },
    {
      "id": 6,
      "title": "Electric Charging",
      "content": "Power up your electric vehicle at Khan Brothers CNG Station. Our Electric Charging services provide a reliable and fast-charging experience, supporting the future of sustainable transportation. Choose us for convenient and eco-friendly charging solutions.",
      "img_path": "img/icon/6.png"
    }
  ]

def services_list_page(request):

  return render(request, 'services/services_list_page.html', {'service_items': data})




def service_detail_page(request, pk):
  service = next((item for item in data if item['id'] == pk), None)

  if not service:
    return render(request, '404.html')

  context = {
    'services': data,
    'service': service,
  }

  return render(request, 'services/service_detail.html', context)
