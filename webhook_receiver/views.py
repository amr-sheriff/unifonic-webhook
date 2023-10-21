from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Notification
import json


@csrf_exempt
@require_POST
def notification(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            json_data = json.loads(request.body)

            # Save the notification payload to the database
            Notification.objects.create(payload=json.dumps(json_data))

            # Extract the 'digits' field from the JSON data
            digits = json_data.get('digits')

            # Prepare the custom response based on the 'digits' value
            if digits in ["1", "2", "3"]:
                response_data = {
                    "say": "thank you",
                    "language": "english",
                    "voice": "female"
                }
            else:
                response_data = {
                    "say": "Incorrect response, our customer service team will connect with you shortly.",
                    "language": "english",
                    "voice": "female"
                }

            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError:
            # In case of invalid JSON
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError:
            # In case of missing key
            return JsonResponse({'error': 'Bad Request: Missing key'}, status=400)
        except Exception as e:
            # In case of any other issues
            return JsonResponse({'error': 'An error occurred: {}'.format(str(e))}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are accepted'}, status=405)
