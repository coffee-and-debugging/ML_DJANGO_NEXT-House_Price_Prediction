from django.http import JsonResponse
from rest_framework.decorators import api_view
from .ml_model import predict_price

@api_view(['POST'])
def predict(request):
    data = request.data
    features = [
        data['area'],
        data['bedrooms'],
        data['bathrooms'],
        data['stories'],
        1 if data['mainroad'] == 'yes' else 0,
        1 if data['guestroom'] == 'yes' else 0,
        1 if data['furnishingstatus'] == 'furnished' else 0,
        1 if data['furnishingstatus'] == 'semi-furnished' else 0
    ]
    price = predict_price(features)
    return JsonResponse({'price': price})
