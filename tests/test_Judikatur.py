from risApiWrapper.Judikatur import *

def testJustizEntscheidungstext():
    """Test an API call to get a Entscheidungstext"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", rechtssaetze=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    for i in response: 
        assert "5Ob234/20b" in i["caseNumber"]
    for i in response:
        assert i["type"] == "Entscheidungstext"
    assert response[0].keys() >= {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "dokumentUrl", "contentUrls"}

def testJustizRechtssatz():
    """Test an API call to get a Rechtssatz"""

    wrapperInstance = Justiz(caseNumber="5Ob234/20b", entscheidungstexte=False)
    response = wrapperInstance.info()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    for i in response:
        assert "5Ob234/20b" in i["caseNumber"]
    for i in response:
        assert i["type"] == "Rechtssatz"
    assert response[0].keys() >= {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "dokumentUrl", "contentUrls"}

