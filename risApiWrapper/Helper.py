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
    if int(response["OgdSearchResult"]["OgdDocumentResults"]["Hits"]["#text"]) == 0:
        return []
    """
    If only one item is found, "OgdDocumentReference" contains only one dict.
    If multiple items are found, "OgdDocumentReference" contains a list of
    dicts.
    """
    results = (
        [response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]]
        if isinstance(
            response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"],
            dict,
        )
        else response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]
    )

    # If 100 items are found, there may be additional items on the next "page".
    if (
        len(response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"])
        == 100
    ):
        parameters["Seitennummer"] += 1
        results += _request(url, parameters)

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
    if value:
        if not any(sub_value in value for sub_value in values):
            raise ValueError(
                'Please provide a valid argument for "{0}". Accepted arguments for'
                ' "{0}" are "{1}" or "{2}".'.format(
                    key, '", "'.join(values[0:-1]), values[-1]
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


def _get_content_urls(raw_case: dict) -> list:
    """
    Extracts all content urls from the raw case data and returns them as a list.
    """
    content_urls = []
    try:
        if isinstance(raw_case["Data"]["Dokumentliste"]["ContentReference"], list):
            # If more than one document exists (like in 4Ob72/21y),
            # "ContentReference" contains a list.
            for element in raw_case["Data"]["Dokumentliste"]["ContentReference"]:
                if isinstance(element["Urls"]["ContentUrl"], dict):
                    content_urls.append(
                        {
                            "Name": element["Name"],
                            "Datatype": element["Urls"]["ContentUrl"]["DataType"],
                            "Url": element["Urls"]["ContentUrl"]["Url"],
                        }
                    )

                else:
                    for url in element["Urls"]["ContentUrl"]:
                        content_urls.append(
                            {
                                "Name": element["Name"],
                                "Datatype": url["DataType"],
                                "Url": url["Url"],
                            }
                        )

        else:
            # If only one document exists, "ContentReference" contains a dict.
            for url in raw_case["Data"]["Dokumentliste"]["ContentReference"]["Urls"][
                "ContentUrl"
            ]:
                content_urls.append(
                    {
                        "Name": raw_case["Data"]["Dokumentliste"]["ContentReference"][
                            "Name"
                        ],
                        "Datatype": url["DataType"],
                        "Url": url["Url"],
                    }
                )

    except KeyError:
        pass

    finally:
        return content_urls
