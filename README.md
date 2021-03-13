# pochtaru

`pochtaru` is a pochta.ru downloader service.

## Usage

Currently `pochtaru` implements two entry points: 
- `get_postcode` - to download a single adress postcode
- `download_postcode_list` - to dowload postcodes for a list of addresses

## Examples:

### Single address

```Python
import pochtaru

postcode = pochtaru.get_postcode('г. Москва, ул. Смольная, 14')

# postcode = '125493'
```

### Address list

```Python
import pochtaru

ADDRESS_LIST_FN = '../output/_redundant_addresses.csv'
ADDRESS_COL_NAME = 'addr'
POSTCODES_CACHE = '../output/_postcodes_cache.csv'

pochtaru.download_postcode_list(
        address_list_filename=ADDRESS_LIST_FN,
        address_column_name=ADDRESS_COL_NAME,
        cache_filename=POSTCODES_CACHE,
        limit=10
    )
```

