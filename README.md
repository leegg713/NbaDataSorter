# NBA Data Sorter

A Python project for analyzing and visualizing NBA player performance. This script combines multiple CSVs of game data, computes player averages, and displays results in both terminal tables and interactive graphs.

## Features

- Combine multiple CSV data files into one
- Calculate overall and per-team stats, including averages, maximums, and minimums
- Display results as formatted tables in the terminal (using `tabulate`)
- Generate interactive bar charts with Plotly
- Filter out unwanted columns and handle zero values correctly in graphs

## Requirements

- Python 3.7 or higher
- [pandas](https://pandas.pydata.org/)
- [tabulate](https://pypi.org/project/tabulate/)
- [plotly](https://plotly.com/python/)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

1. **Combine CSV Files (Need to be done manually if using multiple different files)**

   Place your raw CSV file in your chosen directory (e.g. `Downloads`). Then run:

   ```bash
   python main.py
   ```

   The script will combine them into a new file, e.g. `sportsref_combined.csv`.

2. **Analyze Data**

   The script will load the combined CSV and allow you to analyze statistics versus specific teams. Example table and graph functions are included so you can just press run on the script:

   ```python
   print_graph(df, column_avg, team)      # Prints stats table in terminal
   plotly_graph(df, column_avg, column_max, column_min, team)  # Shows interactive bar chart
   ```

   - Set `team` to the team name you want to analyze. --- When running the script you will be asked for input
   - Adjust `column_avg`, `column_max`, and `column_min` lists to include the stats you care about. --- If you need to limit the output for some reason

3. **Configure Exclusions**

   To exclude additional columns from the graph, add their names to the `exclude_cols` list in the script at the bottom

## Customization

- **Change columns**: Update `column_avg`, `column_max`, and `column_min` in your script to match your CSV columns. (Should not be needed if getting CSVs from BasketballReference.com)
- **Exclude columns**: Add unwanted column names to the `exclude_cols` list.
- **Y-Axis Scale**: Set `dtick=5` in the Plotly layout to adjust y-axis increments. --- 5 should work but can adjust if needed

## File Structure

```
nba-data-sorter/
├── main.py
├── requirements.txt
├── sportsref_combined.csv --- This will need to be your CSV from BasketballReference.com, etc,
└── README.md
```
**Questions or suggestions?**  
Feel free to open an issue or submit a pull request with me as this is one of my first Python projects and I would love to improve it!