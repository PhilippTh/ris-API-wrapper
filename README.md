# ris API wrapper in Python

![License](https://img.shields.io/github/license/PhilippTh/ris-API-wrapper)
![Contributions](https://img.shields.io/badge/contributions-welcome-blue)
[![Twitter Follow](https://img.shields.io/twitter/follow/philippthumfart.svg?style=social)](https://twitter.com/philippthumfart)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?hosted_button_id=H2M2D3JC4KXRG)

RIS is a plattform by the Austrian government giving open access to legal codes and court rulings. This project creates a wrapper for their API in Python. The wrapper is currently being developed for version 2.5 of the API but will be updated to version 2.6 in the future. You can get more information about the API at [data.gv.at](https://www.data.gv.at/suche/?searchterm=%22RIS+Daten%22&searchin=data)

The benefits of this wrapper as opposed to using the API itself are:
- Argument validation to make sure the API returns the results you expect
- Proper error handling to deal with known issues of the api
- Return data in a sensible structure
- Sort your results as you wish

## Example queries

The following examples can help you get started:

```
# Print all Rechtssatz numbers for a specific decision.
from risApiWrapper.Judikatur import Justiz

wrapper_instance = Justiz(
    case_number="5Ob234/20b",
    show_entscheidungstexte=False)

for rechtssatz in wrapper_instance:
    print(rechtssatz["rechtssatz_number"])
```

```
# Print all case number of decisions the High Constitutional Court has decided in a specific period.
from risApiWrapper.Judikatur import Vfgh

wrapper_instance = Vfgh(
    decision_date_from = "2021-01-01",
    decision_date_to = "2021-12-31",
    show_rechtssaetze = False)

for decision in wrapper_instance:
    print(decision["case_number"])
```


## Structure

TODO

## Contribution

Contributions are welcome! If this wrapper helped you, please also consider [donating](https://www.paypal.com/donate?hosted_button_id=H2M2D3JC4KXRG) to keep this project running. Donations will be split among all contributors.