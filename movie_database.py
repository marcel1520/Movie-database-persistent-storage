import random
import statistics
import json


def header(header_line):
    return header_line


def menu(choices_menu):
    return choices_menu


def get_movies_from_film_database(film_database):
    with open(film_database, "r") as data_file:
        database_content = json.load(data_file)
        return database_content


def option_1_display_dictionary():
    with open("film_database.json", "r") as file:
        films = json.load(file)
    all_films = ""
    for movie, movie_info in films.items():
        all_films += f"{movie_info['title']} -- Year of Release: {movie_info['release_year']} -- Rating: {movie_info['rating']}\n"
    return all_films


def save_movies(updated_movies):
    form_movies_file = json.dumps(updated_movies, indent=4)
    with open("film_database.json", "w") as movies_file:
        movies_file.write(form_movies_file)
        conv_dict = json.loads(form_movies_file)
        return conv_dict


def option_2_movie_adding():
    film_database = "film_database.json"
    add_title = input("Enter title: ").strip()
    add_year = int(input("Enter year: "))
    add_rating = float(input("Enter rating: "))
    movies_database_get = get_movies_from_film_database(film_database)
    movies_database_get[add_title] = {
        "title": add_title,
        "release_year": add_year,
        "rating": add_rating
        }
    mov_dict = save_movies(movies_database_get)
    print("Movie added successfully")
    return mov_dict


def get_original_movie_name(title, movie_dict):
    original_movie_name = ""
    for key in movie_dict.keys():
        if key.lower() == title:
            original_movie_name = key
    return original_movie_name


def option_3_movie_delete():
    film_database = "film_database.json"
    delete_title = input("Enter title: ").strip().lower()
    movies_database_get = get_movies_from_film_database(film_database)
    original_movie_name = get_original_movie_name(delete_title, movies_database_get)
    movies_database_get.pop(original_movie_name)
    save_movies(movies_database_get)
    return None


def option_4_movie_update():
    film_database = "film_database.json"
    update_title = input("Enter title: ").strip().lower()
    release_year = int(input("Enter release year: "))
    update_rating = float(input("Enter rating: "))
    movies_database_get = get_movies_from_film_database(film_database)
    original_movie_name = get_original_movie_name(update_title, movies_database_get)
    movies_database_get[original_movie_name] = {
        "title": original_movie_name,
        "release_year": release_year,
        "rating": update_rating
        }
    save_movies(movies_database_get)
    return None


def option_5_get_stats(dictionary_films):
    if len(dictionary_films) == 0:
        print_info = "\nNo movies in database\n"
        return print_info
    else:
        def get_average():
            val_list = []
            average_rating = 0
            for val in dictionary_films.values():
                rating = val["rating"]
                val_list.append(rating)
                average_rating = statistics.mean(val_list)
            print_average = f"\nThe average rating is: {average_rating:.2f}"
            return print_average
        average_get = get_average()


        def get_median():
            val_list = []
            for val in dictionary_films.values():
                rating = val["rating"]
                val_list.append(rating)
                val_list.sort()
            val_list = val_list[::-1]
            median = len(val_list) // 2
            if len(val_list) % 2 != 0:
                print_med = f"The median value is: {val_list[median]}"
                return print_med, val_list
            else:
                median = len(val_list) // 2
                print_med = f"The median value is: {(val_list[median - 1] + val_list[median]) / 2}"
                return print_med, val_list
        med_value, values_list = get_median()


        def get_best_worst_ratings(list_of_vals):
            highest_rating = max(list_of_vals)
            lowest_rating = min(list_of_vals)
            best_list = []
            worst_list = []
            for value in dictionary_films.values():
                title = value["title"]
                rating = value["rating"]
                if rating == highest_rating:
                    best_list.append(title)
                    best_list.append(rating)
                if rating == lowest_rating:
                    worst_list.append(title)
                    worst_list.append(rating)
            print_info_best = f"Highest Rating {best_list[1]}: movie(s) -> {', '.join(best_list[::2])}"
            print_info_worst = f"Lowest Rating {worst_list[1]}: movie(s) -> {', '.join(worst_list[::2])}\n"
            return print_info_best, print_info_worst
        get_best_movie, get_worst_movie = get_best_worst_ratings(values_list)
        print_info = f"{average_get}\n{med_value}\n{get_best_movie}\n{get_worst_movie}"
        return print_info


def option_6_pick_random_movie(dictionary_films):
    random_item = random.choices(list(dictionary_films.values()))
    display_random_choice = f"Random Choice: {random_item[0]["title"]} from {random_item[0]["release_year"]} rated {random_item[0]["rating"]}."
    return display_random_choice


def option_7_search_movie(dictionary_films):
    dict_lower_keys = {key.lower(): value for key, value in dictionary_films.items()}
    user_input_search_movie = input("\nEnter part of movie name: ").lower()
    print_info = ""
    for movie, movie_info in dict_lower_keys.items():
        if user_input_search_movie in movie:
            print_info += f"\n{movie.title()}: {movie_info["release_year"]} {movie_info["rating"]}"
    return print_info


def option_8_sort_dict_by_rating(dictionary_films):
    print(dictionary_films)
    with open("film_database.json", "r") as file:
        films_database = json.load(file)
    def get_ratings_list(rat_dict):
        ratings_list = []
        for key, val in rat_dict.items():
            ratings_list.append((key, val["rating"]))
        return ratings_list


    def get_rating(tuple_rating):
        return tuple_rating[1]


    def sort_database_rating(tup_list):
        sorted_films_database = {}
        for movie, rating in tup_list:

            sorted_films_database.update({movie: {
                "title": movie,
                "release_year": dictionary_films[movie]["release_year"],
                "rating": rating
            }})
        mov_sav_rat = save_movies(sorted_films_database)
        return mov_sav_rat


    def display_dict_rating(rat_sorted_films):
        return_info = ""
        for movie, details in rat_sorted_films.items():
            return_info += f"{details['title']}: {details['release_year']} {details['rating']}\n"
        return return_info


    def sub_main_rating():
        ratings_list_get = get_ratings_list(films_database)
        sorted_by_rating = sorted(ratings_list_get, key=get_rating, reverse=True)
        database_rating_sort = sort_database_rating(sorted_by_rating)
        dict_rating_display = display_dict_rating(database_rating_sort)
        return dict_rating_display


    if __name__ == "__main__":
        return sub_main_rating()


def option_9_sort_dict_by_year(dictionary_films):
    with open("film_database.json", "r") as file:
        films_database = json.load(file)
    def get_years_list(dict_films):
        year_list = []
        for key, val in dict_films.items():
            year_list.append((val["title"], val["release_year"]))
        return year_list


    def get_year(y_tuple):
        return y_tuple[1]


    def sort_database_year(tuple_list):
        sorted_films_database = {}
        for movie, year in tuple_list:
            sorted_films_database.update({movie: {
                "title": movie,
                "release_year": year,
                "rating": dictionary_films[movie]["rating"]
            }})
        mov_sav_year = save_movies(sorted_films_database)
        return mov_sav_year


    def display_dict_year(years_dict):
        return_info = ""
        for key, val in years_dict.items():
            return_info += f"{val['title']}: {val['release_year']} {val['rating']}\n"
        return return_info


    def sub_main_year():
        year_tuple = get_years_list(films_database)
        sorted_year = sorted(year_tuple, key=get_year)
        dict_year_create = sort_database_year(sorted_year)
        dict_year_display = display_dict_year(dict_year_create)
        return dict_year_display


    if __name__ == "__main__":
        return sub_main_year()


def get_valid_choice(user_prompt, min_val=0, max_val=9):
    while True:
        try:
            user_choice = int(input(user_prompt))
            if min_val <= user_choice <= max_val:
                return user_choice
            else:
                print("Enter valid choice in range (0-9): ")
        except ValueError:
            print("Enter a valid choice in range (0-9): ")


def get_user_input():
    dictionary_films = get_movies_from_film_database("film_database.json")

    user_choice = get_valid_choice("Enter choice in range (0-9): ")
    if user_choice == 0:
        exit()
    elif user_choice == 1:
        print(f"\n{len(dictionary_films)} in the Movie Database\n")
        option_1 = option_1_display_dictionary()
        return option_1
    elif user_choice == 2:
        option_2_movie_adding()
        return None
    elif user_choice == 3:
        option_3_movie_delete()
        return None
    elif user_choice == 4:
        option_4_movie_update()
        return None
    elif user_choice == 5:
        option_5 = option_5_get_stats(dictionary_films)
        return option_5
    elif user_choice == 6:
        option_6 = option_6_pick_random_movie(dictionary_films)
        return option_6
    elif user_choice == 7:
        option_7 = option_7_search_movie(dictionary_films)
        return option_7
    elif user_choice == 8:
        option_8 = option_8_sort_dict_by_rating(dictionary_films)
        return option_8
    elif user_choice == 9:
        option_9 = option_9_sort_dict_by_year(dictionary_films)
        return option_9


def main():
    while True:
        title_database = (
            f"\n{'*' * 10 + ' MY MOVIE DATABASE ' + '*' * 10}"
        )
        menu_database = (
            f"\nMOVIES DATABASE MENU:\n"
            f"0. Exit\n"
            f"1. List Movies\n"
            f"2. Add movie\n"
            f"3. Delete movie\n"
            f"4. Update movie\n"
            f"5. Stats\n"
            f"6. Random movie\n"
            f"7. Search movie\n"
            f"8. Movies sorted by rating\n"
            f"9. Movies sorted by year\n"
        )


        line_header = header(title_database)
        print(line_header)
        list_choices = menu(menu_database)
        print(list_choices)
        user_input_get = get_user_input()
        if user_input_get:
            print(user_input_get)
        input("Press enter to continue: ")


if __name__ == "__main__":
    main()

