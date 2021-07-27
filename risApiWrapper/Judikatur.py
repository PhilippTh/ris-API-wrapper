import requests
import ValidationError


class Justiz():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])
        
        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze})

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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "VfghRequestEntscheidungsart": VfghRequestEntscheidungsart})
        
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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "VwghRequestEntscheidungsart": VwghRequestEntscheidungsart})

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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "BvwgRequestEntscheidungsart": BvwgRequestEntscheidungsart})
        
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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "LvwgRequestEntscheidungsart": LvwgRequestEntscheidungsart, "LvwgBundesland": LvwgBundesland})

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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "GbkRequestEntscheidungsart": GbkRequestEntscheidungsart, "GbkKommission": GbkKommission, "GbkSenat": GbkSenat, "GbkDiskriminierungsgrund": GbkDiskriminierungsgrund})

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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "DskRequestEntscheidungsart": DskRequestEntscheidungsart, "DskBehoerde": DskBehoerde})

        self.results = _convertResults(response)

    def info(self, sortKey="caseNumber", ascending=False):
        return _sortResults(self.results)

class Dok():
    def __init__(self, keywords: str, caseNumber: str, legalNorm: str, fromDate, toDate, published="Undefined", entscheidungstexte=True, rechtssaetze=True):
        if published not in ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"]:
            raise ValidationError("published", ["Undefined", "EinerWoche", "ZweiWochen", "EinemMonat", "DreiMonaten", "SechsMonaten", "EinemJahr"])

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze})

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

        response = _request({"Suchworte": keywords, "Geschaeftszahl": caseNumber, "Norm": legalNorm, "EntscheidungsdatumVon": fromDate, "EntscheidungsdatumBis": toDate,"ImRisSeit": published,"DokumenteProSeite": "OneHundred", "Seitennummer": 1, "Dokumenttyp[SucheInEntscheidungstexten]": entscheidungstexte, "Dokumenttyp[SucheInRechtssaetzen]": rechtssaetze, "PvakBehoerde": PvakBehoerde})

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
        parameters["Seitenzahl"] = parameters["Seitenzahl"] +1
        results.append(requests(parameters))

    return results

def _convertResults(rawResults: list):
    # TODO(PTH) convert data 
    return rawResults

def _sortResults(rawResults: list, sortKey:str, ascending:bool):
    # TODO(PTH) implement sort algorithm
    return rawResults

    