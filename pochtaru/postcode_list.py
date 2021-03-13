"""
pochtaru
========

postcode_list
-------------
postcode_list is a module that provides tools to download a list of postcodes.
"""

import pandas as pd

import pochtaru


def open_address_list(address_list_filename: str,
                      address_column_name: str) -> pd.Series:
    """Read address list from a CSV file and return them as a Series."""
    addr_df = pd.read_csv(address_list_filename, sep=';', dtype=str)
    addr_s = addr_df[address_column_name]
    print(f'Loaded {len(addr_s)} addresses for querying.')
    return addr_s


def open_cache(cache_filename: str) -> pd.DataFrame:
    """Read cache DataFrame from file or create a new one if it doesn't
    exist.
    """
    try:
        cache = pd.read_csv(cache_filename, sep=';', dtype=str)
    except FileNotFoundError:
        cache = pd.DataFrame(columns=['address', 'postcode'])
    print(f'{len(cache)} addresses in cache.')
    return cache


def get_a_record(address: str, cache: pd.DataFrame) -> pd.DataFrame:
    """Query a single address and save it to cache.

    Return a new (updated) cache DataFrame.
    """
    print(f'Querying {address:<50}…', end='', flush=True)
    postcode = pochtaru.get_postcode(address)
    cache_row = {'address': address, 'postcode': postcode}
    cache_upd = cache.append(cache_row, ignore_index=True)
    print(postcode)
    return cache_upd


def save_cache(cache_df: pd.DataFrame, cache_filename: str) -> None:
    """Save cache DataFrame to a CSV file."""
    cache_df.to_csv(cache_filename, sep=';', index=False)
    print(f'Cache saved to {cache_filename}.')


def download_postcode_list(address_list_filename: str,
                           address_column_name: str,
                           cache_filename: str,
                           limit: int) -> None:
    """Download postcodes for a list of addresses.

    Given the unreliable nature of scraping, the intermediate results will be
    stored in a cache file that will persist even if the script terminates.
    """
    addr = open_address_list(address_list_filename, address_column_name)
    cache = open_cache(cache_filename)
    for idx, address in enumerate(addr, 1):
        try:
            cache = get_a_record(address, cache)
        except KeyboardInterrupt:
            print('Interrupted by user... Quitting')
            break
        if idx >= limit:
            break
    save_cache(cache, cache_filename)
