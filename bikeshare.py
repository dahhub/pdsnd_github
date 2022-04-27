import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter city name (Chicago, New York City, Washington): ')
        city = city.lower()
        if city == 'chicago':
            break
        elif city == 'new york city':
            break
        elif city == 'washington':
            break
        else:
            print("Invalid city name. Try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month (all, january, february, ... , june): ')
        month = month.lower()
        if month in months or month == 'all':
            break
        else:
            print("Invalid month. Try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day (all, monday, tuesday, ... sunday): ')
        day = day.lower()
        if day in days or day == 'all':
            break
        else:
            print("Invalid day. Try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[(df['month'] == month)]

    # filter by day of week if applicable
    if day != 'all':
        day = days.index(day.lower())

        # filter by day of week to create the new dataframe
        df = df[(df['day_of_week'] == day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Common Month: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most Common Day of Week: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('Most Common Start Hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Common Start Station: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most Common End Station  : {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station']).size().sort_values().tail(1)
    print('Most Common Combination:')
    print('  Start Station: {}'.format(combo.index[0][0]))
    print('  End Station  : {}'.format(combo.index[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Duration: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Mean Travel Duration : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type counts:')
    print(df['User Type'].value_counts().to_string() + '\n')

    if 'Gender' in df.columns:
        # Display counts of gender
        print('Gender counts:')
        print(df['Gender'].value_counts().to_string() + '\n')
    else:
        print('Gender data does not exist for this city.')

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('Earliest Birth Year {}:'.format(df['Birth Year'].min()))
        print('Most Recent Birth Year {}:'.format(df['Birth Year'].max()))
        print('Most Common Birth Year {}:'.format(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year data does not exist for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_raw_data(df):
    """Displays raw data based on user input."""

    i = 0
    while i < len(df.index):
        view = input('\nWould you like to view raw data? Enter yes or no.\n')
        if view.lower() != 'yes':
            break

        print(df.iloc[i:i+5, :-3])
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
