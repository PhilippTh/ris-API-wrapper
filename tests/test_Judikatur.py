from risApiWrapper.Judikatur import *

def testJustizEntscheidungstext():
    """Test an API call for Justiz() to get a Entscheidungstext"""

    wrapper_instance = Justiz(case_number="5Ob234/20b", rechtssaetze=False)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        assert item.keys() == {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testJustizRechtssatz():
    """Test an API call for Justiz() to get a Rechtssatz"""

    wrapper_instance = Justiz(case_number="5Ob234/20b", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatz_number", "decisions", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testVfghEntscheidungstext():
    """Test an API call for Vfgh() to get a Rechtssatz"""

    wrapper_instance = Vfgh(case_number="E3310/2020", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "E3310/2020" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        assert item.keys() == {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testVfghRechtssatz():
    """Test an API call for Vfgh() to get a Rechtssatz"""

    wrapper_instance = Vfgh(case_number="E3310/2020", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "E3310/2020" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatz_number", "decisions", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testVwghEntscheidungstext():
    """Test an API call for Vwgh() to get a Rechtssatz"""

    wrapper_instance = Vwgh(case_number="So 2021/03/0006", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "So 2021/03/0006" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        assert item.keys() == {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testVwghRechtssatz():
    """Test an API call for Vwgh() to get a Rechtssatz"""

    wrapper_instance = Vwgh(case_number="So 2021/03/0006", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "So 2021/03/0006" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatz_number", "decisions", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testBvwgEntscheidungstext():
    """Test an API call for Bvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number="W241 2175652-1", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "W241 2175652-1" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        assert item.keys() == {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testBvwgRechtssatz():
    """Test an API call for Bvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number="W241 2175652-1", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "W241 2175652-1" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatz_number", "decisions", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testLvwgEntscheidungstext():
    """Test an API call for Lvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number="LVwG-AV-953/001-2021", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "LVwG-AV-953/001-2021" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entscheidungstext'"
        assert item.keys() == {"type", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"

def testLvwgRechtssatz():
    """Test an API call for Lvwg() to get a Rechtssatz"""

    wrapper_instance = Bvwg(case_number="LVwG-AV-953/001-2021", entscheidungstexte=False)
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "LVwG-AV-953/001-2021" in item["case_number"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatz_number", "decisions", "case_number", "european_case_law_identifier", "judicial_body", "decision_date", "published", "edited", "legal_norms", "document_url", "content_urls"}, "checks whether an item has all desired fields"