import media
import fresh_tomatoes

# Toy Story (title, storyline, poster URL, trailer URL)
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous "
                        "when a new spaceman figure supplants him as top toy "
                        "in a boy's room.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Tommy Boy
tommy_boy = media.Movie("Tommy Boy",
                        "An incompetent, immature, and dimwitted heir to an"
                        " auto parts factory must save the business to keep "
                        "it out of the hands of his new, con-artist relatives "
                        "and big business.",
                        "http://static2.businessinsider.com/image/52b4700fecad04e52ef848cf-1013-1500/tommy%20boy%20poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=51f2rrYebKo")

# Happy Gilmore
happy_gilmore = media.Movie("Happy Gilmore",
                            "A rejected hockey player puts his skills to the"
                            " golf course to save his grandmother's house.",
                            "http://www.impawards.com/1996/posters/happy_gilmore.jpg", # noqa
                            "https://www.youtube.com/watch?v=-6sT7MSJ4GE")

# Cool Runnings
cool_runnings = media.Movie("Cool Runnings",
                            "When a Jamaican sprinter is disqualified to the "
                            "Olympic Games, he enlists the help of a "
                            "dishonored coach to start the first Jamaican "
                            "Bobsled Team.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxMTQ3MzMwMV5BMl5BanBnXkFtZTgwNTYxNzYxMTE@._V1_.jpg", # noqa
                            "https://www.youtube.com/watch?v=Ob1tnjItuI4")

# Ghostbusters
ghostbusters = media.Movie("Ghostbusters",
                           "Three former parapsychology professors set up shop"
                           " as a unique ghost removal service.",
                           "https://images-na.ssl-images-amazon.com/images/I/417EyUCBJ-L.jpg", # noqa
                           "https://www.youtube.com/watch?v=RYT8ifqLjKA")

# List of movies
movies = [toy_story, avatar, tommy_boy, happy_gilmore, cool_runnings,
          ghostbusters]

# Generate HTML Page
fresh_tomatoes.open_movies_page(movies)
