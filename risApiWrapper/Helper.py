import requests
import re


def _request(url, parameters) -> list:
    """
    Requests a response from the provided api with the provided parameters. If
    the response has 100 entries, it continues to request additional "pages"
    as long as a response with less than 100 entries is returned. A list of
    all entries is returned.
    """
    response = requests.get(url, params=parameters).json()

    # Return nothing if no items are found
    if (
        int(response["OgdSearchResult"]["OgdDocumentResults"]["Hits"]["#text"])
        == 0
    ):
        return []
    """
    If only one item is found, "OgdDocumentReference" contains only one dict.
    If multiple items are found, "OgdDocumentReference" contains a list of
    dicts.
    """
    results = (
        [
            response["OgdSearchResult"]["OgdDocumentResults"][
                "OgdDocumentReference"
            ]
        ]
        if isinstance(
            response["OgdSearchResult"]["OgdDocumentResults"][
                "OgdDocumentReference"
            ],
            dict,
        )
        else response["OgdSearchResult"]["OgdDocumentResults"][
            "OgdDocumentReference"
        ]
    )

    # If 100 items are found, there may be additional items on the next "page".
    if (
        len(
            response["OgdSearchResult"]["OgdDocumentResults"][
                "OgdDocumentReference"
            ]
        )
        == 100
    ):
        parameters["Seitennummer"] += 1
        results.append(_request(parameters))

    return results


def _to_list(data) -> list:
    """
    Returns the input as a list if it is not a list already.
    """
    return [data] if isinstance(data, str) else data


def _sort_results(
    results: list, sort_key: str, sort_keys: list, ascending: bool
) -> list:
    """
    Sorts the provided results by a specified key.
    """
    _input_validation("sort_key", sort_key, sort_keys)

    if ascending:
        return sorted(results, key=lambda item: item[sort_key], reverse=True)
    else:
        return sorted(results, key=lambda item: item[sort_key], reverse=False)


def _input_validation(key: str, value: str, values: list) -> None:
    """
    Validates the provided inputs against a list of possible inputs and raises
    an exception if not matching.
    """
    if value not in values:
        raise ValueError(
            'Please provide a valid argument for "{0}". Accepted arguments for'
            ' "{0}" are "{1}" or "{2}".'.format(
                key, '", "'.join(values[0:-2]), values[-1]
            )
        )


def _date_input_validation(key: str, value: str) -> None:
    """
    Validates the provided date against the format requirements of the API if
    a date is provided.
    """
    if value and not re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise ValueError(
            f'The date "{value}" provided for "{key}" is not formatted'
            ' correctly. Please provide dates in the format "YYYY-MM-DD".'
        )
