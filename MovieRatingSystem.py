import tkinter as tk
from tkinter import ttk

class MovieRatingSystem:
    def __init__(self, movies):
        self.movies = {i+1: {"title": movie, "rating": None, "number_of_rating": 0} for i, movie in enumerate(movies)}

    def rate_movie(self):
        window = tk.Tk()
        window.title("Rate a Movie")
        tk.Label(window, text="Select a movie to rate:", font=("Helvetica", 20)).pack()
        for i, movie in self.movies.items():
            ttk.Button(window, text=movie['title'], command=lambda i=i: self.rate_movie_window(i)).pack()
        window.mainloop()

    def rate_movie_window(self, choice):
        window = tk.Toplevel()
        window.title("Rate a Movie")
        title = self.movies[choice]['title']
        tk.Label(window, text=f"Enter the rating for '{title}':").pack()
        rating_entry = tk.Entry(window)
        rating_entry.pack()
        ttk.Button(window, text="Submit", command=lambda: self.submit_rating(choice, rating_entry.get(), window)).pack()

    def submit_rating(self, choice, rating, window):
        rating = float(rating)
        if self.movies[choice]["rating"] is not None:
            self.movies[choice]["rating"] = ((self.movies[choice]["rating"] * self.movies[choice]["number_of_rating"]) + rating) / (self.movies[choice]["number_of_rating"] + 1)
            self.movies[choice]["number_of_rating"] += 1
        else:
            self.movies[choice]["rating"] = rating
            self.movies[choice]["number_of_rating"] += 1
            print(f"Rating of the movie '{self.movies[choice]['title']}' is updated successfully.")
        window.destroy()

    def get_rating(self):
        window = tk.Tk()
        window.title("Get a Movie Rating")
        tk.Label(window, text="Select a movie to get the rating:", font=("Helvetica", 20)).pack()
        for i, movie in self.movies.items():
            ttk.Button(window, text=movie['title'], command=lambda i=i: self.get_rating_window(i)).pack()
        window.mainloop()

    def get_rating_window(self, choice):
        window = tk.Toplevel()
        window.title("Get a Movie Rating")
        title = self.movies[choice]['title']
        if self.movies[choice]["rating"] is not None:
            tk.Label(window, text=f"The rating of the movie '{title}' is {self.movies[choice]['rating']:.2f}").pack()
        else:
            tk.Label(window, text=f"The movie '{title}' has not been rated yet.").pack()

    def run(self):
        window = tk.Tk()
        window.title("Movie Rating System")
        ttk.Button(window, text="Rate a Movie", command=self.rate_movie).pack()
        ttk.Button(window, text="Get a Movie Rating", command=self.get_rating).pack()
        window.mainloop()


movies = ['Animal', 'Hero', 'Dunki']
a = MovieRatingSystem(movies)
a.run()
