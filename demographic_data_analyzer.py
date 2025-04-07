import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    print(df.columns)

    # Number of people by race
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # Total number of people
    total_people = df.shape[0]

    # Number of people who have a Bachelors degree
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]

    # Percentage of Bachelor's degree holders 
    percentage_bachelors = (bachelors_count / total_people) * 100    

    # With and without higher education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # People earning >50K in each group
    higher_education_rich = higher_education.loc[higher_education['salary'] == '>50K']
    lower_education_rich = lower_education.loc[lower_education['salary'] == '>50K']

    # Percentage with salary >50K
    percentage_higher_education_rich = (higher_education_rich.shape[0] / higher_education.shape[0]) * 100 if higher_education.shape[0] > 0 else 0
    percentage_lower_education_rich = (lower_education_rich.shape[0] / lower_education.shape[0]) * 100 if lower_education.shape[0] > 0 else 0
    
    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]

    # Number of people earning >50K among those who work the fewest hours
    num_rich = (min_hours_workers['salary'] == '>50K').sum()

    # Total number of people who worked the minimum number of hours per week
    total_min_hour_workers = min_hours_workers.shape[0]

    # Percentage of those who earn >50K among those who worked the fewest hours
    rich_percentage = (num_rich / total_min_hour_workers) * 100 if total_min_hour_workers > 0 else 0
   
    # People earning >50K per country
    rich_people = df[df['salary'] == '>50K']
    rich_by_country = rich_people.groupby('native-country').size()

    # Percentage of rich people per country
    total_by_country = df.groupby('native-country').size()
    rich_percentage_by_country = (rich_by_country / total_by_country) * 100

    # Country with the highest percentage
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = rich_percentage_by_country.max()
    
    # People in India who earn >50K
    rich_in_india = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    # Most popular occupation in India
    top_IN_occupation = rich_in_india.groupby('occupation').size().idxmax()

    # Round the results to 1 decimal places 
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    percentage_higher_education_rich = round(percentage_higher_education_rich, 1)
    percentage_lower_education_rich = round(percentage_lower_education_rich, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {percentage_lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': percentage_higher_education_rich,
        'lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
