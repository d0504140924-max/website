from website.client_side import manager_requests as manager
from website.client_side import money_requests as money
from website.client_side import inv_requests as inv
import sys

SECTIONS = [
    ("Inventory", [
        ("Show inventory", inv.req_show_all),
        ("Show one category", inv.req_show_one_category),
        ("Item details", inv.req_item_details),
        ("Add item", inv.req_add_item),
        ("Remove item", inv.req_remove_item),
        ("Item amount", inv.req_get_amount),
    ]),
    ("Manager", [
        ("Purchase item", manager.req_purchase_item),
        ("Change price", manager.req_change_price),
        ("Money status", manager.req_money_status),
    ]),
    ("Money", [
        ("Show money status", money.req_show_money_status),
        ("Deposit money", money.req_deposit_money),
        ("Withdraw money", money.req_withdraw_money),
        ("Movements record", money.req_movements_record),
    ]),
]

def handle_response(resp):
    # prefer the existing pretty printers from the modules when available
    if resp is None:
        return
    try:
        data = resp.json()
        import json
        print("status:", resp.status_code)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except Exception:
        print("status:", resp.status_code)
        print(resp.text)

def main():
    while True:
        print("\n=== Main Menu ===")
        for i, (section_name, _) in enumerate(SECTIONS, start=1):
            print(f"{i}. {section_name}")
        print("0. Exit")
        choice = input("Choose section: ").strip()
        if choice == "0":
            print("bye")
            sys.exit(0)
        try:
            sec_idx = int(choice) - 1
            section_name, items = SECTIONS[sec_idx]
        except Exception:
            print("Invalid choice")
            continue

        # section submenu
        while True:
            print(f"\n-- {section_name} --")
            for i, (title, _) in enumerate(items, start=1):
                print(f"{i}. {title}")
            print("0. Back")
            sub = input("Choose action: ").strip()
            if sub == "0":
                break
            try:
                fn = items[int(sub) - 1][1]
            except Exception:
                print("Invalid choice")
                continue
            resp = fn()
            handle_response(resp)

if __name__ == "__main__":
    main()
