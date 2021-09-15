from risApiWrapper.Judikatur import *
import pytest

@pytest.mark.parametrize("case_number,entscheidungstexte,rechtssaetze", [("5Ob234/20b", True, False), ("5Ob234/20b", False, True)])
def test_justiz(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Justiz()"""

    wrapper_instance = Justiz(case_number=case_number, rechtssaetze=rechtssaetze, entscheidungstexte=entscheidungstexte)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert any(case_number in case_number for case_number in item["case_number"]), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
            assert "rechtssatz_number" in item.keys()
        assert all(key in item.keys() for key in {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}), "checks whether an item has all desired fields"

@pytest.mark.parametrize("keywords,sort_key,ascending", [("unlauterer Wettbewerb", "case_number", False), ("unlauterer Wettbewerb", "rechtssatz_number", True)])
def test_sort(keywords, sort_key, ascending):
    """Test an API call for Justiz() to get a sorted list"""

    wrapper_instance = Justiz(keywords=keywords, published="EinemMonat")
    response = wrapper_instance.info(sort_key=sort_key)
    if ascending:
        assert all(response[i]["case_number"] >= response[i+1]["case_number"] for i in range(len(response) - 1))
    else:
        assert all(response[i]["case_number"] <= response[i+1]["case_number"] for i in range(len(response) - 1))

@pytest.mark.parametrize("case_number,entscheidungstexte,rechtssaetze", [("E3310/2020", True, False), ("E3310/2020", False, True)])
def test_vfgh(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Vfgh() to get a Rechtssatz"""

    wrapper_instance = Vfgh(case_number=case_number, rechtssaetze=rechtssaetze, entscheidungstexte=entscheidungstexte)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert any("E3310/2020" in case_number for case_number in item["case_number"]), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
            assert "rechtssatz_number" in item.keys()
        assert all(key in item.keys() for key in {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}), "checks whether an item has all desired fields"

@pytest.mark.parametrize("case_number,entscheidungstexte,rechtssaetze", [("5Ob234/20b", True, False), ("5Ob234/20b", False, True)])
def test_vwgh(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Vwgh() to get a Rechtssatz"""

    wrapper_instance = Vwgh(case_number=case_number, rechtssaetze=rechtssaetze, entscheidungstexte=entscheidungstexte)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert any("So 2021/03/0006" in case_number for case_number in item["case_number"]), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
            assert "rechtssatz_number" in item.keys()
        assert all(key in item.keys() for key in {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}), "checks whether an item has all desired fields"

@pytest.mark.parametrize("case_number,entscheidungstexte,rechtssaetze", [("W241 2175652-1", True, False), ("W241 2175652-1", False, True)])
def test_bvwg(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Bvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number=case_number, rechtssaetze=rechtssaetze, entscheidungstexte=entscheidungstexte)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert any("W241 2175652-1" in case_number for case_number in item["case_number"]), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
            assert "rechtssatz_number" in item.keys()
        assert all(key in item.keys() for key in {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}), "checks whether an item has all desired fields"

@pytest.mark.parametrize("case_number,entscheidungstexte,rechtssaetze", [("LVwG-AV-953/001-2021", True, False), ("LVwG-AV-953/001-2021", False, True)])
def test_lvwg(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Lvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number=case_number, rechtssaetze=rechtssaetze, entscheidungstexte=entscheidungstexte)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert any("LVwG-AV-953/001-2021" in case_number for case_number in item["case_number"]), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
            assert "rechtssatz_number" in item.keys()
        assert all(key in item.keys() for key in {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}), "checks whether an item has all desired fields"

#TODO (PTH) add the remaining tests