# Meraki Camera Retention Automation

This project automates the collection of video retention information from Meraki cameras across multiple organizations, using the Meraki API and web automation with Selenium. The goal is to facilitate audits and management of video retention policies, centralizing the data in a CSV file.

## Use Case

Automates the login process, camera inventory collection, and extraction of retention days configured on each Meraki MV device. Ideal for IT teams that need to monitor and document video retention policies in corporate environments.

## Technology Stack

- Python 3.8+
- Selenium WebDriver
- Meraki Python SDK
- python-dotenv

## Status

Beta – Functional, but may require adjustments for different authentication flows or changes in the Meraki dashboard.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lucasmbarboza/rpa-rentention-meraki
   cd rpa-rentention-meraki
   ```

2. Install dependencies using the requirements file:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have Google Chrome installed and a compatible ChromeDriver in your PATH.

## Configuration

Create a `.env` file in the project root with the following variables:

```env
MERAKI_API_KEY=YOUR_API_KEY
MERAKI_USERNAME=your@email.com
MERAKI_PASSWORD=your_password
```

## Usage

Run the main script:

```bash
python rpa.py
```

During execution, follow the terminal instructions for authentication (including 2FA, if necessary).

Results will be saved in `camera_retention.csv` with the columns: organization, camera name, serial, and retention days.

## Known Issues

- The login flow may change as the Meraki dashboard is updated.
- The script requires manual intervention for 2FA authentication.

## Getting help

Open an issue in this repository for questions or problems.

## Getting involved

Contributions are welcome! See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for details.

## License

This code is licensed under the MIT License. See [LICENSE.txt](./LICENSE.txt) for details.
