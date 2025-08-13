from playwright.sync_api import sync_playwright
import time

def accept_friend_requests():
    with sync_playwright() as p:
        # You can use 'chromium', 'firefox', or 'webkit'
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open a new tab
        page = context.new_page()

        # Step 1: Go to Facebook login
        page.goto("https://www.facebook.com/")

        # Step 2: Let the user log in manually
        print("🔐 Please log in to Facebook manually in the browser window...")
        input("✅ After logging in, press Enter here to continue...")

        # Step 3: Navigate to friend requests page
        page.goto("https://www.facebook.com/friends/requests/")

        # Wait for the friend request buttons to load
        page.wait_for_timeout(5000)  # wait 5 seconds

        # Step 4: Click all visible "Confirm" buttons
        confirm_buttons = page.locator('text=Confirm')
        count = confirm_buttons.count()

        print(f"🧾 Found {count} friend request(s). Accepting...")

        for i in range(count):
            try:
                confirm_buttons.nth(i).click()
                print(f"✅ Accepted request #{i + 1}")
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ Could not accept request #{i + 1}: {e}")

        print("🎉 Done accepting friend requests!")
        time.sleep(3)

        browser.close()

# Run the function
accept_friend_requests()
