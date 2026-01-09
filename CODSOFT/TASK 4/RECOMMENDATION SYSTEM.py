def recommend(preference):
    preference = preference.lower()

    if preference == "action":
        return ["Avengers", "Mission Impossible", "John Wick"]

    elif preference == "comedy":
        return ["3 Idiots", "PK", "Hera Pheri"]

    elif preference == "romance":
        return ["Titanic", "Dilwale Dulhania Le Jayenge", "Notebook"]

    elif preference == "technology":
        return ["AI Basics", "Python Programming", "Data Science Handbook"]

    else:
        return ["No recommendation available"]


# Main Program
user_choice = input("Enter your preference (action/comedy/romance/technology): ")
suggestions = recommend(user_choice)

print("Recommended items:")
for item in suggestions:
    print("-", item)