from api import WeatherLocation
import json
import textwrap


def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split("\n")
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'┌{"─" * (width + indent * 2)}┐\n'  # upper_border
    if title:
        box += f"│{space}{title:<{width}}{space}│\n"  # title
        box += f'│{space}{"-" * len(title):<{width}}{space}│\n'  # underscore
    box += "".join([f"│{space}{line:<{width}}{space}│\n" for line in lines])
    box += f'└{"─" * (width + indent * 2)}┘'  # lower_border
    print(box)


def main():
    address = input("Enter address for forecast...\n")
    wl = WeatherLocation(address=address)
    wl.get_coordinates()
    wl.get_forecast_url()
    wl.get_forecast()

    forecasts = [x for x in wl.forecast_data["properties"]["periods"]]

    wrapper = textwrap.TextWrapper(width=50) 

    for forecast in forecasts:
        number = forecast["number"]
        name = forecast["name"]
        temperature = forecast["temperature"]
        short_forecast = forecast["shortForecast"]
        detailed_forecast = wrapper.fill(text=forecast["detailedForecast"])

        str_to_log = (
            "number: "
            + str(number)
            + "\n"
            + "name: "
            + str(name)
            + "\n"
            + "temperature: "
            + str(temperature)
            + "\n"
            + "short_forecast: "
            + str(short_forecast)
            + "\n"
            + "detailed_forecast: "
            + str(detailed_forecast)
        )
        print_msg_box(str_to_log)


if __name__ == "__main__":
    main()
