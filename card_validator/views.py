from django.shortcuts import render


# Create your views here.

from django.shortcuts import render
from .utils import verify_card_number

def validate_card(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card_translation = str.maketrans({'-': '', ' ': ''})
        translated_card_number = card_number.translate(card_translation)

        is_valid = verify_card_number(translated_card_number)
        return render(request, 'index.html', {'is_valid': is_valid})

    return render(request, 'index.html', {'is_valid': None})

