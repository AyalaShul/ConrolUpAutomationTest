# ControlUp Automation Test

This repo contains my solution for the ControlUp Automation Home Assignment.  
Implemented in **Python**, using **Selenium** for UI tests and the `requests` library for API tests.

## Covered Scenarios

### UI Tests – [saucedemo.com](https://www.saucedemo.com)
- Verify 6 inventory items appear after login.
- Add first item to cart and confirm cart badge shows `1`.

### API Tests – [airportgap.com](https://airportgap.com)
- Confirm exactly 30 airports are returned.
- Check presence of 3 specific airports.
- Verify distance between KIX and NRT is over 400 km.
  
## Running the Tests
Tests can be executed using `pytest`:
Make sure dependencies are installed, then run:
python -m pytest
