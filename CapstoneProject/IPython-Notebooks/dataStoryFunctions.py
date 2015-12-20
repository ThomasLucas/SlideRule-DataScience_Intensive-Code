######################################
###          DATA STORY            ###
######################################

### Imports ###
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import scipy.stats as sstats

from matplotlib import gridspec
from pyechonest import config
from pyechonest import song
from pyechonest import artist

### Global variables ###

# Colors
colors_list_tableau = create_tableau20_RGB_code()

### Functions creation ###

# Creation of a list of integers corresponding to all the years we are interested in
def create_years_list(start_year, end_year):
    years = []
    for i in range(start_year + 1, end_year + 1):
        years.append(i)
    return years

# Creation of a global dataframe from the CSV files
# This df has a new column named "year" to be able to do the filtering
def create_billboard_df_from_CSV(start_year, years):
    billboard_df = pd.read_csv('CSV_data/Billboard_Year-End_Hot_100_singles_of_' + str(start_year) + '.csv')
    billboard_df['Year'] = pd.Series(start_year, index = billboard_df.index)

    df_list = []
    for year in years:
        # Open CSV file
        billboard_current_year = pd.read_csv('CSV_data/Billboard_Year-End_Hot_100_singles_of_' + str(year) + '.csv')
        billboard_current_year['Year'] = pd.Series(year, index = billboard_current_year.index)
        df_list.append(billboard_current_year)

    # Creation of a big data frame containing all the data
    return billboard_df.append(df_list, ignore_index = True)

def create_tableau20_RGB_code():
    # These are the "Tableau 20" colors as RGB + pale gray
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229), (248,248,248)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)

    return tableau20

# graph_type is a string which can be {'Artist(s)', 'Title'}
def create_stats_lists(graph_type, years, billboard_df):
    if graph_type not in ['Artist(s)', 'Title']:
        raise NameError('Incorrect value of parameter graph_type')

    # Put the different values in lists as it is easier to plot
    min_values = []
    max_values = []
    mean_values = []
    number1_values = []
    for year in years:
        min_values.append(billboard_df[billboard_df["Year"] == year][graph_type].str.len().min())
        max_values.append(billboard_df[billboard_df["Year"] == year][graph_type].str.len().max())
        mean_values.append(billboard_df[billboard_df["Year"] == year][graph_type].str.len().mean())
        number1_values.append(billboard_df[(billboard_df["Year"] == year) & (billboard_df["Num"] == 1)][graph_type].str.len().item())

    return (min_values, max_values, mean_values, number1_values)

def create_name_length_plot(graph_type, billboard_df, years, start_year, end_year,
                     ylabel, plot_title, save_title_path, legend_loc):

    tableau20 = create_tableau20_RGB_code()
    min_values, max_values, mean_values, number1_values = create_stats_lists(graph_type, years, billboard_df)

    # Plot size
    plt.figure(figsize=(12, 9))

    # Remove the plot frame lines
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # Limit the range of the plot to only where the data is.
    plt.ylim(0, max(max_values) + 5)
    plt.xlim(start_year - 2, end_year + 2)

    # Make sure axis ticks are large enough to be easily read.
    plt.xticks(range(start_year, end_year, 10), fontsize=14)
    plt.yticks(range(0, max(max_values) + 5, 10), fontsize=14)

    # Make sure axis labels are large enough to be easily read as well.
    plt.ylabel(ylabel, fontsize=16)

    # Use matplotlib's fill_between() call to fill the area between the different lines
    plt.fill_between(years, min_values, max_values, color = tableau20[len(tableau20) - 1])

    # Plot the mean, min, max and number 1 values
    plt.plot(years, mean_values, marker = 'o', linestyle = '--', color = tableau20[0], label = "mean")
    plt.plot(years, min_values, marker = 'v', linestyle = '--', color = tableau20[2], label = "min")
    plt.plot(years, max_values, marker = '^', linestyle = '--', color = tableau20[4], label = "max")
    plt.plot(years, number1_values, '*', color = tableau20[6], label = "number1")

    # Plot title
    plt.title(plot_title, fontsize=22)

    # Legend
    plt.legend(loc=legend_loc)

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")

def create_bar_chart_featurings(x, y, xlabel, ylabel, title, save_title_path, n1_list):
    plt.figure(figsize=(12, 9))

    # Axis properties
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Axis labels
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    # Plot title
    plt.title(title, fontsize=22)

    color_list = []
    for value in x:
        if value in n1_list:
            color_list.append(colors_list_tableau[3])
        else:
            color_list.append(colors_list_tableau[0])

    # Bar chart creation
    plt.bar(x, y, color=color_list)

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")

def create_entries_count_by_artist(billboard_df, start_year, end_year):
    billboard_df = billboard_df[(billboard_df["Year"] >= start_year) & (billboard_df["Year"] < end_year)]
    billboard_artists_series = billboard_df['Artist(s)']
    featuring_mask = billboard_artists_series.str.contains("featuring")

    billboard_df_temp = pd.DataFrame.copy(billboard_df)
    billboard_df_temp.loc[:, "Lead Artist(s)"] = billboard_df['Artist(s)']

    billboard_df_temp["Lead Artist(s)"] = billboard_df_temp["Lead Artist(s)"].str.split(" featuring ").str.get(0)

    billboard_df_temp.loc[:, "Counts"] = billboard_df_temp.groupby('Lead Artist(s)')['Lead Artist(s)'].transform('count')
    billboard_df_artist_count = pd.concat([billboard_df_temp['Lead Artist(s)'],
                                           billboard_df_temp['Counts']], axis=1,
                                          keys=['Lead Artist(s)', 'Counts'])

    billboard_df_artist_count = billboard_df_artist_count.groupby('Lead Artist(s)').count().reset_index()
    return billboard_df_artist_count.sort_values(['Counts'], ascending = 0)

def create_histogram_nb_entries(counts_col, xlabel, ylabel, title, save_title_path):
    plt.figure(figsize=(12, 9))

    # Axis properties
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Axis labels
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    # Plot title
    plt.title(title, fontsize=22)

    n, bins, patches = plt.hist(counts_col, 10, normed=1, facecolor='green', alpha=0.5)

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")

def create_cumulative_counts_df(billboard_df_artist_count):
    counts_col = billboard_df_artist_count.sort_values(['Counts'], ascending = 0)["Counts"]
    cumulative_count = []
    temp = 0
    for count in counts_col:
        temp += count
        cumulative_count.append(temp)

    index = range(1, len(cumulative_count) + 1)
    data = {"Index": index, "Cumulative Count": cumulative_count}
    cumulative_count_df = pd.DataFrame(data, columns = ["Index", "Cumulative Count"])
    return cumulative_count_df

def plot_cumulative_distribution_function(cumulative_count_df, xlabel, ylabel, title, save_title_path):
    plt.figure(figsize=(12, 9))

    # Axis properties
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Axis labels
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    # Limit the range of the plot to only where the data is.
    plt.ylim(0, max(cumulative_count_df["Cumulative Count"]) + 5)
    plt.xlim(1, max(cumulative_count_df["Index"]) + 2)

    # Plot title
    plt.title(title, fontsize=22)

    # Line chart creation
    plt.plot(cumulative_count_df["Index"], cumulative_count_df["Cumulative Count"], color="#3F5D7D")

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")

def create_cumulative_counts_reverse_df(billboard_df_artist_count):
    counts_col_reverse = billboard_df_artist_count.sort_values(['Counts'], ascending = 1)["Counts"]
    cumulative_count_reverse = []
    temp = 0
    cumulative_count_reverse.append(temp)
    for count in counts_col_reverse:
        temp += count
        cumulative_count_reverse.append(temp)

    data = {"Cumulative Count Reverse": cumulative_count_reverse}
    cumulative_count_reverse_df = pd.DataFrame(data, columns = ["Cumulative Count Reverse"])
    return cumulative_count_reverse_df

def plot_lorenz_curve(cumulative_count_reverse_df, total_nb_songs, total_nb_artists, xlabel, ylabel, title, save_title_path):
    plt.figure(figsize=(12, 9))

    # Axis properties
    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    xticks = mtick.FormatStrFormatter(fmt)
    yticks = mtick.FormatStrFormatter(fmt)
    ax.xaxis.set_major_formatter(xticks)
    ax.yaxis.set_major_formatter(yticks)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Axis labels
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    # Plot title
    plt.title(title, fontsize=22)

    # x axis values normalized
    x_values_normalized = [i/ float(total_nb_artists) * 100 for i in range(0, total_nb_artists + 1)]

    # y axis values normalized
    y_values_normalized = [i/ float(total_nb_songs) * 100 for i in cumulative_count_reverse_df["Cumulative Count Reverse"]]

    # Line chart creation
    plt.plot(x_values_normalized, y_values_normalized)

    # Equity line
    plt.plot(x_values_normalized, x_values_normalized, color="#3F5D7D")

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")


def plot_multiple_lorenz_curves(billboard_df, start_year, end_year, interval, step,
                                    xlabel, ylabel, title, save_title_path, subplot):

    if not subplot:
        fig = plt.figure(figsize=(12, 15))
        nb_plots = (end_year - start_year) / step
        if nb_plots > 1:
            gs = gridspec.GridSpec(nb_plots / 2, 2)
        else:
            gs = gridspec.GridSpec(1, 1)
    else:
        fig = plt.figure(figsize=(12, 9))

    years_range = range(start_year, end_year - step, step)

    if subplot:
        last_year = years_range[-1] + step
        if last_year <= end_year:
            years_range.append(last_year)

    for year in years_range:
        if year + interval <= end_year:
            billboard_df_artist_count = create_entries_count_by_artist(billboard_df, year, year + interval)
            upper_bound = year + interval - 1
        else:
            billboard_df_artist_count = create_entries_count_by_artist(billboard_df, year, end_year)
            upper_bound = end_year
        cumulative_count_reverse_df = create_cumulative_counts_reverse_df(billboard_df_artist_count)
        total_nb_songs = cumulative_count_reverse_df.tail(1)["Cumulative Count Reverse"].tolist()[0]
        total_nb_artists = cumulative_count_reverse_df.tail(1)["Cumulative Count Reverse"].index.tolist()[0]

        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        if subplot:
            ax = plt.subplot(111)
        else:
            ax = fig.add_subplot(gs[years_range.index(year) / 2, years_range.index(year) % 2])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        xticks = mtick.FormatStrFormatter(fmt)
        yticks = mtick.FormatStrFormatter(fmt)
        ax.xaxis.set_major_formatter(xticks)
        ax.yaxis.set_major_formatter(yticks)

        # Axis labels
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)           

         # x axis values normalized
        x_values_normalized = [i/ float(total_nb_artists) * 100 for i in range(0, total_nb_artists + 1)]

        # y axis values normalized
        y_values_normalized = [i/ float(total_nb_songs) * 100 for i in cumulative_count_reverse_df["Cumulative Count Reverse"]]

        # Line chart creation
        plt.plot(x_values_normalized, y_values_normalized, label = str(year) + " - " + str(upper_bound))

        if not subplot:
            # Title
            plt.title(title + " " + str(year) + " - " + str(upper_bound), fontsize=14)

            # Equity line
            plt.plot(x_values_normalized, x_values_normalized, color="#3F5D7D")

            gs.update(wspace=0.5, hspace=0.8)

    if subplot:
        # Title
        plt.title(title + "s for each decade between " + str(start_year) + " and " + str(end_year), fontsize=14)

        # Equity line
        plt.plot(x_values_normalized, x_values_normalized, color="#3F5D7D")

        # Legend
        plt.legend(loc = 2)

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")


def calculate_gini_coefficient(billboard_df, start_year, end_year):
    billboard_df_artist_count = create_entries_count_by_artist(billboard_df, start_year, end_year)
    total_nb_artists = billboard_df_artist_count["Lead Artist(s)"].count()
    mean = billboard_df_artist_count["Counts"].mean()
    rank = range(1, total_nb_artists + 1)
    sum_product = sum(billboard_df_artist_count["Counts"] * rank)

    g = (total_nb_artists + 1) / float(total_nb_artists - 1) - (2 / (total_nb_artists * (total_nb_artists - 1) * mean)) * sum_product
    return g

def calculte_gini_per_year(billboard_df, start_year, end_year, interval):
    years = []
    gini = []
    years_range = range(start_year, end_year - interval, interval)
    last_year = years_range[-1] + interval
    if last_year <= end_year:
        years_range.append(last_year)

    for year in years_range:
        if year + interval <= end_year:
            upper_bound = year + interval
        else:
            upper_bound = end_year
        if interval > 1:
            years.append(str(year) + " - " + str(upper_bound))
        else:    
            years.append(year)
        gini.append(calculate_gini_coefficient(billboard_df, year, upper_bound))

    data = {"Year(s)": years, "Gini Coefficient": gini}
    gini_coefficient_df = pd.DataFrame(data, columns = ["Year(s)", "Gini Coefficient"])
    return gini_coefficient_df  

def plot_gini_coefficient(gini_coefficient_df, xlabel, ylabel, title, save_title_path):
    plt.figure(figsize=(12, 9))

    # Axis properties
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.yticks(fontsize=12)

    # Axis labels
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)

    # Plot title
    plt.title(title, fontsize=22)

    # x axis values can be strings, we need to map this to integer to be able to plot them
    years_index = gini_coefficient_df["Year(s)"].index.tolist()

    # Limit the range of the plot to only where the data is.
    plt.xlim(years_index[0] - 2, years_index[len(years_index) - 1] + 2)

    # Bar chart creation
    plt.bar(years_index, gini_coefficient_df["Gini Coefficient"], color = colors_list_tableau[0], align='center')
    plt.xticks(years_index, gini_coefficient_df["Year(s)"], fontsize = 12, rotation = 70)

    # Save the figure as a PNG.
    plt.savefig(save_title_path, bbox_inches="tight")






