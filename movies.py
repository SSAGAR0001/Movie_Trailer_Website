# cook your code here
import fresh_tomatoes
import media
# import urllib
# import json
# Function to get information regarding Movie details like
# title , rating , poster etc.
# Using Info function to get Movie Information
FastFurious8 = media.Movie("Fast And Furious 8",
                           "When a mysterious woman seduces Dom into the" +
                           " world of crime and a betrayal of those" +
                           "closest to him, the crew face trials" +
                           " that will test them as never before.",
                           "http://www.etonline.com/movies/2016/04/24232821/" +
                           "640_furious8_poster.jpg",
                           "https://www.youtube.com/watch?v=uisBaTkQAEs&t=87s")
# print(Fast_&_Furious_8.storyline)

ToyStory = media.Movie("Toy Story",
                       "A cowboy doll is profoundly threatened and jealous" +
                       " when a new spaceman figure" +
                       "supplants him as top toy in a boy's room.",
                       "https://upload.wikimedia.org/wikipedia/" +
                       "en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Toy_Story.show_trailer()

dangal = media.Movie("Dangal",
                     "Biographical sports drama on former wrestler Mahavir" +
                     " Singh Phogat and his two wrestler daughters' struggle" +
                     " towards glory at the Commonwealth Games in the face" +
                     " of societal oppression.",
                     "http://dramas.hdpixelstalk.com/wp-content/uploads/" +
                     "2016/12/23-dec-2016-dangal-poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

IronMan3 = media.Movie("Iron Man 3",
                       "When Tony Stark's world is torn apart by a " +
                       "formidable terrorist called the Mandarin, he starts " +
                       "an odyssey of rebuilding and retribution.",
                       "http://www.impawards.com/2013/posters/iron_man_three" +
                       ".jpg",
                       "https://www.youtube.com/results?search_query=iron" +
                       "+man+3+trailer")

CapAmerica = media.Movie("Captain America - Civil War",
                         "Political interference in the Avengers' activities" +
                         " causes a rift between former allies " +
                         "Captain America and Iron Man.",
                         "http://akns-images.eonline.com/eol_images/" +
                         "Entire_Site/201627/rs_634x940-160307074539-634." +
                         "captain-america-civil-war-poster-chris-evans-" +
                         "robert-downey-jr.3716.jpg",
                         "https://www.youtube.com/watch?v=dKrVegVI0Us")


Batvssup = media.Movie("Batman vs Superman - Dawn of Justice",
                       "Fearing that the actions of Superman are left" +
                       " unchecked, Batman takes on the Man of Steel, while" +
                       " the world wrestles with what kind of a hero it" +
                       " really needs.",
                       "https://s-media-cache-ak0.pinimg.com/736x/43/c9/b1/" +
                       "43c9b1626b559a2d4104c22e61ee490e.jpg",
                       "https://www.youtube.com/watch?v=0WWzgGyAH6Y")


frozen = media.Movie("Frozen",
                     "When the newly crowned Queen Elsa accidentally uses " +
                     "her power to turn things into ice to curse her home in" +
                     " infinite winter, her sister, Anna, teams up with a" +
                     " mountain man, his playful reindeer, and a snowman to" +
                     " change the weather condition.",
                     "http://vignette4.wikia.nocookie.net/disney/images/6/6" +
                     "6/Frozen_castposter.jpg/revision/latest?cb=2014060" +
                     "2183635",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg")


raees = media.Movie("Raees",
                    "Criticizing the prohibition of alcohol, prostitution " +
                    "and illegal drugs in Gujarat, this film unfolds the " +
                    "story of a cruel and clever bootlegger, whose business " +
                    "is highly challenged by a tough cop.",
                    "http://media1.bollywoodhungama.in/wp-content/uploads/" +
                    "2016/03/Raees1-1-306x393.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0")
movies = [FastFurious8, ToyStory, dangal, IronMan3, CapAmerica, Batvssup,
          frozen, raees]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
