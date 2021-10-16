from enum import Enum

class Topics(Enum):
    # Admin
    "app/uninstalled",
    "shop/update",
    "bulk_operations/finish",

    # Collections
    "collections/create",
    "collections/delete",
    "collections/update",

    # Customers
    "customers/create",
    "customers/delete",
    "customers/disable",
    "customers/enable",
    "customers/update",

    # Draft orders
    "draft_orders/create",
    "draft_orders/delete",
    "draft_orders/update",

    # Filfillment
    "fulfillment_events/create",
    "fulfillment_events/delete",
    "fulfillments/create",
    "fulfillments/update",

    # Inventory
    "inventory_items/create",
    "inventory_items/delete",
    "inventory_items/update",
    "inventory_levels/connect",
    "inventory_levels/disconnect",
    "inventory_levels/update",

    # Locations
    "locations/create",
    "locations/delete",
    "locations/update",

    # Orders
    "orders/create",
    "orders/cancelled",
    "orders/delete",
    "orders/edited",
    "orders/updated",
    "orders/fulfilled",
    "orders/paid",
    "orders/partially_fulfilled",
    "order_transactions/create",

    # Products
    "products/create",
    "products/delete",
    "products/update"

    # Product Listing
    "product_listings/add",
    "product_listings/remove",
    "product_listings/update",
    
    # Collection Listing
    "collection_listings/add",
    "collection_listings/remove",
    "collection_listings/update",
    
    # Customer Groups
    "customer_groups/create",
    "customer_groups/delete",
    "customer_groups/update",
    "refunds/create",
    "customer_payment_methods/create",
    "customer_payment_methods/revoke",
    "customer_payment_methods/update",
    "carts/create",
    "carts/update",
    "checkouts/create",
    "checkouts/delete",
    "checkouts/update",
    "disputes/create",
    "disputes/update",
    "domains/create",
    "domains/destroy",
    "domains/update",  
    "locales/create",
    "locales/update",    
    "profiles/create",
    "profiles/delete",
    "profiles/update",
    "selling_plan_groups/create",
    "selling_plan_groups/delete",
    "selling_plan_groups/update",
    "customers_marketing_consent/update",
    "subscription_billing_attempts/challenged",
    "subscription_billing_attempts/failure",
    "subscription_billing_attempts/success",
    "subscription_contracts/create",
    "subscription_contracts/update",
    "tender_transactions/create",
    "themes/create",
    "themes/delete",
    "themes/publish",
    "themes/update"
