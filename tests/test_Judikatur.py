from risApiWrapper.Judikatur import *


def testJudikaturEntscheidungstext():
    """Test an API call to get a case"""

    wrapperInstance = Justiz(caseNumber="13Os65/21i")
    response = wrapperInstance.info()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]["caseNumber"][0] == "13Os65/21i"
    assert response[0]["type"] == "Entscheidungstext"
    assert response[0].keys() >= {"type", "caseNumber", "europeanCaseLawIdentifier", "judicialBody", "decisionDate", "published", "edited", "legalNorms", "dokumentUrl", "contentUrls"}

