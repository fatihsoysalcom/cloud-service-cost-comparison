import json

# This script demonstrates a simplified comparison of cloud service costs, akin to understanding the fundamental pricing models of Azure and AWS.
# It's a conceptual example, not a real-time API integration.

def calculate_azure_cost(service_type, usage_hours, price_per_hour):
    """Calculates hypothetical Azure cost."""
    return usage_hours * price_per_hour

def calculate_aws_cost(service_type, usage_hours, price_per_hour):
    """Calculates hypothetical AWS cost."""
    return usage_hours * price_per_hour

def compare_cloud_costs(services):
    """Compares costs for a list of services across hypothetical Azure and AWS pricing."""
    print("\n--- Cloud Service Cost Comparison ---")
    print("\nThis is a simplified demonstration. Real-world costs depend on many factors.")

    for service in services:
        service_name = service['name']
        azure_price = service['azure_price_per_hour']
        aws_price = service['aws_price_per_hour']
        usage = service['usage_hours']

        # Calculate hypothetical costs for each service
        hypothetical_azure_total = calculate_azure_cost(service_name, usage, azure_price)
        hypothetical_aws_total = calculate_aws_cost(service_name, usage, aws_price)

        print(f"\nService: {service_name}")
        print(f"  Usage: {usage} hours")
        print(f"  Hypothetical Azure Cost: ${hypothetical_azure_total:.2f}")
        print(f"  Hypothetical AWS Cost: ${hypothetical_aws_total:.2f}")

        # Basic comparison
        if hypothetical_azure_total < hypothetical_aws_total:
            print("  Azure is hypothetically cheaper for this service.")
        elif hypothetical_aws_total < hypothetical_azure_total:
            print("  AWS is hypothetically cheaper for this service.")
        else:
            print("  Hypothetical costs are the same.")

if __name__ == "__main__":
    # Sample service data with hypothetical pricing and usage
    # This data represents the *kind* of information you'd analyze when choosing between cloud providers.
    cloud_services_to_compare = [
        {
            "name": "Virtual Machine (Basic)",
            "azure_price_per_hour": 0.05,
            "aws_price_per_hour": 0.06,
            "usage_hours": 100
        },
        {
            "name": "Object Storage (GB)",
            "azure_price_per_hour": 0.0001,
            "aws_price_per_hour": 0.00012,
            "usage_hours": 10000
        },
        {
            "name": "Database (Small Instance)",
            "azure_price_per_hour": 0.08,
            "aws_price_per_hour": 0.075,
            "usage_hours": 200
        }
    ]

    compare_cloud_costs(cloud_services_to_compare)
