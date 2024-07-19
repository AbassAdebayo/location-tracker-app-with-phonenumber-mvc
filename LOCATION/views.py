from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def track_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        if phone_number:
            # Use the Abstract API to validate the phone number
            abstract_url = f'https://phonevalidation.abstractapi.com/v1/?api_key={settings.ABSTRACT_API_KEY}&phone={phone_number}'
            response = requests.get(abstract_url)

            if response.status_code == 200:
                data = response.json()

                # Use IPinfo to get location data based on the IP address
                ipinfo_url = f'https://ipinfo.io/json?token={settings.IPINFO_API_TOKEN}'
                ipinfo_response = requests.get(ipinfo_url)

                if ipinfo_response.status_code == 200:
                    ipinfo_data = ipinfo_response.json()
                    location = ipinfo_data.get('loc')
                    if location:
                        lat, lng = location.split(',')

                        data['latitude'] = lat
                        data['longitude'] = lng
                        data['detailed_location'] = f"{ipinfo_data.get('city')}, {ipinfo_data.get('region')}, {ipinfo_data.get('country')}"

                        return render(request, 'LOCATION/track_result.html', {'data': data})
                    else:
                        error_message = "Error: No location data found in IPinfo response."
                        return render(request, 'LOCATION/track.html', {'error': error_message})
                else:
                    error_message = f"Error: Unable to retrieve IPinfo data. Status code: {ipinfo_response.status_code}"
                    return render(request, 'LOCATION/track.html', {'error': error_message})
            else:
                error_message = f"Error: Unable to retrieve data from Abstract API. Status code: {response.status_code}"
                return render(request, 'LOCATION/track.html', {'error': error_message})
        else:
            return render(request, 'LOCATION/track.html', {'error': 'Please provide a phone number.'})
    return render(request, 'LOCATION/track.html')
