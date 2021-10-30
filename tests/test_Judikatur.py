from risApiWrapper.Judikatur import *
import pytest


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("5Ob234/20b", True, False), ("5Ob234/20b", False, True)],
)
def test_justiz(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Justiz()"""

    wrapper_instance = Justiz(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "keywords,sort_key,ascending",
    [
        ("unlauterer Wettbewerb", "case_number", False),
        ("unlauterer Wettbewerb", "rechtssatz_number", True),
    ],
)
def test_sort(keywords, sort_key, ascending):
    """Test an API call for Justiz() to get a sorted list"""

    wrapper_instance = Justiz(keywords=keywords, published="EinemMonat")
    response = wrapper_instance.info(sort_key=sort_key)
    if ascending:
        assert all(
            response[i]["case_number"] >= response[i + 1]["case_number"]
            for i in range(len(response) - 1)
        )
    else:
        assert all(
            response[i]["case_number"] <= response[i + 1]["case_number"]
            for i in range(len(response) - 1)
        )


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("E3310/2020", True, False), ("E3310/2020", False, True)],
)
def test_vfgh(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Vfgh()"""

    wrapper_instance = Vfgh(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("Ra 2018/22/0098", True, False), ("Ra 2018/22/0098", False, True)],
)
def test_vwgh(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Vwgh()"""

    wrapper_instance = Vwgh(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list)
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("W241 2175652-1", True, False), ("W241 2175652-1", False, True)],
)
def test_bvwg(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Bvwg()"""

    wrapper_instance = Bvwg(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [
        ("LVwG-AV-953/001-2021", True, False),
        ("LVwG-AV-953/001-2021", False, True),
    ],
)
def test_lvwg(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Lvwg()"""

    wrapper_instance = Lvwg(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize("case_number", ["B-GBK I/263/21", "B-GBK II/161/21"])
def test_gbk(case_number):
    """Test an API call for Gbk()"""

    wrapper_instance = Gbk(case_number=case_number)
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [
        ("DSB-D122.259/0008-DSB/2015", True, False),
        ("DSB-D122.259/0008-DSB/2015", False, True),
    ],
)
def test_dsk(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Dsk()"""

    wrapper_instance = Dsk(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("DG/001/2018", True, False), ("DG/001/2018", False, True)],
)
def test_dok(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Dok()"""

    wrapper_instance = Dok(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"


@pytest.mark.parametrize(
    "case_number,entscheidungstexte,rechtssaetze",
    [("B2-PVAB/21", True, False), ("B2-PVAB/21", False, True)],
)
def test_pvak(case_number, entscheidungstexte, rechtssaetze):
    """Test an API call for Pvak()"""

    wrapper_instance = Pvak(
        case_number=case_number,
        show_rechtssaetze=rechtssaetze,
        show_entscheidungstexte=entscheidungstexte,
    )
    response = wrapper_instance.info()

    assert isinstance(response, list), "checks whether .info() returns a list"
    for item in wrapper_instance:
        assert isinstance(
            item, dict
        ), "checks whether the individual items are dicts"
        assert any(
            case_number in case_number for case_number in item["case_number"]
        ), "checks whether the queried case number is found"
        if entscheidungstexte and not rechtssaetze:
            assert (
                item["type"] == "Entscheidungstext"
            ), "checks whether all found items are of type 'Entscheidungstext'"
        elif rechtssaetze and not entscheidungstexte:
            assert (
                item["type"] == "Rechtssatz"
            ), "checks whether all found items are of type 'Rechtssatz'"
        assert all(
            key in item.keys()
            for key in {
                "type",
                "case_number",
                "european_case_law_identifier",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
                "legal_norms",
                "document_url",
                "content_urls",
                "rechtssatz_number",
            }
        ), "checks whether an item has all desired fields"
