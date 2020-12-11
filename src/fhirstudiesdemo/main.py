import json
import os

import fhirclientdemo.demo
import fhirpydemo.demo
import fhirresourcesdemo.demo

_RUN_DEMO1 = True
_RUN_DEMO2 = False
_RUN_DEMO3 = False


def get_local_path() -> str:
    return os.path.dirname(
        os.path.abspath(__file__))


def get_config() -> dict:
    config_path = os.path.join(get_local_path(), "settings.json")
    with open(config_path) as f:
        return json.load(f)


def main():
    config = get_config()

    if _RUN_DEMO1:
        print("~" * 72)
        print("### DEMO FOR 'fhirclient'")
        fhirclientdemo.demo.main(config)

    if _RUN_DEMO2:
        print("~" * 72)
        print("### DEMO FOR 'fhirpy'")
        fhirpydemo.demo.main(config)

    if _RUN_DEMO3:
        print("~" * 72)
        print("### DEMO FOR 'fhir.resources'")
        fhirresourcesdemo.demo.main(config)

    print("~" * 72)
    print("END.")


if __name__ == '__main__':
    main()
