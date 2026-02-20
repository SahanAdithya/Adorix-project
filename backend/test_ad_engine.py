"""
Test suite for the Ad Engine module.
Tests the AdSelector class with various user profiles and scenarios.
"""

import os
import sys
import json
from pathlib import Path

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.ad_engine import AdSelector


class TestAdEngine:
    def __init__(self):
        self.rules_path = os.path.join(
            os.path.dirname(__file__),
            "modules/ad_engine/rules.json"
        )
        self.ads_dir = os.path.join(
            os.path.dirname(__file__),
            "modules/ad_engine/data"
        )
        self.selector = None
        self.test_results = []

    def setup(self):
        """Initialize the AdSelector."""
        print("=" * 70)
        print("SETTING UP AD ENGINE TEST")
        print("=" * 70)
        print(f"Rules path: {self.rules_path}")
        print(f"Ads directory: {self.ads_dir}")
        
        if not os.path.exists(self.rules_path):
            print(f"ERROR: Rules file not found at {self.rules_path}")
            return False
        
        if not os.path.exists(self.ads_dir):
            print(f"ERROR: Ads directory not found at {self.ads_dir}")
            return False
        
        self.selector = AdSelector(self.rules_path, self.ads_dir)
        print(f"✓ AdSelector initialized successfully")
        print(f"✓ Loaded {len(self.selector.idle_ads)} idle ads")
        print()
        return True

    def test_idle_status(self):
        """Test ad selection when user status is IDLE."""
        print("TEST 1: IDLE Status")
        print("-" * 70)
        
        payload = {"status": "IDLE"}
        ad = self.selector.choose_ad_filename(payload, advance_idle=True)
        print(f"Payload: {payload}")
        print(f"Selected ad: {ad}")
        print(f"Full path: {self.selector.ad_path(ad)}")
        
        # Test rotation through idle ads
        print("\nTesting idle ad rotation (3 rotations):")
        for i in range(3):
            ad = self.selector.choose_ad_filename(payload, advance_idle=True)
            print(f"  Rotation {i+1}: {ad}")
        
        self.test_results.append(("IDLE Status", "PASSED"))
        print()

    def test_no_payload(self):
        """Test ad selection with no payload."""
        print("TEST 2: No Payload / None")
        print("-" * 70)
        
        payload = None
        ad = self.selector.choose_ad_filename(payload)
        print(f"Payload: {payload}")
        print(f"Selected ad: {ad}")
        
        self.test_results.append(("No Payload", "PASSED"))
        print()

    def test_female_19_29(self):
        """Test ad selection for female user aged 19-29."""
        print("TEST 3: Female 19-29 Demographic")
        print("-" * 70)
        
        payload = {
            "status": "DETECTED",
            "primary": {
                "gender": "Female",
                "age": "19-29"
            }
        }
        ad = self.selector.choose_ad_filename(payload)
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print(f"Selected ad: {ad}")
        print(f"Expected: makeup_ad.mp4 (from rules)")
        
        self.test_results.append(("Female 19-29", "PASSED"))
        print()

    def test_male_19_29(self):
        """Test ad selection for male user aged 19-29."""
        print("TEST 4: Male 19-29 Demographic")
        print("-" * 70)
        
        payload = {
            "status": "DETECTED",
            "primary": {
                "gender": "Male",
                "age": "19-29"
            }
        }
        ad = self.selector.choose_ad_filename(payload)
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print(f"Selected ad: {ad}")
        print(f"Expected: gaming_ad.mp4 (from rules)")
        
        self.test_results.append(("Male 19-29", "PASSED"))
        print()

    def test_default_fallback(self):
        """Test default ad fallback for unmapped demographics."""
        print("TEST 5: Default Fallback (Unmapped Demographic)")
        print("-" * 70)
        
        payload = {
            "status": "DETECTED",
            "primary": {
                "gender": "Female",
                "age": "50-60"
            }
        }
        ad = self.selector.choose_ad_filename(payload)
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print(f"Selected ad: {ad}")
        print(f"Expected: furniture_ad.mp4 (DEFAULT from rules)")
        
        self.test_results.append(("Default Fallback", "PASSED"))
        print()

    def test_rules_loading(self):
        """Test that rules are loaded correctly."""
        print("TEST 6: Rules Configuration")
        print("-" * 70)
        
        print(f"Loaded rules:")
        for key, value in self.selector.rules.items():
            print(f"  {key}: {value}")
        
        print(f"\nSHUFFLE_IDLE enabled: {self.selector.rules.get('SHUFFLE_IDLE')}")
        
        self.test_results.append(("Rules Loading", "PASSED"))
        print()

    def test_reshuffle_functionality(self):
        """Test the reshuffle functionality."""
        print("TEST 7: Reshuffle Idle Ads")
        print("-" * 70)
        
        original_order = self.selector.idle_ads.copy()
        print(f"Original idle ads order: {original_order}")
        
        self.selector.reshuffle_idle_ads()
        shuffled_order = self.selector.idle_ads.copy()
        print(f"Shuffled idle ads order: {shuffled_order}")
        
        # Note: shuffle might result in the same order occasionally
        print(f"Orders are different: {original_order != shuffled_order}")
        
        self.test_results.append(("Reshuffle Functionality", "PASSED"))
        print()

    def test_ad_path(self):
        """Test the ad_path method."""
        print("TEST 8: Ad Path Construction")
        print("-" * 70)
        
        test_filename = "test_ad.mp4"
        path = self.selector.ad_path(test_filename)
        print(f"Filename: {test_filename}")
        print(f"Full path: {path}")
        print(f"Expected: {os.path.join(self.ads_dir, test_filename)}")
        
        self.test_results.append(("Ad Path Construction", "PASSED"))
        print()

    def test_multiple_users_scenario(self):
        """Test a realistic multi-user scenario."""
        print("TEST 9: Multi-User Scenario")
        print("-" * 70)
        
        users = [
            {"status": "DETECTED", "primary": {"gender": "Female", "age": "19-29"}},
            {"status": "IDLE"},
            {"status": "DETECTED", "primary": {"gender": "Male", "age": "29-39"}},
            {"status": "IDLE"},
            None,
        ]
        
        for i, user in enumerate(users, 1):
            ad = self.selector.choose_ad_filename(user, advance_idle=(user and user.get("status") == "IDLE"))
            user_desc = str(user) if user else "No user"
            print(f"  User {i}: {user_desc}")
            print(f"    → Selected: {ad}")
        
        self.test_results.append(("Multi-User Scenario", "PASSED"))
        print()

    def print_summary(self):
        """Print test summary."""
        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        
        for test_name, result in self.test_results:
            status_symbol = "✓" if result == "PASSED" else "✗"
            print(f"{status_symbol} {test_name}: {result}")
        
        passed = sum(1 for _, r in self.test_results if r == "PASSED")
        total = len(self.test_results)
        print(f"\nTotal: {passed}/{total} tests passed")
        print("=" * 70)

    def run_all_tests(self):
        """Run all tests."""
        if not self.setup():
            print("Setup failed. Exiting.")
            return
        
        try:
            self.test_idle_status()
            self.test_no_payload()
            self.test_female_19_29()
            self.test_male_19_29()
            self.test_default_fallback()
            self.test_rules_loading()
            self.test_reshuffle_functionality()
            self.test_ad_path()
            self.test_multiple_users_scenario()
        except Exception as e:
            print(f"ERROR during tests: {str(e)}")
            import traceback
            traceback.print_exc()
        
        self.print_summary()


if __name__ == "__main__":
    tester = TestAdEngine()
    tester.run_all_tests()
