import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')
    def r(n): return round(n, 1)
    def p(a, t): return r(a * 100 / t)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    is_male = df['sex'] == 'Male'
    average_age_men = r(df.loc[is_male, 'age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    is_bachelors = df.loc[df['education'] == 'Bachelors']
    percentage_bachelors = p(len(is_bachelors), len(df))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education_titles = ['Bachelors', 'Doctorate', 'Masters']
    higher_education_and_rich = df.loc[(df['education'].isin(
        higher_education_titles)) & (df['salary'] == '>50K')]
    lower_education_and_rich = df.loc[(~df['education'].isin(
        higher_education_titles)) & (df['salary'] == '>50K')]
    higher_education = df.loc[(df['education'].isin(higher_education_titles))]
    lower_education = df.loc[(~df['education'].isin(higher_education_titles))]

    # percentage with salary >50K
    # print(len(lower_education), len(df.loc[df['salary'] == '>50K']))
    higher_education_rich = p(
        len(higher_education_and_rich), len(higher_education))
    lower_education_rich = p(
        len(lower_education_and_rich), len(lower_education))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours])
    rich_and_min_hours = df.loc[(
        df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    rich_percentage = p(len(rich_and_min_hours), num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].value_counts()
    highest_earning_country = None
    highest_earning_country_percentage = 0
    for ind, val in countries.items():
        lives_in_ind_and_has_over_50K = df.loc[(
            df['native-country'] == ind) & (df['salary'] == '>50K')]
        percentage = p(len(lives_in_ind_and_has_over_50K), val)
        if (percentage > highest_earning_country_percentage):
            highest_earning_country = ind
            highest_earning_country_percentage = percentage

    # Identify the most popular occupation for those who earn >50K in India.
    has_over_50K_and_in_india = df.loc[(df['salary'] == '>50K') & (
        df['native-country'] == 'India'), 'occupation']
    top_IN_occupation = has_over_50K_and_in_india.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()
