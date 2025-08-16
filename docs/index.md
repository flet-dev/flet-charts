# flet-charts

[![pypi](https://img.shields.io/pypi/v/flet-charts.svg)](https://pypi.python.org/pypi/flet-charts)
[![downloads](https://static.pepy.tech/badge/flet-charts/month)](https://pepy.tech/project/flet-charts)
[![license](https://img.shields.io/github/license/flet-dev/flet-charts.svg)](https://github.com/flet-dev/flet-charts/blob/main/LICENSE)

A [Flet](https://flet.dev) extension for creating interactive charts and graphs.

It is based on the [fl_chart](https://pub.dev/packages/fl_chart) Flutter package.

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ✅     |
| Linux    |     ✅     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Usage

### Installation

To install the `flet-charts` package and add it to your project dependencies:

=== "uv"
    ```bash
    uv add flet-charts
    ```

=== "pip"
    ```bash
    pip install flet-charts  # (1)!
    ```

    1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"
    ```bash
    poetry add flet-charts
    ```

## Examples

You can find examples in the respective documentation pages for each chart type:

- [`BarChart`](bar_chart.md#examples)
- [`LineChart`](line_chart.md#examples)
- [`MatplotlibChart`](matplotlib_chart.md#examples)
- [`PieChart`](pie_chart.md#examples)
- [`PlotlyChart`](plotly_chart.md#examples)
- [`ScatterChart`](scatter_chart.md#examples)
