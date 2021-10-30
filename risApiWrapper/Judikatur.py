from dataclasses import dataclass
from risApiWrapper.Helper import (
    _request,
    _to_list,
    _sort_results,
    _input_validation,
    _date_input_validation,
)


@dataclass
class _BaseClass:
    """
    A class providing basic functions to be inherited by applications of the
    category "Judikatur".
    """

    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        """
        Sorts the queried results. If sorting should not be persistent, use
        .info() and provide a sort_key in order to receive a sorted list.
        """
        self._results = _sort_results(
            self._results,
            sort_key=sort_key,
            sort_keys=[
                "type",
                "case_number",
                "european_case_law_identifier",
                "rechtssatz_number",
                "judicial_body",
                "decision_date",
                "published",
                "edited",
            ],
            ascending=ascending,
        )

    def info(self, sort_key="", ascending=False) -> list:
        """
        Retruns a list of queried results. If sorting should be persitent, use
        .sort() to sort the results.
        """
        if sort_key:
            return _sort_results(
                self._results,
                sort_key=sort_key,
                sort_keys=[
                    "type",
                    "case_number",
                    "european_case_law_identifier",
                    "rechtssatz_number",
                    "judicial_body",
                    "decision_date",
                    "published",
                    "edited",
                ],
                ascending=ascending,
            )
        else:
            return self._results


class Justiz(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    legal_assessment : str
        Search for specific keywords in the legal assessment only.
    court : str
        Search for desicions by a specific court.
    case_number : str
        Search for a case with a specific number.
    rechtssatz_number : str
        Search for a "Rechtssatz" with specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    official_reference : str
        Search by reference in a official collection.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        legal_assessment=None,
        court=None,
        case_number=None,
        rechtssatz_number=None,
        legal_norm=None,
        official_reference=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Justiz",
            "Suchworte": keywords,
            "RechtlicheBeurteilung": legal_assessment,
            "Gericht": court,
            "Geschaeftszahl": case_number,
            "Rechtssatznummer": rechtssatz_number,
            "Norm": legal_norm,
            "Fundstelle": official_reference,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Vfgh(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    official_reference : str
        Search by reference in a official collection.
    index : str
        Search for cases via the official classification of areas of Austrian
        law.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    type_of_decision : {"Undefined", "Beschluss", "Erkenntnis", "Vergleich"}
        Search only for certain types of decisions.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        official_reference=None,
        index=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        type_of_decision="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            ["Undefined", "Beschluss", "Erkenntnis", "Vergleich"],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Vfgh",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "Sammlungsnummer": official_reference,
            "Index": index,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "VfghRequestEntscheidungsart": type_of_decision,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Vwgh(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    official_reference : str
        Search by reference in a official collection.
    index : str
        Search for cases via the official classification of areas of Austrian
        law.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    type_of_decision : {"Undefined", "Beschluss", "Erkenntnis", "BeschlussVS",
                        "ErkenntnisVS"}
        Search only for certain types of decisions.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        official_reference=None,
        index=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        type_of_decision="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            [
                "Undefined",
                "Beschluss",
                "Erkenntnis",
                "BeschlussVS",
                "ErkenntnisVS",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Vwgh",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "Sammlungsnummer": official_reference,
            "Index": index,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "VwghRequestEntscheidungsart": type_of_decision,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Bvwg(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    type_of_decision : {"Undefined", "Beschluss", "Erkenntnis"}
        Search only for certain types of decisions.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        type_of_decision="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            ["Undefined", "Beschluss", "Erkenntnis"],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Bvwg",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "BvwgRequestEntscheidungsart": type_of_decision,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Lvwg(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    type_of_decision : {"Undefined", "Beschluss", "Erkenntnis", "Bescheid"}
        Search only for certain types of decisions.
    federal_state : {"Undefined", "Burgenland", "Kaernten",
                     "Niederoesterreich", "Oberoesterreich", "Salzburg",
                     "Steiermark", "Tirol", "Vorarlberg", "Wien"}
        Search only for decisions by a court of a specific federal state.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        type_of_decision="Undefined",
        federal_state="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            ["Undefined", "Beschluss", "Erkenntnis", "Bescheid"],
        )
        _input_validation(
            "federal_state",
            federal_state,
            [
                "Undefined",
                "Burgenland",
                "Kaernten",
                "Niederoesterreich",
                "Oberoesterreich",
                "Salzburg",
                "Steiermark",
                "Tirol",
                "Vorarlberg",
                "Wien",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Lvwg",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "LvwgRequestEntscheidungsart": type_of_decision,
            "LvwgBundesland": federal_state,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Gbk(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    type_of_decision : {"Undefined", "Einzelfallpruefungsergebnis",
                        "Gutachten"}
        Search only for certain types of decisions.
    commission : {"Undefined", "BundesGleichbehandlungskommission",
                  "Gleichbehandlungskommission"}
        Search only for decisions by a specific commission.
    senat : {"Undefined", "I", "II", "III"}
        Search only for decisions by a specific senat.
    reason_for_discrimination : {"Undefined", "Geschlecht",
                                 "EthnischeZugehoerigkeit", "Religion",
                                 "Weltanschauung", "Alter",
                                 "SexuelleOrientierung",
                                 "Mehrfachdiskriminierung"}
        Search only for decisions concerning a specific reason for
        discrimination.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        type_of_decision="Undefined",
        commission="Undefined",
        senat="Undefined",
        reason_for_discrimination="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            ["Undefined", "Einzelfallpruefungsergebnis", "Gutachten"],
        )
        _input_validation(
            "commission",
            commission,
            [
                "Undefined",
                "BundesGleichbehandlungskommission",
                "Gleichbehandlungskommission",
            ],
        )
        _input_validation("senat", senat, ["Undefined", "I", "II", "III"])
        _input_validation(
            "reason_for_discrimination",
            reason_for_discrimination,
            [
                "Undefined",
                "Geschlecht",
                "EthnischeZugehoerigkeit",
                "Religion",
                "Weltanschauung",
                "Alter",
                "SexuelleOrientierung",
                "Mehrfachdiskriminierung",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Gbk",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "GbkRequestEntscheidungsart": type_of_decision,
            "GbkKommission": commission,
            "GbkSenat": senat,
            "GbkDiskriminierungsgrund": reason_for_discrimination,
        }

        # There are no Rechtssaetze in Gbk decisions
        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur", arguments
        )

        self._results = _convert_results(response)


class Dsk(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    type_of_decision : {"Undefined", "Beschluss", "Erkenntnis", "Bescheid"}
        Search only for certain types of decisions.
    authority : {"Undefined", "Datenschutzkommission", "Datenschutzbehoerde"}
        Search only for decisions by a specific authority.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        type_of_decision="Undefined",
        authority="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "type_of_decision",
            type_of_decision,
            [
                "Undefined",
                "BescheidBeschwerde",
                "BescheidInternatDatenverkehr",
                "BescheidRegistrierung",
                "Bescheid__46_47_DSG_2000",
                "BescheidSonstiger",
                "Empfehlung",
                "Verfahrensschriftsaetze",
            ],
        )
        _input_validation(
            "authority",
            authority,
            ["Undefined", "Datenschutzkommission", "Datenschutzbehoerde"],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Dsk",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "DskRequestEntscheidungsart": type_of_decision,
            "DskBehoerde": authority,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Dok(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Dok",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


class Pvak(_BaseClass):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in the whole decisions.
    case_number : str
        Search for a case with a specific number.
    legal_norm : str
        Search for cases concerning a specific legal norm.
    decision_date_from : str
        Search for decisions decided after a certain date. Format YYYY-mm-dd.
    decision_date_to : str
        Search for decisions decided before a certain date. Format YYYY-mm-dd.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for decisions published within a certain period of time.
    show_entscheidungstexte : bool, default True
        Whether "Entscheideungstexte" should be included.
    show_rechtssaetze : bool, default True
        Whether "Rechtssätze" should be included.
    authority : {"Undefined", "PersonalvertretungsAufsichtskommission",
                 "Personalvertretungsaufsichtsbehoerde"}
        Search only for decisions by a specific authority.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried cases by
        civil or criminal courts.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        case_number=None,
        legal_norm=None,
        decision_date_from=None,
        decision_date_to=None,
        published="Undefined",
        show_entscheidungstexte=True,
        show_rechtssaetze=True,
        authority="Undefined",
    ):
        _input_validation(
            "published",
            published,
            [
                "Undefined",
                "EinerWoche",
                "ZweiWochen",
                "EinemMonat",
                "DreiMonaten",
                "SechsMonaten",
                "EinemJahr",
            ],
        )
        _input_validation(
            "authority",
            authority,
            [
                "Undefined",
                "PersonalvertretungsAufsichtskommission",
                "Personalvertretungsaufsichtsbehoerde",
            ],
        )

        _date_input_validation("decision_date_from", decision_date_from)
        _date_input_validation("decision_date_to", decision_date_to)

        arguments = {
            "Applikation": "Pvak",
            "Suchworte": keywords,
            "Geschaeftszahl": case_number,
            "Norm": legal_norm,
            "EntscheidungsdatumVon": decision_date_from,
            "EntscheidungsdatumBis": decision_date_to,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
            "PvakBehoerde": authority,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/judikatur",
            _rechtssatz_or_enscheidungstext(
                arguments, show_entscheidungstexte, show_rechtssaetze
            ),
        )

        self._results = _convert_results(response)


def _convert_results(raw_results: list) -> list:
    # TODO(PTH) we should refactor this
    converted_results = []
    for raw_case in raw_results:
        converted_case = {}
        try:
            if (
                raw_case["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"]
                == "Rechtssatz"
            ):
                converted_case["type"] = "Rechtssatz"
                # TODO(PTH) incorporate raw_case["Data"]["Metadaten"]
                # ["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"] for
                # rechtssätze
                try:
                    # Sometimes multiple rechtssatz_number are assigned. This
                    # data field should therefore always be a list.
                    converted_case["rechtssatz_number"] = _to_list(
                        [
                            raw_case["Data"]["Metadaten"]["Judikatur"][
                                "Justiz"
                            ]["Rechtssatznummern"]["item"]
                        ]
                    )
                except KeyError:
                    converted_case["rechtssatz_number"] = None
                try:
                    converted_case["decisions"] = []
                    if isinstance(
                        raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"][
                            "Entscheidungstexte"
                        ]["item"],
                        list,
                    ):
                        for decision in raw_case["Data"]["Metadaten"][
                            "Judikatur"
                        ]["Justiz"]["Entscheidungstexte"]["item"]:
                            converted_case["decisions"].append(
                                {
                                    "case_number": decision["Geschaeftszahl"],
                                    "judicial_body": decision["Gericht"],
                                    "decision_date": decision[
                                        "Entscheidungsdatum"
                                    ],
                                    "document_url": decision["DokumentUrl"],
                                }
                            )
                    else:
                        converted_case["decisions"].append(
                            {
                                "case_number": raw_case["Data"]["Metadaten"][
                                    "Judikatur"
                                ]["Justiz"]["Entscheidungstexte"]["item"][
                                    "Geschaeftszahl"
                                ],
                                "judicial_body": raw_case["Data"]["Metadaten"][
                                    "Judikatur"
                                ]["Justiz"]["Entscheidungstexte"]["item"][
                                    "Gericht"
                                ],
                                "decision_date": raw_case["Data"]["Metadaten"][
                                    "Judikatur"
                                ]["Justiz"]["Entscheidungstexte"]["item"][
                                    "Entscheidungsdatum"
                                ],
                                "document_url": raw_case["Data"]["Metadaten"][
                                    "Judikatur"
                                ]["Justiz"]["Entscheidungstexte"]["item"][
                                    "DokumentUrl"
                                ],
                            }
                        )
                except KeyError:
                    converted_case["decisions"] = None

            elif (
                raw_case["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"]
                == "Text"
            ):
                converted_case["type"] = "Entscheidungstext"
                # In order to allow for sorting lists of "rechtssaetze" and
                # "Entscheidungstexte" by "rechtssatz_number" the following
                # field has to be included.
                converted_case["rechtssatz_number"] = None

        except KeyError:
            # This is the case with all tested decisions by the GBK.
            converted_case["type"] = None

        try:
            # Sometimes multiple case_number are assigned. This data field
            # should therefore always be a list.
            converted_case["case_number"] = _to_list(
                raw_case["Data"]["Metadaten"]["Judikatur"]["Geschaeftszahl"][
                    "item"
                ]
            )
        except KeyError:
            converted_case["case_number"] = None

        try:
            # Sometimes multiple european_case_law_identifier are assigned.
            # This data field should therefore always be a list.
            converted_case["european_case_law_identifier"] = _to_list(
                raw_case["Data"]["Metadaten"]["Judikatur"][
                    "EuropeanCaseLawIdentifier"
                ]
            )
        except KeyError:
            converted_case["european_case_law_identifier"] = None

        try:
            converted_case["judicial_body"] = raw_case["Data"]["Metadaten"][
                "Technisch"
            ]["Organ"]
        except KeyError:
            converted_case["judicial_body"] = None

        try:
            converted_case["decision_date"] = raw_case["Data"]["Metadaten"][
                "Judikatur"
            ]["Entscheidungsdatum"]
        except KeyError:
            converted_case["decision_date"] = None

        try:
            converted_case["published"] = raw_case["Data"]["Metadaten"][
                "Allgemein"
            ]["Veroeffentlicht"]
        except KeyError:
            converted_case["published"] = None

        try:
            converted_case["edited"] = raw_case["Data"]["Metadaten"][
                "Allgemein"
            ]["Geaendert"]
        except KeyError:
            converted_case["edited"] = None

        try:
            # Sometimes multiple norms are assigned. This data field should
            # therefore always be a list.
            converted_case["legal_norms"] = _to_list(
                raw_case["Data"]["Metadaten"]["Judikatur"]["Normen"]["item"]
            )
        except KeyError:
            converted_case["legal_norms"] = None

        try:
            converted_case["document_url"] = raw_case["Data"]["Metadaten"][
                "Allgemein"
            ]["DokumentUrl"]
        except KeyError:
            converted_case["document_url"] = None

        try:
            converted_case["content_urls"] = {}
            for url in raw_case["Data"]["Dokumentliste"]["ContentReference"][
                "Urls"
            ]["ContentUrl"]:
                converted_case["content_urls"][url["DataType"]] = url["Url"]
        except KeyError:
            converted_case["content_urls"] = None

        converted_results.append(converted_case)

    return converted_results


def _rechtssatz_or_enscheidungstext(
    arguments: dict, show_entscheidungstexte: bool, show_rechtssaetze: bool
) -> dict:
    """
    "Dokumenttyp[SucheInRechtssaetzen]" or
    "Dokumenttyp[SucheInEntscheidungstexten]" require "On" if the
    corresponding information should be shown. If the corresponding
    information should not be shown, no parameter should be provided.
    """
    if show_entscheidungstexte and show_rechtssaetze:
        return arguments
    if show_entscheidungstexte and not show_rechtssaetze:
        arguments["Dokumenttyp[SucheInEntscheidungstexten]"] = "On"
        return arguments
    if not show_entscheidungstexte and show_rechtssaetze:
        arguments["Dokumenttyp[SucheInRechtssaetzen]"] = "On"
        return arguments
    raise ValueError(
        '"show_entscheidungstexte" and "show_rechtssaetze" cannot both be'
        " False. Please provide at least one argument as True."
    )
