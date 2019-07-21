from recipe_scrapers import *
import json

extracted = scrape_me('https://www.allrecipes.com/recipe/25317/carrot-chile-and-cilantro-soup/')

recipe = { 'host': extracted.host(),
            'title': extracted.title(),
            'total_time': extracted.total_time(),
            'yields': extracted.yields(),
            'ingredients': extracted.ingredients(),
            'instructions': extracted.instructions(),
            'ratings': extracted.ratings(),
            'reviews': extracted.reviews(),
}

print('foo')
print( json.dumps(recipe, sort_keys=True, indent=4))