from django.shortcuts import render

def index(request):
    """Homepage view"""
    context = {
        'title': 'Home',
        'page_name': 'home'
    }
    return render(request, 'birthday_site/home.html', context)

def best_bf(request):
    """Best boyfriend page view"""
    context = {
        'title': 'The Best BF???',
        'page_name': 'best_bf'
    }
    return render(request, 'birthday_site/best_bf.html', context)

def personality(request):
    """Personality traits view"""
    context = {
        'title': 'Personality',
        'page_name': 'personality'
    }
    return render(request, 'birthday_site/personality.html', context)

def physical_traits(request):
    """Physical traits view"""
    context = {
        'title': 'Physical Traits',
        'page_name': 'physical_traits'
    }
    return render(request, 'birthday_site/physical_traits.html', context)

def hobbies(request):
    """Hobbies view"""
    context = {
        'title': 'Hobbies',
        'page_name': 'hobbies'
    }
    return render(request, 'birthday_site/hobbies.html', context)

def birthday_card(request):
    """Birthday card view"""
    context = {
        'title': 'Birthday Card',
        'page_name': 'birthday_card'
    }
    return render(request, 'birthday_site/birthday_card.html', context)