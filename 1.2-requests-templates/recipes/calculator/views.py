from django.shortcuts import render

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
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)

    if not recipe:
        return render(request, 'calculator/index.html', {
            'error': f'Рецепт "{dish}" не найден'
        })

    servings_str = request.GET.get('servings')
    servings = 1

    if servings_str:
        try:
            servings = int(servings_str)
            if servings <= 0:
                servings = 1
        except ValueError:
            servings = 1

    if servings > 1:
        recipe = {name: round(amount * servings, 2) for name, amount in recipe.items()}

    context = {
        'recipe': recipe,
        'dish': dish,
        'servings': servings,
    }

    return render(request, 'calculator/index.html', context)