# pochtaru

`pochtaru` is a pochta.ru downloader service.

## Usage

Currently `pochtaru` implements a single entry point - `get_postcode`

Example:
```Python
import pochtaru

postcode = pochtaru.get_postcode('г. Москва, ул. Смольная, 14')

# postcode = '125493'
```
