# Course Recommendation System
# Made by: [Kalal Sohana]
# Internship Task - Codsoft


# i will use this list to store all the ratings user gives
all_ratings = []


# ------------------------------------------------
# storing all courses category wise
# each course has a name, platform, level, base rating, and empty user ratings list
# ------------------------------------------------

ai_courses = [
    ["AI For Everyone by Andrew Ng", "Coursera", "Beginner", 4.8, []],
    ["Introduction to Artificial Intelligence", "Udemy", "Beginner", 4.5, []],
    ["Machine Learning Crash Course", "Google", "Beginner", 4.7, []],
    ["Elements of AI", "University of Helsinki", "Beginner", 4.6, []],
    ["AI Basics with Python", "edX", "Beginner", 4.4, []]
]

web_courses = [
    ["The Web Developer Bootcamp", "Udemy", "Beginner", 4.9, []],
    ["Responsive Web Design", "freeCodeCamp", "Beginner", 4.7, []],
    ["HTML and CSS for Beginners", "Coursera", "Beginner", 4.5, []],
    ["JavaScript Basics", "Udacity", "Beginner", 4.6, []],
    ["Full Stack Web Development", "edX", "Beginner", 4.8, []]
]

ds_courses = [
    ["Python for Data Science", "Coursera", "Beginner", 4.8, []],
    ["Data Science with Python", "Udemy", "Beginner", 4.6, []],
    ["Introduction to Data Science", "IBM", "Beginner", 4.7, []],
    ["Data Analysis with Pandas", "Kaggle", "Beginner", 4.5, []],
    ["Statistics for Data Science", "edX", "Beginner", 4.4, []]
]

cyber_courses = [
    ["Introduction to Cybersecurity", "Cisco", "Beginner", 4.7, []],
    ["Cybersecurity Fundamentals", "Coursera", "Beginner", 4.6, []],
    ["Ethical Hacking for Beginners", "Udemy", "Beginner", 4.8, []],
    ["Network Security Basics", "edX", "Beginner", 4.5, []],
    ["Google Cybersecurity Certificate", "Google", "Beginner", 4.9, []]
]

# index positions for each value inside a course list
# i used numbers so i dont have to type the key name every time
NAME = 0
PLATFORM = 1
LEVEL = 2
BASE_RATING = 3
USER_RATINGS = 4


# this function shows the welcome message
def show_welcome():
    print("=" * 50)
    print("  WELCOME TO COURSE RECOMMENDATION SYSTEM  ")
    print("=" * 50)
    print("  Find the best beginner courses for you!  ")
    print("  Your ratings help improve the system!    ")
    print("=" * 50)


# this function shows the 4 category options
def show_categories():
    print("\n------ COURSE CATEGORIES ------")
    print("1. Artificial Intelligence")
    print("2. Web Development")
    print("3. Data Science")
    print("4. Cybersecurity")
    print("--------------------------------")


# this function asks user to pick a category
# i used a while loop so it keeps asking if they type something wrong
def get_user_category():
    while True:
        user_input = input("\nEnter category number (1-4): ")

        # checking if the input is a number first
        if user_input.isdigit() == False:
            print("Please enter a number, not text!")
            continue

        choice = int(user_input)

        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        elif choice == 4:
            return 4
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4 only.")


# this function returns the correct course list based on category number
def get_course_list(category_number):
    if category_number == 1:
        return ai_courses
    elif category_number == 2:
        return web_courses
    elif category_number == 3:
        return ds_courses
    else:
        return cyber_courses


# this function returns the category name from number
def get_category_name(category_number):
    if category_number == 1:
        return "Artificial Intelligence"
    elif category_number == 2:
        return "Web Development"
    elif category_number == 3:
        return "Data Science"
    else:
        return "Cybersecurity"


# ---------------------------------------------------
# CONTENT BASED FILTERING
# this is the main filtering logic
# it calculates a final score for each course
# the score is a mix of the original base rating and user ratings
# so if users give low ratings, the course will go down in the list
# and if users rate it high, it will come up -- this is content based filtering
# ---------------------------------------------------

def calculate_final_score(course):
    base = course[BASE_RATING]
    user_list = course[USER_RATINGS]

    # if no one rated it yet, just use the base rating as it is
    if len(user_list) == 0:
        return base

    # calculate average of all user ratings manually
    total = 0
    count = 0
    for r in user_list:
        total = total + r
        count = count + 1

    avg_user_rating = total / count

    # mix base rating (60%) with user rating average (40%)
    # i kept base rating higher so one bad rating doesnt destroy a good course
    final = (base * 0.6) + (avg_user_rating * 0.4)

    # round to 2 decimal points
    final = round(final, 2)

    return final


# this function sorts courses by score using bubble sort
# i did not use sorted() with lambda because i didnt understand it fully
# bubble sort is simple - it just compares two items and swaps them if needed
def sort_courses_by_score(course_list):

    # first calculate score for every course
    scores = []
    for i in range(len(course_list)):
        score = calculate_final_score(course_list[i])
        scores.append(score)

    # bubble sort - sort both lists together based on score
    # higher score should come first so we swap when left score is smaller
    n = len(course_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if scores[j] < scores[j + 1]:
                # swap scores
                temp_score = scores[j]
                scores[j] = scores[j + 1]
                scores[j + 1] = temp_score

                # swap courses too so they stay in sync
                temp_course = course_list[j]
                course_list[j] = course_list[j + 1]
                course_list[j + 1] = temp_course

    return course_list, scores


# this function shows all courses for selected category
def show_courses(category_number):
    category_name = get_category_name(category_number)
    course_list = get_course_list(category_number)

    print("\n--- COURSES FOR:", category_name, "---")
    print("(sorted by score - best rated courses come first)")
    print()

    # calling the filter function to sort courses by score
    sorted_list, scores = sort_courses_by_score(course_list)

    # now print each course with its details
    for i in range(len(sorted_list)):
        course = sorted_list[i]
        score = scores[i]
        num_user_ratings = len(course[USER_RATINGS])

        print(str(i + 1) + ". " + course[NAME])
        print("   Platform    : " + course[PLATFORM])
        print("   Level       : " + course[LEVEL])
        print("   Base Rating : " + str(course[BASE_RATING]) + " / 5.0")

        if num_user_ratings > 0:
            print("   User Votes  : " + str(num_user_ratings) + " person(s) rated this")
            print("   Final Score : " + str(score) + " / 5.0 * (updated by users)")
        else:
            print("   Final Score : " + str(score) + " / 5.0")

        print()

    print("-" * 40)
    return sorted_list


# this function asks user to pick a course from the list
def get_user_course(sorted_list):
    total_courses = len(sorted_list)

    while True:
        user_input = input("Enter course number (1-" + str(total_courses) + "): ")

        if user_input.isdigit() == False:
            print("Please enter a number!")
            continue

        choice = int(user_input)

        if choice >= 1 and choice <= total_courses:
            selected = sorted_list[choice - 1]
            return selected
        else:
            print("Please pick a number between 1 and " + str(total_courses))


# this function asks user to give a rating from 1 to 5
def get_user_rating(course_name):
    print("\nYou selected : " + course_name)
    print("Please give a rating for this recommendation:")
    print("1 = Poor | 2 = Fair | 3 = Good | 4 = Very Good | 5 = Excellent")

    while True:
        user_input = input("Your Rating (1-5): ")

        if user_input.isdigit() == False:
            print("Please enter a number!")
            continue

        rating = int(user_input)

        if rating >= 1 and rating <= 5:
            return rating
        else:
            print("Rating must be between 1 and 5 only!")


# this function saves the rating
# it adds the rating inside the course list (so sorting will update)
# and also adds it to the all_ratings list for the final summary
def store_rating(category_number, course, user_rating):

    # this is the important step -- adding rating inside the course
    # next time sort_courses_by_score runs, it will include this rating
    course[USER_RATINGS].append(user_rating)

    # also saving info to all_ratings for showing summary later
    category_name = get_category_name(category_number)
    saved_entry = [category_name, course[NAME], user_rating]
    all_ratings.append(saved_entry)

    print("\nYour rating has been saved!")
    print("It will affect how courses are ranked if you come back to this category.")


# this is the AI suggestion part
# it checks what category user was in and suggests a related one
# the message also changes based on what rating they gave
def ai_suggest_next(category_number, user_rating):
    print("\n--- AI SUGGESTION ---")

    category_name = get_category_name(category_number)

    # i hardcoded which category is related to which
    if category_number == 1:
        suggestion = "Data Science"
    elif category_number == 2:
        suggestion = "Cybersecurity"
    elif category_number == 3:
        suggestion = "Artificial Intelligence"
    else:
        suggestion = "Web Development"

    # show different message based on what they rated
    if user_rating >= 4:
        print("Great! You gave a high rating for " + category_name)
        print("Since you liked it, you should also try: " + suggestion)
        print("These two fields go really well together!")

    elif user_rating == 3:
        print("You gave an average rating for " + category_name)
        print("Maybe try exploring: " + suggestion)
        print("It might be a better match for your interests!")

    else:
        print("Looks like " + category_name + " was not the best fit.")
        print("How about trying: " + suggestion + " instead?")
        print("Sometimes a different starting point helps a lot!")


# this shows all ratings user gave in this session
def show_all_ratings():
    if len(all_ratings) == 0:
        print("\nYou have not rated anything yet.")
    else:
        print("\n--- YOUR RATINGS THIS SESSION ---")
        for i in range(len(all_ratings)):
            entry = all_ratings[i]
            print(str(i + 1) + ". Category : " + entry[0])
            print("   Course   : " + entry[1])
            print("   Rating   : " + str(entry[2]) + " out of 5")
            print()


# thank you message at the end
def show_thankyou(course_name, rating):
    print("\n" + "=" * 50)
    print("       THANK YOU FOR USING OUR SYSTEM!      ")
    print("=" * 50)
    print("  Course : " + course_name)
    print("  Rating : " + str(rating) + " / 5")
    print("  Your feedback improves the recommendations!")
    print("  Happy Learning!")
    print("=" * 50)


# main function - this is where everything runs from
def main():

    show_welcome()

    # keep running until user wants to stop
    while True:

        show_categories()
        category_number = get_user_category()

        sorted_courses = show_courses(category_number)

        selected_course = get_user_course(sorted_courses)

        user_rating = get_user_rating(selected_course[NAME])

        store_rating(category_number, selected_course, user_rating)

        ai_suggest_next(category_number, user_rating)

        show_thankyou(selected_course[NAME], user_rating)

        print("\nDo you want to explore another category?")
        again = input("Type 'yes' to continue or 'no' to exit: ")
        again = again.lower()

        if again != "yes":
            show_all_ratings()
            print("Thanks for using the Course Recommendation System!")
            print("Goodbye! Keep Learning!")
            break


# run the program
main()