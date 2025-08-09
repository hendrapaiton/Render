import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RENDER_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}
BASE_URL = "https://api.render.com/v1/services"


def list_service(args):
    print("Listing all services...")
    res = requests.get(BASE_URL, headers=headers)
    services = res.json()
    if not services:
        print("No services have been installed on this account yet.")
    else:
        for svc in services:
            print(f"{svc['id']} - {svc['name']} ({svc['service']['type']})")


def create_service(args):
    print(f"Creating service: {args.name} of type {args.type}")
    # Add your service creation logic here
    pass


def delete_service(args):
    print(f"Deleting service with ID: {args.id}")
    # Add your service deletion logic here
    pass


def main():
    parser = argparse.ArgumentParser(description="Render Unofficial CLI Tool")
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # List service command
    list_parser = subparsers.add_parser("list", help="List all services")
    list_parser.set_defaults(func=list_service)

    # Create service command
    create_parser = subparsers.add_parser(
        "create", help="Create a new service")
    create_parser.add_argument(
        "--name", required=True, help="Name of the service")
    create_parser.add_argument(
        "--type", required=True, help="Type of the service (e.g., web, cron)")
    create_parser.set_defaults(func=create_service)

    # Delete service command
    delete_parser = subparsers.add_parser(
        "delete", help="Delete an existing service")
    delete_parser.add_argument(
        "--id", required=True, help="ID of the service to delete")
    delete_parser.set_defaults(func=delete_service)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
