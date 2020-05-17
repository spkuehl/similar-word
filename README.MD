# Similar-Words

similar-words is a Python library for dealing with determining if a list of words have contain similar or identical words.

## Installation

Clone the repository.

Install requirements.

Run pytests.



## Usage

```python
import words

wc = words.WordComparison(starting_word='condiment')

wc.user_submissions = {'joe': 'ketchup',
                       'zoe': 'sauce',
                       'ash': 'ketchup',
                       'jane': 'mustard',
                       'dani': 'Bottle',
                       'ali': 'bottles'}
wc.get_unique_words()
#['mustard','sauce'] is returned
```

## Contributing
Pull requests are always welcome. For major changes, please open an issue first to discuss what you would like to change.

Fork > Clone > Make Changes > Commit > Pull Request

Encouraged to update tests as appropriate.

