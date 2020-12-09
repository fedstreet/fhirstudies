import fhirclientdemo.demo
import fhirpydemo.demo
import fhirresourcesdemo.demo


def main():
    print("~" * 72)
    fhirclientdemo.demo.main()
    print("~" * 72)
    fhirpydemo.demo.main()
    print("~" * 72)
    fhirresourcesdemo.demo.main()
    print("~" * 72)
    print("END.")


if __name__ == '__main__':
    main()
