from dataclasses import dataclass
from risApiWrapper.Helper import (
    _request,
    _sort_results,
    _input_validation,
    _date_input_validation,
)


@dataclass
class _Base_Class:
    """
    A class providing basic functions to be inherited by applications of the
    category "Normen".
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
            sort_keys=["legal_code_name"],
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
                sort_keys=["legal_code_name"],
                ascending=ascending,
            )
        else:
            return self._results


class Bundesnormen(_Base_Class):
    """
    Parameters
    ----------
    keywords : str
        Search for specific keywords in a legal statute.
    legal_code_name : str
        Search within a specific legal code.
    legal_code_number : str
        TODO(PTH): provide description
    index : str
        Search for legal statutes by classification number of the main and
        subgroup of federal law.
    source_type : {"BVG", "BG", "V", "K", "K (Geltungsbereich)",
                   "Entschl. d. BPräs.",
                   "Vereinbarung gem. Art. 15a B-VG",
                   "Geschäftsordnung, Geschäftseinteilung etc.",
                   "Vertrag - mit Angabe des Staates",
                   "Vertrag - mit Angabe einer internationalen Organisation",
                   "Vertrag - Multilateral"}
        Search for legal statutes by type of source. Multiple types can be
        specified. The search operators 'oder' (or) or 'nicht' (not) can also
        be used
    section_type : {"Alle", "Artikel", "Paragraph", "Anlage"}
        Search for a specific type of legal statute or document. 'section_type'
        cannot be specified  without specifying either 'section_from' or
        'section_to' or both.
    section_from : str
        Search for legal statutes from a certain point in the specified section
        type. If 'section_from' is specified, 'section_type' has to be
        specified as well.
    section_to : str
        Search for legal statutes to a certain point in the specified section
        type. If 'section_to' is specified, 'section_type' has to be
        specified as well.
    version_date : str
        Search for a legal statute version from a specific date. If either
        effective_date_from, effective_date_to, expiry_date_from or
        expiry_date_to is provided, version_date cannot be provided at the
        same time.Format YYYY-mm-dd.
    effective_date_from : str
        Search for legal statutes with an effective date after the specified
        date. If version_date is provided, effective_date_from cannot be
        provided at the same time. Format YYYY-mm-dd.
    effective_date_to : str
        Search for legal statutes with an effective date before the specified
        date. If version_date is provided, effective_date_to cannot be
        provided at the same time. Format YYYY-mm-dd.
    expiry_date_from : str
        Search for legal statutes with an expiry date after the specified date.
        If version_date is provided, expiry_date_from cannot be provided at
        the same time.Format YYYY-mm-dd.
    expiry_date_to : str
        Search for legal statutes with an expiry date before the specified
        date. If version_date is provided, expiry_date_to cannot be provided
        at the same time. Format YYYY-mm-dd.
    signing_date : str
        Search for legal statutes in international treaties singed on a
        specific date. Format YYYY-mm-dd.
    publishing_entity : {"BGBl. I Nr. <Nr>", "BGBl. II Nr. <Nr>",
                         "BGBl. III Nr. <Nr>", "BGBl. Nr. <Nr>",
                         "RGBl. Nr. <Nr>", "StGBl. Nr. <Nr>", "ASlg. Nr. <Nr>",
                         "AmtlNHW Nr. <Nr>", "DJ S  <Nr>", "DRAnz. Nr.  <Nr>",
                         "dRGBl. I S <Nr>", "dRGBl. II S <Nr>",
                         "dRGBl. S <Nr>", "GBlÖ Nr. <Nr>",
                         "GVBlTirVbg.Nr. <Nr>", "JABl. Nr. <Nr>",
                         "JakschGL II, S <Nr>", "JGS Nr. <Nr>",
                         "JMVBl. Nr. <Nr>", "JosGS II., Nr. <Nr>",
                         "LGBl. Nr. <Nr>", "LGBlBgld. Nr. <Nr>",
                         "LGBlSbg. Nr. <Nr>", "LGBlStmk. Nr. <Nr>",
                         "LGuVBlStmk. Nr. <Nr>", "LGVBlTir. Nr.  <Nr>",
                         "LGBlKtn. Nr.  <Nr>", "LGBlNÖ. Nr.  <Nr>",
                         "LGBlOÖ. Nr.  <Nr>", "LGBlTir. Nr. <Nr>",
                         "LGBlVbg. Nr. <Nr>", "LGVBlSbg. Nr. <Nr>",
                         "LGVBlStmk. Nr. <Nr>", "LGVBlW. Nr. <Nr>",
                         "MBl. I S <Nr>", "MThGS Bd. 6, Nr. <Nr>",
                         "MThGS Bd. 7, Nr. <Nr>", "NSlgpolVerwD Nr. <Nr>",
                         "PGS Nr. <Nr>", "PTVBl. Nr. <Nr>", "RMinBl. S <Nr>",
                         "RVBl. Nr. <Nr>", "RVBl. S <Nr>",
                         "SlgGOeudEns14  <Nr>", "StGBl.Nr.  <Nr>",
                         "VABlNiederdonau S  <Nr>", "VABlWien Nr. <Nr>",
                         "VerBKAVVers. Nr. <Nr>", "Zl. II b Nr. <Nr>"}
        Search for legal statutes published by a specific entity. Provide a
        number instead of <Nr> to search for legal statutes of a specific
        publication. Do not provide a number in order to search for legal
        statutes in all publications of one publishing entity.
    published : {"Undefined", "EinerWoche", "ZweiWochen", "EinemMonat",
                 "DreiMonaten", "SechsMonaten", "EinemJahr"}
        Search only for legal statutes published within a certain period of
        time.

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried legal
        statutes.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(
        self,
        keywords=None,
        legal_code_name=None,
        legal_code_number=None,
        index=None,
        section_type=None,
        source_type=None,
        section_from=None,
        section_to=None,
        version_date=None,
        effective_date_from=None,
        effective_date_to=None,
        expiry_date_from=None,
        expiry_date_to=None,
        signing_date=None,
        publishing_entity=None,
        published="Undefined",
    ):

        source_types = [
            "BVG",
            "BG",
            "V",
            "K",
            "K (Geltungsbereich)",
            "Entschl. d. BPräs.",
            "Vereinbarung gem. Art. 15a B-VG",
            "Geschäftsordnung, Geschäftseinteilung etc.",
            "Vertrag - mit Angabe des Staates",
            "Vertrag - mit Angabe einer internationalen Organisation",
            "Vertrag - Multilateral",
        ]
        _input_validation("source_type", source_type, source_types)

        publishing_entity_names = [
            "BGBl. I Nr.",
            "BGBl. II Nr.",
            "BGBl. III Nr.",
            "BGBl. Nr.",
            "RGBl. Nr.",
            "StGBl. Nr.",
            "ASlg. Nr.",
            "AmtlNHW Nr.",
            "DJ S",
            "DRAnz. Nr.",
            "dRGBl. I S",
            "dRGBl. II S",
            "dRGBl. S",
            "GBlÖ Nr.",
            "GVBlTirVbg.Nr.",
            "JABl. Nr.",
            "JakschGL II, S",
            "JGS Nr.",
            "JMVBl. Nr.",
            "JosGS II., Nr.",
            "LGBl. Nr.",
            "LGBlBgld. Nr.",
            "LGBlSbg. Nr.",
            "LGBlStmk. Nr.",
            "LGuVBlStmk. Nr.",
            "LGVBlTir. Nr.",
            "LGBlKtn. Nr.",
            "LGBlNÖ. Nr.",
            "LGBlOÖ. Nr.",
            "LGBlTir. Nr.",
            "LGBlVbg. Nr.",
            "LGVBlSbg. Nr.",
            "LGVBlStmk. Nr.",
            "LGVBlW. Nr.",
            "MBl. I S",
            "MThGS Bd. 6, Nr.",
            "MThGS Bd. 7, Nr.",
            "NSlgpolVerwD Nr.",
            "PGS Nr.",
            "PTVBl. Nr.",
            "RMinBl. S",
            "RVBl. Nr.",
            "RVBl. S",
            "SlgGOeudEns14",
            "StGBl.Nr.",
            "VABlNiederdonau S",
            "VABlWien Nr.",
            "VerBKAVVers. Nr.",
            "Zl. II b Nr.",
        ]
        _input_validation(
            "publishing_entity", publishing_entity, publishing_entity_names
        )

        if publishing_entity:
            publishing_entity_name = [
                name for name in publishing_entity_names if name in publishing_entity
            ][0]
            publishing_entity_number = publishing_entity.split()[-1]
        else:
            publishing_entity_name = None
            publishing_entity_number = None

        if (
            section_type
            and not (section_from or section_to)
            or (section_from or section_to)
            and not section_type
        ):
            raise ValueError(
                "'section_type' cannot be specified without specifying 'section_from' or 'section_to' and vice versa."
            )

        _input_validation(
            "section_type",
            section_type,
            ["Alle", "Artikel", "Paragraph", "Anlage"],
        )

        if (
            effective_date_from
            or effective_date_to
            or expiry_date_from
            or expiry_date_to
        ) and version_date:
            raise ValueError(
                "'version_date' and 'effective_date_from', 'effective_date_to', 'expiry_date_from' or 'expiry_date_to' cannot be provided in the same query since the API treats them as mutually exclusive. Please provide either 'version_date' or one or more of the other parameters."
            )

        _date_input_validation("version_date", version_date)
        _date_input_validation("effective_date_from", effective_date_from)
        _date_input_validation("effective_date_to", effective_date_to)
        _date_input_validation("expiry_date_from", expiry_date_from)
        _date_input_validation("expiry_date_to", expiry_date_to)

        arguments = {
            "Suchworte": keywords,
            "Titel": legal_code_name,
            "Index": index,
            "Typ": source_type,
            "Abschnitt[Typ]": section_type,
            "Abschnitt[Von]": section_from,
            "Abschnitt[Bis]": section_to,
            "Fassung[FassungVom]": version_date,
            "Fassung[VonInkrafttretensdatum]": effective_date_from,
            "Fassung[BisInkrafttretensdatum]": effective_date_to,
            "Fassung[VonAusserkrafttretensdatum]": expiry_date_from,
            "Fassung[BisAusserkrafttretensdatum]": expiry_date_to,
            "Gesetzesnummer": legal_code_number,
            "Kundmachungsorgan": publishing_entity_name,
            "Kundmachungsorgannummer": publishing_entity_number,
            "Unterzeichnungsdatum": signing_date,
            "ImRisSeit": published,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.6/Bundesrecht", arguments
        )

        self._results = _convert_results(response)


class Landesnormen(_Base_Class):
    """
    Creates an iterable object representing a list of queried state legal norms.

    Parameters
    ----------
    TODO(PTH): provide description

    Yields
    -------
    dict
        Object can be iterated to return dicts containing queried legal
        statutes.

    Raises
    ------
    ValueError
        Is raised if the provided value is not accepted by the API.
    """

    def __init__(self):
        # TODO(PTH): validate input
        arguments = {
            "Suchworte": None,
            "Titel": None,
            "Index": None,
            "Typ": None,
            "Abschnitt": None,
            "Fassung": None,
            "Gesetzesnummer": None,
            "Kundmachungsorgan": None,
            "Kundmachungsorgannummer": None,
            "Unterzeichnungsdatum": None,
            "ImRisSeit": None,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": 1,
        }

        response = _request(
            "https://data.bka.gv.at/ris/api/v2.5/landesnormen", arguments
        )

        self._results = _convert_results(response)


def _convert_results(raw_results: list) -> list:
    # TODO(PTH): convert results
    return raw_results
