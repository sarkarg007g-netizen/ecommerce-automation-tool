import json
import logging

# Configure logging for operational tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ECommerceInventoryManager:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = {}

    def update_stock(self, product_id, stock_count):
        """Updates stock count for e-commerce catalog."""
        self.inventory[product_id] = stock_count
        logging.info(f"[{self.store_name}] Updated SKU {product_id} to {stock_count} units.")

    def audit_inventory(self):
        """Returns current inventory counts."""
        return json.dumps(self.inventory, indent=4)

if __name__ == "__main__":
    # Initialize operational manager for your venture
    manager = ECommerceInventoryManager(store_name="Santosh Organic Resources")
    manager.update_stock(product_id="SKU_ORG_001", stock_count=150)
    manager.update_stock(product_id="SKU_ORG_002", stock_count=75)
    
    print("Current Inventory Audit:")
    print(manager.audit_inventory())
