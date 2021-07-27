import requests
import ValidationError


class Justiz():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        
        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}
        
        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Vfgh():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, VfghRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if VfghRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "Vergleich"]:
            raise ValidationError(
                "VfghRequestEntscheidungsart", ["Undefined", "Beschluss", "Erkenntnis", "Vergleich"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "VfghRequestEntscheidungsart": VfghRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Vwgh():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, VwghRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if VwghRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "BeschlussVS", "ErkenntnisVS"]:
            raise ValidationError(
                "VwghRequestEntscheidungsart", ["Undefined", "Beschluss", "Erkenntnis", "BeschlussVS", "ErkenntnisVS"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "VwghRequestEntscheidungsart": VwghRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Bvwg():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, BvwgRequestEntscheidungsart="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if BvwgRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis"]:
            raise ValidationError(
                "BvwgRequestEntscheidungsart", ["Undefined", "Beschluss", "Erkenntnis"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "BvwgRequestEntscheidungsart": BvwgRequestEntscheidungsart}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))
        
        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Lvwg():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate,  published="Undefined", entscheidungstexte=True, rechtssaetze=True, LvwgRequestEntscheidungsart="Undefined", LvwgBundesland="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if LvwgRequestEntscheidungsart not in ["Undefined", "Beschluss", "Erkenntnis", "Bescheid"]:
            raise ValidationError(
                "LvwgRequestEntscheidungsart", ["Undefined", "Beschluss", "Erkenntnis", "Bescheid"])

        if LvwgBundesland not in ["Undefined", "Burgenland", "Kaernten", "Niederoesterreich", "Oberoesterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"]:
            raise ValidationError(
                "LvwgBundesland", ["Undefined", "Burgenland", "Kaernten", "Niederoesterreich", "Oberoesterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "LvwgRequestEntscheidungsart": LvwgRequestEntscheidungsart, "LvwgBundesland": LvwgBundesland}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Gbk():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, GbkRequestEntscheidungsart="Undefined", GbkKommission="Undefined", GbkSenat="Undefined", GbkDiskriminierungsgrund="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if GbkRequestEntscheidungsart not in ["Undefined", "Einzelfallpruefungsergebnis", "Gutachten"]:
            raise ValidationError(
                "GbkRequestEntscheidungsart", ["Undefined", "Einzelfallpruefungsergebnis", "Gutachten"])

        if GbkKommission not in ["Undefined", "BundesGleichbehandlungskommission", "Gleichbehandlungskommission"]:
            raise ValidationError(
                "GbkKommission", ["Undefined", "BundesGleichbehandlungskommission", "Gleichbehandlungskommission"])

        if GbkSenat not in ["Undefined", "I", "II", "III"]:
            raise ValidationError("GbkSenat", ["Undefined", "I", "II", "III"])

        if GbkDiskriminierungsgrund not in ["Undefined", "Geschlecht", "EthnischeZugehoerigkeit", "Religion", "Weltanschauung", "Alter", "SexuelleOrientierung", "Mehrfachdiskriminierung"]:
            raise ValidationError("GbkDiskriminierungsgrund", ["Undefined", "Geschlecht", "EthnischeZugehoerigkeit", "Religion", "Weltanschauung", "Alter", "SexuelleOrientierung", "Mehrfachdiskriminierung"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1,  "GbkRequestEntscheidungsart": GbkRequestEntscheidungsart, "GbkKommission": GbkKommission, "GbkSenat": GbkSenat, "GbkDiskriminierungsgrund": GbkDiskriminierungsgrund}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Dsk():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, DskRequestEntscheidungsart="Undefined", DskBehoerde="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if DskRequestEntscheidungsart not in ["Undefined", "BescheidBeschwerde", "BescheidInternatDatenverkehr", "BescheidRegistrierung", "Bescheid__46_47_DSG_2000", "BescheidSonstiger", "Empfehlung", "Verfahrensschriftsaetze"]:
            raise ValidationError(
                "DskRequestEntscheidungsart", ["Undefined", "BescheidBeschwerde", "BescheidInternatDatenverkehr", "BescheidRegistrierung", "Bescheid__46_47_DSG_2000", "BescheidSonstiger", "Empfehlung", "Verfahrensschriftsaetze"])

        if DskBehoerde not in ["Undefined", "Datenschutzkommission", "Datenschutzbehoerde"]:
            raise ValidationError(
                "DskBehoerde", ["Undefined", "Datenschutzkommission", "Datenschutzbehoerde"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "DskRequestEntscheidungsart": DskRequestEntscheidungsart, "DskBehoerde": DskBehoerde}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Dok():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        
        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Pvak():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True, PvakBehoerde="Undefined"):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        if PvakBehoerde not in ["Undefined", "PersonalvertretungsAufsichtskommission", "Personalvertretungsaufsichtsbehoerde"]:
            raise ValidationError(
                "PvakBehoerde", ["Undefined", "PersonalvertretungsAufsichtskommission", "Personalvertretungsaufsichtsbehoerde"])

        arguments = {"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "PvakBehoerde": PvakBehoerde}

        response = _request(_rechtssatzOrEnscheidungstext(arguments, entscheidungstexte, rechtssaetze))

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)


def _request(parameters):
    response = requests.get("https://data.bka.gv.at/ris/api/v2.5/judikatur", params=parameters).json()

    # Return nothing if no items are found
    if int(response["OgdSearchResult"]["OgdDocumentResults"]["Hits"]["#text"]) == 0:
        return []

    # If only one item is found, "OgdDocumentReference" contains only one dict.
    # If multiple items are found, "OgdDocumentReference" contains a list of dicts.
    results = [response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]] if isinstance(response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"], dict) else response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]

    # If 100 items are found, there may be additional items on the next "page".
    if len(response["OgdSearchResult"]["OgdDocumentResults"]["OgdDocumentReference"]) == 100:
        parameters["Seitenzahl"] += 1
        results.append(requests(parameters))

    return results

def _convertResults(rawResults: list):
    # TODO(PTH) convert data 
    return rawResults

def _sortResults(rawResults: list, sortKey:str, ascending:bool):
    # TODO(PTH) implement sort algorithm
    return rawResults

def _rechtssatzOrEnscheidungstext(arguments:dict, entscheidungstexte:bool, reschtssaetze:bool):
    """
    This argument behaves strange.
    If either parameter is provided, no matter if True or False, only results of this parameter are provided.
    If both parameters are provided only results of the first one are provided
    """
    if entscheidungstexte and reschtssaetze:
        return arguments
    if entscheidungstexte and not reschtssaetze:
        return arguments["Dokumenttyp[SucheInEntscheidungstexten]" : True]
    if not entscheidungstexte and reschtssaetze:
        return arguments["Dokumenttyp[SucheInRechtssaetzen]" : True]
    raise ValueError('"entscheidungstexte" and "reschtssaetze" cannot both be False. Please provide at least one argument as True.')
    