from risApiWrapper.Judikatur import *

def testJustizEntscheidungstext():
    """Test an API call for Justiz() to get a Entscheidungstext"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", rechtssaetze=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() == {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testJustizRechtssatz():
    """Test an API call for Justiz() to get a Rechtssatz"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatznummer", "decisions", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testVfghEntscheidungstext():
    """Test an API call for Vfgh() to get a Rechtssatz"""

    wrapperInstance = Vfgh(caseNumber="E3310/2020", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "E3310/2020" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() == {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testVfghRechtssatz():
    """Test an API call for Vfgh() to get a Rechtssatz"""

    wrapperInstance = Vfgh(caseNumber="E3310/2020", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "E3310/2020" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatznummer", "decisions", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testVwghEntscheidungstext():
    """Test an API call for Vwgh() to get a Rechtssatz"""

    wrapperInstance = Vwgh(caseNumber="So 2021/03/0006", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "So 2021/03/0006" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() == {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testVwghRechtssatz():
    """Test an API call for Vwgh() to get a Rechtssatz"""

    wrapperInstance = Vwgh(caseNumber="So 2021/03/0006", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "So 2021/03/0006" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatznummer", "decisions", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testBvwgEntscheidungstext():
    """Test an API call for Bvwg() to get a Rechtssatz"""

    wrapperInstance = Bvwg(caseNumber="W241 2175652-1", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "W241 2175652-1" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() == {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testBvwgRechtssatz():
    """Test an API call for Bvwg() to get a Rechtssatz"""

    wrapperInstance = Bvwg(caseNumber="W241 2175652-1", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "W241 2175652-1" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatznummer", "decisions", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testLvwgEntscheidungstext():
    """Test an API call for Lvwg() to get a Rechtssatz"""

    wrapperInstance = Bvwg(caseNumber="LVwG-AV-953/001-2021", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "LVwG-AV-953/001-2021" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() == {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testLvwgRechtssatz():
    """Test an API call for Lvwg() to get a Rechtssatz"""

    wrapperInstance = Bvwg(caseNumber="LVwG-AV-953/001-2021", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "LVwG-AV-953/001-2021" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() == {"type", "rechtssatznummer", "decisions", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "documentUrl", "contentUrls"}, "checks whether an item has all desired  fields"