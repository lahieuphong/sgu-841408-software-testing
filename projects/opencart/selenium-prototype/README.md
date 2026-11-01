# OpenCart public demo browser examples

Early Selenium examples for the public OpenCart demo. Run these scripts explicitly from this directory after installing Selenium and WebDriver Manager. They are demonstrations rather than a collected pytest suite.

| File | Purpose |
| --- | --- |
| `open_demo_with_profile.py` | Open with a Chrome profile by default, or `--browser firefox` |
| `browser_profiles.py` | Shared browser/profile creation helper |
| `chrome_profile_setup.py` | Create and reuse a Chrome profile |
| `firefox_profile_setup.py` | Create and reuse a Firefox profile |
| `firefox_headless_demo.py` | Headless Firefox example |
| `firefox_user_agent.py` | Firefox-specific user-agent helper |
| `firefox_user_agent_demo.py` | Separate Firefox example with additional preferences |
| `login_demo.py` | Login using a saved profile and environment-supplied credentials |
| `demo_workflow.py` | Login, form submission, navigation and logout demonstration |

The former Chrome/Firefox `main` scripts are combined through the `--browser` argument. `login_demo.py` and `demo_workflow.py` require `OPENCART_DEMO_EMAIL` and `OPENCART_DEMO_PASSWORD`; see the [environment template](../../../.env.example). Saved browser profiles remain local and are excluded from Git.

[OpenCart project](../README.md)
