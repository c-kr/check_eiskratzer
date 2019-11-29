# check_eiskratzer

check_eiskratzer is a Python 3 Monitoring Plugin that predicts if you need to scrape ice off your car windows. 

It checks geo coordinates against the REST-API https://www.eiswarnung.de/rest-api/ which uses machine learning algorithms for prediction.

You need a personal API-Key. Request it at info@eiswarnung.de


## Installation

Install python requests, move check_eiskratzer.py to your monitoring libexec directory and make it executable:

```bash
pip install requests
mv check_eiskratzer.py /usr/local/nagios/libexec/
chmod 755 /usr/local/nagios/libexec/check_eiskratzer.py
```

## Usage

```bash
check_eiskratzer.py -k [API-KEY] -a [latitude] -o [longitude]
```

## Example

```bash
check_eiskratzer.py -k a124a249dce89667106b665bf3c0e9b4 -a 51.397933 -o 12.399797
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
