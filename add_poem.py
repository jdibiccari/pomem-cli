from slugify import slugify
from multiline_input import multiline_input
import yaml

def add_new():
    # Gather poem meta data
    prompts = [
        "author",
        "title"
    ]
    poem_data = {}
    body = ""
    for prompt in prompts:
        response = raw_input(prompt + ': ')
        poem_data[prompt] = response

    # Gather poem body
    stopword = "@@"
    print "Copy and paste the body of the poem. Type '{}' and enter when you are finished.".format(stopword)
    body = multiline_input(stopword)
    poem_data['body'] = body
    slug = slugify(poem_data['title'])
    with open('data/' + slug + '.yml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(poem_data, allow_unicode=True, default_flow_style=False))