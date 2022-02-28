from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'Zebra Pie': {
        'Сахар, стакан': 2,
        'Куриное яйцо, штук': 5,
        'Сливочное масло, г': 200,
        'Сметана, банка': 1,
        'Пшеничная мука, стакан': 2,
        'Какао-порошок, столовые ложки': 2,
        'Гашеная сода, чайная ложка': 1
    }
}


photo_link = {'omlet': 'https://legkovmeste.ru/wp-content/uploads/2018/08/omlet-kak-v-detskom-sadu.jpg'}


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
    }
    link = "recipe/"
    context = {
        'pages': pages,
        'link': link,
        'DATA': DATA,
    }
    return render(request, template_name, context)


def recipe(request, name_recipe):
    template_name = 'calculator/index.html'
    pages = {
        'Главная страница': reverse('home'),
    }
    context = {
        'pages': pages,
        'recipe': {
        }
    }
    servings = int(request.GET.get("servings", 1))
    all_ingredients = DATA[name_recipe]
    context['recipe'].setdefault('Наименование блюда', name_recipe)
    context['recipe'].setdefault('Колличество порций', servings)
    context['recipe'].setdefault('Ингредиенты', '')
    for ingredients in all_ingredients:
        context['recipe'].setdefault(ingredients, all_ingredients[ingredients] * servings)
    return render(request, template_name, context)
