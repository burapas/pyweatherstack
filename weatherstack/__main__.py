import argparse
import logging

def main():
    parser = argparse.ArgumentParser(
        description="WeatherStack API Client"
    )
    parser.add_argument("--current", nargs=1,
        help="retreive current weather from location")
    
    parser.add_argument("--historical")
    parser.add_argument("--forecast")

    args = parser.parse_args()

if __name__ == "__main__":
    main()