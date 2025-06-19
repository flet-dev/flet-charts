# flet-charts

[![pypi](https://img.shields.io/pypi/v/flet-charts.svg)](https://pypi.python.org/pypi/flet-charts)
[![downloads](https://static.pepy.tech/badge/flet-charts/month)](https://pepy.tech/project/flet-charts)
[![license](https://img.shields.io/github/license/flet-dev/flet-charts.svg)](https://github.com/flet-dev/flet-charts/blob/main/LICENSE)

A Flet extension for creating interactive charts and graphs.

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
pip install flet-charts
```

    You will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"

```bash
poetry add flet-charts
```

???+ note annotate
If you plan to use the [`MatplotlibChart`](matplotlib_chart) and/or [`PlotlyChart`](plotly_chart) controls,
you need to install [`matplotlib`](https://matplotlib.org/) and/or [`plotly`](https://plotly.com/python/) packages
respectively as well.

    This can easily be done when installing `flet-charts` by specifying an extra:
    
    - `[matplotlib]` which installs _only_ `matplotlib`
    - `[plotly]` which installs _only_ `plotly`
    - `[all]` which installs _both_ `matplotlib` and `plotly`
    
    === "uv"
        ```bash
        uv add "flet-charts[all]"  # (1)!
        ```
    
    === "pip"
        ```bash
        pip install flet-charts[all]  # (2)!
        ```
    
    === "poetry"
        ```bash
        poetry add "flet-charts[all]" # (3)!
        ```
    
    **You can also install them on their own:**
    
    === "uv"
        ```bash
        uv add matplotlib 
        uv add plotly
        ```
    
    === "pip"
        ```bash
        pip install matplotlib
        pip install plotly
        ```
    
    === "poetry"
        ```bash
        poetry add matplotlib
        poetry add plotly
        ```

1. Replace `all` with `matplotlib` or `plotly` to install only one of them.
2. Replace `all` with `matplotlib` or `plotly` to install only one of them.
3. Replace `all` with `matplotlib` or `plotly` to install only one of them.

## Examples

You can find examples in the respective documentation pages for each chart type:

- [`BarChart`](bar_chart.md#examples)
- [`LineChart`](line_chart.md#examples)
- [`MatplotlibChart`](matplotlib_chart.md#examples)
- [`PieChart`](pie_chart.md#examples)
- [`PlotlyChart`](plotly_chart.md#examples)

<!--- [`ScatterChart`](scatter_chart#examples) -->

