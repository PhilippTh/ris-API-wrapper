import requests
from dataclasses import dataclass

@dataclass
class Justiz():
    '''
    Creates an iterable object representing a list of queried cases by civil or criminal courts.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')
                
        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}
        
        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self._results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Vfgh():
    '''
    Creates an iterable object representing a list of queried cases by the constitutional court.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, VfghRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if VfghRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "Vergleich"]:
            raise ValueError('Please provide a valid argument for "VfghRequestEntscheidungsart". The API accepts "Undefined", "Beschluss", "Erkenntnis"or "Vergleich".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "VfghRequestEntscheidungsart": VfghRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self.results = _convertResults(response)

    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Vwgh():
    '''
    Creates an iterable object representing a list of queried cases by the high administrative court.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, VwghRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if VwghRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "BeschlussVS", "ErkenntnisVS"]:
            raise ValueError('Please provide a valid argument for "VwghRequestEntscheidungsart". The API accepts "Undefined", "Beschluss", "Erkenntnis", "BeschlussVS" or "ErkenntnisVS".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "VwghRequestEntscheidungsart": VwghRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Bvwg():
    '''
    Creates an iterable object representing a list of queried cases by the state administrative court.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, BvwgRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if BvwgRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis"]:
            raise ValueError('Please provide a valid argument for "BvwgRequestEntscheidungsart". The API accepts "Undefined", "Beschluss" or "Erkenntnis".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "BvwgRequestEntscheidungsart": BvwgRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Lvwg():
    '''
    Creates an iterable object representing a list of queried cases by regional administrative courts.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None,  published="Undefined", entscheidungstexte=True, rechtssaetze=True, LvwgRequestEntscheidungsart="Undefined", LvwgBundesland="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if LvwgRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "Bescheid"]:
            raise ValueError('Please provide a valid argument for "LvwgRequestEntscheidungsart". The API accepts "Undefined", "Beschluss", "Erkenntnis" or "Bescheid".')

        if LvwgBundesland not in ["Undefined", "Burgenland", "Kaernten", "Niederoesterreich", "Oberoesterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"]:
            raise ValueError('Please provide a valid argument for "LvwgBundesland". The API accepts "Undefined", "Burgenland", "Kaernten", "Niederoesterreich", "Oberoesterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg" or "Wien".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "LvwgRequestEntscheidungsart": LvwgRequestEntscheidungsart, "LvwgBundesland": LvwgBundesland}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Gbk():
    '''
    Creates an iterable object representing a list of queried cases by the "Gleichbehandlungskommission".
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, GbkRequestEntscheidungsart="Undefined", GbkKommission="Undefined", GbkSenat="Undefined", GbkDiskriminierungsgrund="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if GbkRequestEntscheidungsart not in ["Undefined", "Einzelfallpruefungsergebnis", "Gutachten"]:
            raise ValueError('Please provide a valid argument for "GbkRequestEntscheidungsart". The API accepts "Undefined", "Einzelfallpruefungsergebnis" or "Gutachten".')

        if GbkKommission not in ["Undefined", "BundesGleichbehandlungskommission", "Gleichbehandlungskommission"]:
            raise ValueError('Please provide a valid argument for "GbkKommission". The API accepts "Undefined", "BundesGleichbehandlungskommission" or "Gleichbehandlungskommission".')

        if GbkSenat not in ["Undefined", "I", "II", "III"]:
            raise ValueError('Please provide a valid argument for "GbkSenat". The API accepts "Undefined", "I", "II" or "III".')

        if GbkDiskriminierungsgrund not in ["Undefined", "Geschlecht", "EthnischeZugehoerigkeit", "Religion", "Weltanschauung", "Alter", "SexuelleOrientierung", "Mehrfachdiskriminierung"]:
            raise ValueError('Please provide a valid argument for "GbkDiskriminierungsgrund". The API accepts "Undefined", "Geschlecht", "EthnischeZugehoerigkeit", "Religion", "Weltanschauung", "Alter", "SexuelleOrientierung" or "Mehrfachdiskriminierung".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "GbkRequestEntscheidungsart": GbkRequestEntscheidungsart, "GbkKommission": GbkKommission, "GbkSenat": GbkSenat, "GbkDiskriminierungsgrund": GbkDiskriminierungsgrund}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(tuple(self._results))

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Dsk():
    '''
    Creates an iterable object representing a list of queried cases by the data protecton authority.
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, DskRequestEntscheidungsart="Undefined", DskBehoerde="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if DskRequestEntscheidungsart not in ["Undefined", "BescheidBeschwerde", "BescheidInternatDatenverkehr", "BescheidRegistrierung", "Bescheid__46_47_DSG_2000", "BescheidSonstiger", "Empfehlung", "Verfahrensschriftsaetze"]:
            raise ValueError('Please provide a valid argument for "DskRequestEntscheidungsart". The API accepts "Undefined", "BescheidBeschwerde", "BescheidInternatDatenverkehr", "BescheidRegistrierung", "Bescheid__46_47_DSG_2000", "BescheidSonstiger", "Empfehlung" or "Verfahrensschriftsaetze".')

        if DskBehoerde not in ["Undefined", "Datenschutzkommission", "Datenschutzbehoerde"]:
            raise ValueError('Please provide a valid argument for "DskBehoerde". The API accepts "Undefined", "Datenschutzkommission" or "Datenschutzbehoerde".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "DskRequestEntscheidungsart": DskRequestEntscheidungsart, "DskBehoerde": DskBehoerde}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Dok():
    '''
    Creates an iterable object representing a list of queried cases by the "Disziplinarkommission".
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')
        
        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
        else:
            return self._results

@dataclass
class Pvak():
    '''
    Creates an iterable object representing a list of queried cases by the "Personalvertretungsaufsichtsbehörde".
    '''
    def __init__(self, keywords=None, caseNumber=None, legalNorm=None, fromDate=None, toDate=None, published="Undefined", entscheidungstexte=True, rechtssaetze=True, PvakBehoerde="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValueError('Please provide a valid argument for "published". The API accepts "Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten" or "EinemJahr".')

        if PvakBehoerde not in ["Undefined", "PersonalvertretungsAufsichtskommission", "Personalvertretungsaufsichtsbehoerde"]:
            raise ValueError('Please provide a valid argument for "PvakBehoerde". The API accepts "Undefined", "PersonalvertretungsAufsichtskommission" or "Personalvertretungsaufsichtsbehoerde".')

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "PvakBehoerde": PvakBehoerde}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)
    
    def __iter__(self):
        return iter(self._results)

    def __len__(self):
        return len(self._results)

    def sort(self, sortKey="", ascending=False) -> None:
        '''
        Sorts the queried results.
        '''
        _sortResults(self._results)

    def info(self, sortKey="", ascending=False) -> list:
        '''
        Retruns a sorted list of queried results.
        '''
        if sortKey:
            return _sortResults(self._results, sortKey=sortKey, ascending=ascending)
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

def _convertResults(rawResults: list) -> list:
    convertedResults = []
    for rawCase in rawResults:
        convertedCase ={}
        if rawCase["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"] == "Rechtssatz":
            pass
            convertedCase["type"] = "Rechtssatz"
            # TODO(PTH) incorporate rawCase["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Entscheidungstexte"]["item"] for rechtssätze
            try:
                # Sometimes multiple Rechtssatznummer are assigned. This data field should therefore always be a list.
                convertedCase["rechtssatznummer"] = _toList([rawCase["Data"]["Metadaten"]["Judikatur"]["Justiz"]["Rechtssatznummern"]["item"]])
            except KeyError:
                convertedCase["rechtssatznummer"] = None

        elif rawCase["Data"]["Metadaten"]["Judikatur"]["Dokumenttyp"] == "Text":
            convertedCase["type"] = "Entscheidungstext"

        else:
            # This should never be the case!
            convertedCase["type"] = None

        try:
            # Sometimes multiple caseNumber are assigned. This data field should therefore always be a list.
            convertedCase["caseNumber"] = _toList(rawCase["Data"]["Metadaten"]["Judikatur"]["Geschaeftszahl"]["item"])
        except KeyError:
            convertedCase["caseNumber"] = None

        try:
            # Sometimes multiple europeanCaseLawIdentifier are assigned. This data field should therefore always be a list.
            convertedCase["europeanCaseLawIdentifier"] = _toList(rawCase["Data"]["Metadaten"]["Judikatur"]["EuropeanCaseLawIdentifier"])
        except KeyError:
            convertedCase["europeanCaseLawIdentifier"] = None

        try:
            convertedCase["judicialBody"] = rawCase["Data"]["Metadaten"]["Technisch"]["Organ"]
        except KeyError:
            convertedCase["judicialBody"] = None

        try:
            convertedCase["decisionDate"] = rawCase["Data"]["Metadaten"]["Judikatur"]["Entscheidungsdatum"]
        except KeyError:
            convertedCase["decisionDate"] = None

        try:
            # Sometimes multiple europeanCaseLawIdentifier are assigned. This data field should therefore always be list.
            convertedCase["published"] = _toList(rawCase["Data"]["Metadaten"]["Allgemein"]["Veroeffentlicht"])
        except KeyError:
            convertedCase["published"] = None

        try:
            convertedCase["edited"] = rawCase["Data"]["Metadaten"]["Allgemein"]["Geaendert"]
        except KeyError:
            convertedCase["edited"] = None

        try:
            # Sometimes multiple europeanCaseLawIdentifier are assigned. This data field should therefore always be a list.
            convertedCase["legalNorms"] = _toList(rawCase["Data"]["Metadaten"]["Judikatur"]["Normen"]["item"])
        except KeyError:
            convertedCase["legalNorms"] = None

        try:
            convertedCase["dokumentUrl"] = rawCase["Data"]["Metadaten"]["Allgemein"]["DokumentUrl"]
        except KeyError:
            convertedCase["dokumentUrl"] = None

        try:
            convertedCase["contentUrls"] =  {}
            for url in rawCase["Data"]["Dokumentliste"]["ContentReference"]["Urls"]["ContentUrl"]:
                convertedCase["contentUrls"][url["DataType"]] = url["Url"]
        except KeyError:
            convertedCase["contentUrls"] = None

        convertedResults.append(convertedCase)

    return convertedResults

def _toList(data) -> list:
    return [data] if isinstance(data, str) else data

def _sortResults(rawResults: list, sortKey: str, ascending: bool) -> list:
    if sortKey not in ["type", "caseNumber", "europeanCaseLawIdentifier", "Rechtssatznummer", "judicialBody", "decisionDate", "published", "published", "edited"]:
        raise ValueError('Please provide a valid argument for "sortKey". The results can be sorted by "type", "caseNumber", "europeanCaseLawIdentifier", "Rechtssatznummer", "judicialBody", "decisionDate", "published", "published" or "edited".')
    else:
        # TODO(PTH) implement sort algorithm; check to make rechtssatznummer work; problems with dates?; many fields can be lists
        return rawResults

def _rechtssatzOrEnscheidungstext(arguments:dict, entscheidungstexte:bool, reschtssaetze:bool) -> dict:
    '''
    "Dokumenttyp[SucheInRechtssaetzen]" and "Dokumenttyp[SucheInEntscheidungstexten]" behave strange.
    If either parameter is provided, no matter if True or False, only results of this class are provided.
    If both parameters are provided only results of the first one are provided.
    '''
    if entscheidungstexte and reschtssaetze:
        return arguments
    if entscheidungstexte and not reschtssaetze:
        arguments["Dokumenttyp[SucheInEntscheidungstexten]"] = [True]
        return arguments
    if not entscheidungstexte and reschtssaetze:
        arguments["Dokumenttyp[SucheInRechtssaetzen]"] = [True]
        return arguments
    raise ValueError('"entscheidungstexte" and "reschtssaetze" cannot both be False. Please provide at least one argument as True.')
