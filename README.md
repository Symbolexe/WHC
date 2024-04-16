# Website Health Checker

Website Health Checker ( WHC ) is a Python tool for monitoring the availability of websites. It allows users to specify a list of websites to monitor and checks their status periodically. The tool supports Telegram notifications for website status changes.

## Features

- Monitor the availability of multiple websites simultaneously.
- Flexible scheduling options for checking websites.
- Telegram integration for receiving notifications.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/WHC.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WHC
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python WHC.py
    ```

2. Follow the prompts to configure the tool:
   - Choose whether to use Telegram for notifications.
   - Specify the list of websites to monitor.
   - Select the monitoring interval.

3. Once configured, the tool will start monitoring the specified websites according to the chosen interval.

## Configuration

- **Telegram Notifications**: Enable or disable Telegram notifications by providing your bot token and chat ID when prompted.
- **Website List**: Enter the list of websites to monitor manually or provide a file containing the URLs.
- **Monitoring Interval**: Choose the frequency at which the tool checks the websites (hourly, daily, custom, or none).

## Example

Here's an example usage scenario:

1. User chooses to enable Telegram notifications and enters their bot token and chat ID.
2. User provides a list of websites to monitor.
3. User selects a monitoring interval of 10 minutes.
4. The tool starts monitoring the specified websites and sends notifications via Telegram if any website status changes.

## Contributing

Contributions are welcome! If you have any suggestions or encounter any issues, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
