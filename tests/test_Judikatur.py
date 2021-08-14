from risApiWrapper.Judikatur import *

def testJustizEntscheidungstext():
    """Test an API call to get a Entscheidungstext"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", rechtssaetze=False)
    response = wrapperInstance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Entscheidungstext", "checks whether all found items are of type 'Entschiedungstext'"
        assert item.keys() >= {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "dokumentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

def testJustizRechtssatz():
    """Test an API call to get a Rechtssatz"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    for item in wrapperInstance:
        assert isinstance(item, dict), "checks whether the individual items are dicts"
        assert "5Ob234/20b" in item["caseNumber"], "checks whether the wanted case number is found"
        assert item["type"] == "Rechtssatz", "checks whether all found items are of type 'Rechtssatz'"
        assert item.keys() >= {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "dokumentUrl", "contentUrls"}, "checks whether an item has all desired  fields"

