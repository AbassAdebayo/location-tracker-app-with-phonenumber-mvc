import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
import logging
from django.conf import settings


logger = logging.getLogger(__name__)

class LocationTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'location_tracker'
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
            
        )
        
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
           self.group_name,
           self.channel_name
            
        )
        
    async def receive(self, text_data):
        logger.debug('Received WebSocket message: %s', text_data)
        
        data = json.loads(text_data)
        phone_number = data['phone_number']
        
        
        location_details = await self.get_location_details(phone_number)
        
        await self.send(text_data=json.dumps({
            
            'location': location_details
        }))
        
    async def track_location(self, event):
        logger.debug('Handling track_location event: %s', event)
        
        phone_number = event['phone_number']
        
        location_details = await self.get_location_details(phone_number)
        
        await self.send(text_data=json.dumps({
            
            'location': location_details
        }))
        
    async def get_location_details(self, phone_number):
        logger.debug('Fetching location details for: %s', phone_number)
        
        ipinfo_url = f'https://ipinfo.io/{phone_number}?token={settings.IPINFO_API_TOKEN}'
        ipinfo_response = requests.get(ipinfo_url)

        if ipinfo_response.status_code == 200:
            data = ipinfo_response.json()
            
            location = data.get('loc')
            if location:
                lat, lng = location.split(',')
                return {
                    'latitude': lat,
                    'longitude': lng,
                    'detailed_location': f"{data.get('city', 'Unknown')}, {data.get('region', 'Unknown')}, {data.get('country', 'Unknown')}",
                    'carrier': data.get('carrier', 'Unknown'),
                    'type': data.get('type', 'Unknown')
                }
            else:
                return "Error: No location data found in IPinfo response."
        else:
            return f"Error: Unable to retrieve IPinfo data. Status code: {ipinfo_response.status_code}"
                    