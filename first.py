from recipe_scrapers import *
import json

def make_file_name(recipe) -> str:
    prefix, _ = recipe['host'].split('.')
    name = recipe['title'].replace(' ','_')
    return f'{prefix}_{name}.json'

target_url = 'https://www.allrecipes.com/recipe/25317/carrot-chile-and-cilantro-soup/'
target_url = 'https://www.allrecipes.com/recipe/212722/murgh-makhani-indian-butter-chicken/'
target_url = 'https://www.allrecipes.com/recipe/238522/moroccan-lentil-soup-with-veggies/?internalSource=rr_feed_recipe_sb&referringId=238523%20referringContentType%3Drecipe'

extracted = scrape_me(target_url)

recipe = { 'host': extracted.host(),
            'title': extracted.title(),
            'total_time': extracted.total_time(),
            'yields': extracted.yields(),
            'ingredients': extracted.ingredients(),
            'instructions': extracted.instructions(),
            'ratings': extracted.ratings(),
            'reviews': extracted.reviews(),
            'URL': target_url,
}


with open(make_file_name(recipe), 'w') as f:
    f.write(json.dumps(recipe, sort_keys=True, indent=4))