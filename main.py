import argparse
from cli import create_shipment

def main():
    parser = argparse.ArgumentParser(description='Machool API CLI')
    parser.add_argument('command', choices=['create_shipment'], help='Command to execute')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-keyid', '--key-id', required=True, help='API key ID')
    parser.add_argument('-apikey', '--api-key', required=True, help='API key')

    args = parser.parse_args()

    if args.command == 'create_shipment':
        create_shipment(args.file, args.key_id, args.api_key)

if __name__ == '__main__':
    main()