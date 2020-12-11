from fhirclient.client import FHIRClient

_RECORDS_LIMIT = 10


def main(config: dict):
    fh = _create_client(config)
    status = _get_status(fh)


def _create_client(config: dict) -> FHIRClient:
    settings = {
        "app_id": "fhirclient_demo",
        "api_base": config["fhirApiBaseUrl"]
    }
    return FHIRClient(settings=settings)


def _get_status(fh: FHIRClient) -> bool:
    status = fh.ready
    print(f"Ready: {status}")
    if status:
        return True

    status = fh.prepare()
    print(f"Prepared: {status}")
    status = fh.ready
    print(f"Ready: {status}")
    return status
