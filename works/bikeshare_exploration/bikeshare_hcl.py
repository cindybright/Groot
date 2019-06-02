import time
import pandas as pd
import numpy as np
""" 
As washington.csv is lack of 'Gender' and 'Birth Year' columns, we need to
add two columns of gender and birth year with zeros in 'washington.csv'first.
"""
df = pd.read_csv('washington.csv')
gender = np.zeros(300000,int)
birth_year = np.zeros(300000,int)
df['Gender'] = gender
df['Birth Year'] = birth_year
df.to_csv('washington.csv', index = False)

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
    
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Would you like to see data for Chicago or New York City or Washington? Please type the name of city.\n')
        if city.lower() in cities:
            break
   
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'febuary', 'march', 'april', 'may', 'june']
    while True:
        month = input('Which month? (all, january, febuary, march, april, may, june)\n')
        if month.lower() in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Which day? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n')
        if day.lower() in days:
            break
            

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'febuary', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:',popular_day_of_week)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:',popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_trip = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip:', popular_start_end_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender 
    print('Counts of gender:\n', df['Gender'].value_counts())

        
    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nEarlist year of birth:', df['Birth Year'].min())
    print('Most recent year of birth:', df['Birth Year'].max())
    print('Most common year of birth:', df['Birth Year'].mode()[0])
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
