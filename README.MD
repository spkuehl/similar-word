# Similar-Words

similar-words is a Python library for dealing with determining if a list of words have contain similar or identical words.

Automate the rule enforcement process of the game "JUST ONE".

## Installation

Clone the repository.

Install requirements.

Run pytests.



## Usage

```python
import words

wc = words.WordComparison(prompt='condiment')

wc.user_submissions = {'joe': 'ketchup',
                       'zoe': 'sauce',
                       'ash': 'ketchup',
                       'jane': 'mustard',
                       'dani': 'Bottle',
                       'ali': 'bottles'}
wc.get_unique_words()
#['sauce','mustard'] is returned
```

## Contributing
Pull requests are always welcome. For major changes, please open an issue first to discuss what you would like to change.

Fork > Clone Fork > Branch Clone > Make Changes > Commit Branch > Pull Request

Encouraged to update unit tests with PRs.
