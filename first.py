from recipe_scrapers import *
import json
import uuid


# def make_file_name(recipe) -> str:
#     prefix, _ = recipe["host"].split(".")
#     name = recipe["title"].replace(" ", "_").replace("(","").replace(")","").replace("'","").replace("&","")
#     return f"json/{prefix}_{name}.json"


def scrape_website(target_url):
    extracted = scrape_me(target_url)

    recipe = {
        "host": extracted.host(),
        "title": extracted.title(),
        "total_time": extracted.total_time(),
        "yields": extracted.yields(),
        "ingredients": extracted.ingredients(),
        "instructions": extracted.instructions(),
        "ratings": extracted.ratings(),
        "reviews": extracted.reviews(),
        "URL": target_url,
    }

    file_name = str(uuid.uuid4())
    with open(f"json/{file_name}.json", "w") as f:
        f.write(json.dumps(recipe, sort_keys=True, indent=4))
        f.write("\n")


def read_urls(url_file):
    with open("urls.trc", "w") as trc:
        with open(url_file, "r") as urls:
            for url in urls:
                trc.write(f"{url}\n")
                scrape_website(url)


if __name__ == "__main__":
    read_urls("urls.txt")
    print("terminado")
