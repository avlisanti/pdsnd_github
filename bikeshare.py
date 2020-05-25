import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington','all']
    city = input('\nWhich city would you like to see the data for? Please select Chicago, New York City or Washington.\n').lower()

    while True:
        if city in cities:
            print('\nLooks like you would like to explore the data from {}.'.format(city))
            break
        else:
            print('\nOops! This city is not in our list, please check if you made a typo!\n')
            city = input('\nWhich city would you like to see the data for? Please select Chicago, New York City or Washington.').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','bebruary','march','april','may','june']
    month = input("\nWhich month would you like to explore? Please select January, February, March, April, May, June or enter 'all' to view all months.\n").lower()

    while True:
        if month in months:
            print('\nLooks like you would like to explore the data from {}.'.format(month))
            break
        else:
            print('\nOops! Looks like the month you selected is invalid or our of range. Please try again and check for typos.\n')
            month = input("\nWhich month would you like to explore? Please select January, February, March, April, May, June or enter 'all' to view all months.\n").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("\nPlease select a day of the week you would like to see the data for, or simply type 'all' to view the data for all days of the week.\n").lower()
    while True:
        if day in days:
            print('\nLooks like you would like to explore the data from {}.\n'.format(day))
            break
        else:
            print('\nOops! Looks like the day name you selected is invalid. Please try again and check for typos.\n')
            day = input("\nPlease select a day of the week you would like to see the data for, or simply type 'all' to view the data for all days of the week.\n").lower()


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
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month_index = df['month'].mode()[0]
    most_common_month = months[most_common_month_index - 1]
    print('\n The most common month is: {}'.format(most_common_month).title())

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\n The most common day of the week is: {}'.format(most_common_day).title())

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\n The most common hour to travel is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start = df['Start Station'].mode()[0]
    print('\nThe most popular start station: {}'.format(most_popular_start))

    # TO DO: display most commonly used end station
    most_popular_end = df['End Station'].mode()[0]
    print('\nThe most popular end station: {}'.format(most_popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    # Creating a combination of start and end stations
    route = ('from ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('\nThe most popular route: {}'.format(route))
    #print(df['route'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60 / 60    # This is to output the result in hours
    print("Total trip duration: {} (hours)".format(total_travel_time))
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean() / 60    # This is to output the result in minutes
    print("Average trip duration: {} (minutes)".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if 'Gender' in df.columns:
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print(user_types)
        # TO DO: Display counts of gender
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        # Display this if gender data is no available for a particular city
        print('Gender data is not available')

    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        # Find the earliest YOB
        oldest_yob = int(df['Birth Year'].min())
        print('\nThe oldest customer was born is {}'.format(oldest_yob))
        # Find the most recent YOB
        youngest_yob = int(df['Birth Year'].max())
        print('\nThe youngest customer was born is {}'.format(youngest_yob))
        # Find the most common YOB
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('\nThe most common year of birth is {}'.format(most_common_yob))
    else:
        # Display this if year of birth data is not available for a particular city
        print('Birth year data is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # Prompting user to select if they want to see 5 rows of raw data at a time
        print_raw = input('\nWhould you like to see raw data? Enter yes or no.\n').lower()
        if print_raw in ('yes','y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i+=5
                more_raw = input('\nWould you like to see more raw data? Enter yes or no.\n').lower()
                if more_raw not in ('yes','y'):
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
