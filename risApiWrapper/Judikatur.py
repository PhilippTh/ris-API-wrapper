import requests
from dataclasses import dataclass

@dataclass
class Justiz():
    '''
    Creates an iterable object representing a list of queried cases by civil or criminal courts.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
                
        arguments = {"Applikation": "Justiz", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}
        
        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Vfgh():
    '''
    Creates an iterable object representing a list of queried cases by the constitutional court.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, vfgh_entscheidungsart="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("vfgh_entscheidungsart", vfgh_entscheidungsart, ["Undefined", "Beschluss", "Erkenntnis", "Vergleich"])

        arguments = {"Applikation": "Vfgh", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "VfghRequestEntscheidungsart": vfgh_entscheidungsart}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self._results = _convert_results(response)

    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Vwgh():
    '''
    Creates an iterable object representing a list of queried cases by the high administrative court.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, vwgh_entscheidungsart="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("vwgh_entscheidungsart", vwgh_entscheidungsart, ["Undefined", "Beschluss", "Erkenntnis", "BeschlussVS", "ErkenntnisVS"])

        arguments = {"Applikation": "Vwgh", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "VwghRequestEntscheidungsart": vwgh_entscheidungsart}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Bvwg():
    '''
    Creates an iterable object representing a list of queried cases by the state administrative court.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, bvwg_entscheidungsart="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("bvwg_entscheidungsart", bvwg_entscheidungsart, ["Undefined", "Beschluss", "Erkenntnis"])

        arguments = {"Applikation": "Bvwg", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "BvwgRequestEntscheidungsart": bvwg_entscheidungsart}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Lvwg():
    '''
    Creates an iterable object representing a list of queried cases by regional administrative courts.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None,  published="Undefined", entscheidungstexte=True, rechtssaetze=True, lvwg_entscheidungsart="Undefined", lvwg_bundesland="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("lvwg_entscheidungsart", lvwg_entscheidungsart, ["Undefined", "Beschluss", "Erkenntnis", "Bescheid"])
        _input_validation("lvwg_bundesland", lvwg_bundesland, ["Undefined", "Burgenland", "Kaernten", "Niederoesterreich", "Oberoesterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"])

        arguments = {"Applikation": "Lvwg", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "LvwgRequestEntscheidungsart": lvwg_entscheidungsart, "LvwgBundesland": lvwg_bundesland}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)

    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Gbk():
    '''
    Creates an iterable object representing a list of queried cases by the "Gleichbehandlungskommission".
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", gbk_entscheidungsart="Undefined", gbk_kommission="Undefined", gbk_senat="Undefined", gbk_diskriminierungsgrund="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("gbk_entscheidungsart", gbk_entscheidungsart, ["Undefined", "Einzelfallpruefungsergebnis", "Gutachten"])
        _input_validation("gbk_kommission", gbk_kommission, ["Undefined", "BundesGleichbehandlungskommission", "Gleichbehandlungskommission"])
        _input_validation("gbk_senat", gbk_senat, ["Undefined", "I", "II", "III"])
        _input_validation("gbk_diskriminierungsgrund", gbk_diskriminierungsgrund, ["Undefined", "Geschlecht", "EthnischeZugehoerigkeit", "Religion", "Weltanschauung", "Alter", "SexuelleOrientierung", "Mehrfachdiskriminierung"])

        arguments = {"Applikation": "Gbk", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "GbkRequestEntscheidungsart": gbk_entscheidungsart, "GbkKommission": gbk_kommission, "GbkSenat": gbk_senat, "GbkDiskriminierungsgrund": gbk_diskriminierungsgrund}

        # There are no Rechtssaetze in Gbk decisions
        response = _request(arguments)

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(tuple(self._results))

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Dsk():
    '''
    Creates an iterable object representing a list of queried cases by the data protecton authority.
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, dsk_entscheidungsart="Undefined", dsk_behoerde="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("dsk_entscheidungsart", dsk_entscheidungsart, ["Undefined", "BescheidBeschwerde", "BescheidInternatDatenverkehr", "BescheidRegistrierung", "Bescheid__46_47_DSG_2000", "BescheidSonstiger", "Empfehlung", "Verfahrensschriftsaetze"])
        _input_validation("dsk_behoerde", dsk_behoerde, ["Undefined", "Datenschutzkommission", "Datenschutzbehoerde"])

        arguments = {"Applikation": "Dsk", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "DskRequestEntscheidungsart": dsk_entscheidungsart, "DskBehoerde": dsk_behoerde}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Dok():
    '''
    Creates an iterable object representing a list of queried cases by the "Disziplinarkommission".
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        
        arguments = {"Applikation": "Dok", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results

@dataclass
class Pvak():
    '''
    Creates an iterable object representing a list of queried cases by the "Personalvertretungsaufsichtsbehörde".
    '''
    def __init__(self, keywords=None, case_number=None, legal_norm=None, from_date=None, to_date=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, pvak_behoerde="Undefined"):
        _input_validation("published", published, ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        _input_validation("pvak_behoerde", pvak_behoerde, ["Undefined", "PersonalvertretungsAufsichtskommission", "Personalvertretungsaufsichtsbehoerde"])

        arguments = {"Applikation": "Pvak", "Suchworte": keywords, "Geschaeftszahl": case_number, "Norm": legal_norm, "EntscheidungsdatumVon": from_date, "EntscheidungsdatumBis": to_date,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "PvakBehoerde": pvak_behoerde}

        response = _request(_rechtssatz_or_enscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convert_results(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sort_key="", ascending=False) -> None:
        '''
        Sorts the queried results. If sorting should not be persistent, use .info() and provide a sort_key in order to receive a sorted list.
        '''
        _sort_results(self._results)

    def info(self, sort_key="", ascending=False) -> list:
        '''
        Retruns a list of queried results. If sorting should be persitent, use .sort() to sort the results.
        '''
        if sort_key:
            return _sort_results(self._results, sort_key=sort_key, ascending=ascending)
        else:
            return self._results


def _request(parameters) -> list:
    response = requests.get("https://data.bka.gv.at/ris/api/v2.5/judikatur", params=parameters).json()

    # Return nothing if no items are found
    if int(response["OgdSearchResult"]["OgdDocumentResults"]["Hits"]["#text"]) == 0:
        return []

    # If only one item is found, "OgdDocumentReference" contains only one dict.
    # If multiple items are found, "OgdDocumentReference" contains a list of dicts.
    results = [response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]] if isinstance(response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"], dict) else response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]

    # If 100 items are found, there may be additional items on the next "page".
    if len(response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]) == 100:
        parameters["Seitennummer"] += 1
        results.append(_request(parameters))

    return results

def _convert_results(raw_results: list) -> list:
    converted_results = []
    for raw_case in raw_results:
        converted_case ={}
        try:
            if raw_case["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"] == "Rechtssatz":
                converted_case["type"] = "Rechtssatz"
                # TODO(PTH) incorporate raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"] for rechtssätze
                try:
                    # Sometimes multiple rechtssatz_number are assigned. This data field should therefore always be a list.
                    converted_case["rechtssatz_number"] = _to_list([raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Rechtssatznummern"]["item"]])
                except KeyError:
                    converted_case["rechtssatz_number"] = None
                try:
                    converted_case["decisions"] =[]
                    if isinstance(raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"], list):
                        for decision in raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"]:
                            converted_case["decisions"].append({"case_number" : decision["Geschaeftszahl"], "judicial_body" : decision["Gericht"], "decision_date" : decision["Entscheidungsdatum"], "document_url" : decision["DokumentUrl"]})
                    else:
                        converted_case["decisions"].append({"case_number" : raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"]["Geschaeftszahl"], 
                        "judicial_body" : raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"]["Gericht"], 
                        "decision_date" : raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"]["Entscheidungsdatum"], 
                        "document_url" : raw_case["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"]["DokumentUrl"]})
                except KeyError:
                    converted_case["decisions"] = None

            elif raw_case["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"] == "Text":
                converted_case["type"] = "Entscheidungstext"
                # In order to allow for sorting lists of "rechtssaetze" and "Entscheidungstexte" by "rechtssatz_number" the following field has to be included.
                converted_case["rechtssatz_number"] = None

        except KeyError:
            # This is the case with all tested decisions by the GBK.
            converted_case["type"] = None

        try:
            # Sometimes multiple case_number are assigned. This data field should therefore always be a list.
            converted_case["case_number"] = _to_list(raw_case["Data"]["Metadaten"]["Judikatur"]["Geschaeftszahl"]["item"])
        except KeyError:
            converted_case["case_number"] = None

        try:
            # Sometimes multiple european_case_law_identifier are assigned. This data field should therefore always be a list.
            converted_case["european_case_law_identifier"] = _to_list(raw_case["Data"]["Metadaten"]["Judikatur"]["EuropeanCaseLawIdentifier"])
        except KeyError:
            converted_case["european_case_law_identifier"] = None

        try:
            converted_case["judicial_body"] = raw_case["Data"]["Metadaten"]["Technisch"]["Organ"]
        except KeyError:
            converted_case["judicial_body"] = None

        try:
            converted_case["decision_date"] = raw_case["Data"]["Metadaten"]["Judikatur"]["Entscheidungsdatum"]
        except KeyError:
            converted_case["decision_date"] = None

        try:
            converted_case["published"] = raw_case["Data"]["Metadaten"]["Allgemein"]["Veroeffentlicht"]
        except KeyError:
            converted_case["published"] = None

        try:
            converted_case["edited"] = raw_case["Data"]["Metadaten"]["Allgemein"]["Geaendert"]
        except KeyError:
            converted_case["edited"] = None

        try:
            # Sometimes multiple norms are assigned. This data field should therefore always be a list.
            converted_case["legal_norms"] = _to_list(raw_case["Data"]["Metadaten"]["Judikatur"]["Normen"]["item"])
        except KeyError:
            converted_case["legal_norms"] = None

        try:
            converted_case["document_url"] = raw_case["Data"]["Metadaten"]["Allgemein"]["DokumentUrl"]
        except KeyError:
            converted_case["document_url"] = None

        try:
            converted_case["content_urls"] =  {}
            for url in raw_case["Data"]["Dokumentliste"]["ContentReference"]["Urls"]["ContentUrl"]:
                converted_case["content_urls"][url["DataType"]] = url["Url"]
        except KeyError:
            converted_case["content_urls"] = None

        converted_results.append(converted_case)

    return converted_results

def _to_list(data) -> list:
    return [data] if isinstance(data, str) else data

def _sort_results(raw_results: list, sort_key: str, ascending: bool) -> list:
    _input_validation("sort_key", sort_key, ["type", "case_number", "european_case_law_identifier", "rechtssatz_number", "judicial_body", "decision_date", "published", "edited"])

    if ascending:
        return sorted(raw_results, key=lambda item: item[sort_key], reverse=True)
    else:
        return sorted(raw_results, key=lambda item: item[sort_key], reverse=False)

def _rechtssatz_or_enscheidungstext(arguments:dict, entscheidungstexte:bool, reschtssaetze:bool) -> dict:
    '''
    "Dokumenttyp[SucheInRechtssaetzen]" and "Dokumenttyp[SucheInEntscheidungstexten]" behave strange.
    If either parameter is provided, no matter if True or False, only results of this class are provided.
    If both parameters are provided only results of the first one are provided.
    '''
    if entscheidungstexte and reschtssaetze:
        return arguments
    if entscheidungstexte and not reschtssaetze:
        arguments["Dokumenttyp[SucheInEntscheidungstexten]"] = True
        return arguments
    if not entscheidungstexte and reschtssaetze:
        arguments["Dokumenttyp[SucheInRechtssaetzen]"] = True
        return arguments
    raise ValueError('"entscheidungstexte" and "reschtssaetze" cannot both be False. Please provide at least one argument as True.')

def _input_validation(key: str, value: str, values: list) -> None:
    '''
    Validates the given inputs if they are accepted by the API.
    '''
    if value not in values:
        raise ValueError('Please provide a valid argument for "{0}". Accepted arguments for "{0}" are "{1}" or "{2}".'.format(key, '", "'.join(values[0:-2], values[-1])))
