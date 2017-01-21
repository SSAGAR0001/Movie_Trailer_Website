# Movie_Trailer_Website
Introduction

This is a server-side code written in Python scripting to store the list of one's favorite movies including box art imagery and a movie trailer URL(imported from YouTube).
We can serve this data as a webpage and allow the visitors so as to review the movies and watch the trailer of the movie.

Steps to open the website

1) Unzip the file to a specific folder.
2) OPen the file name fresh_tomatoes.html so as to view the website.

Standard Python Libraries Used:

1) webbrowser :  he webbrowser module provides a high-level interface to allow displaying Web-based documents to users. Under most circumstances, simply calling the open() function from this module will do the right thing.

How to Add Your Favorite Movie

This code is written in Python.

Open movies.py using python IDLE.

Call the get_info method with your favorite movie name to view it.
 
Add the title, Storyline, Poster URL and Youtube URL of the movie as arguments in Movie class contructor in media.py file.
For example: IronMan3 = media.Movie("Iron Man 3",
                        "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.",
                        "http://www.impawards.com/2013/posters/iron_man_three.jpg",
                        "https://www.youtube.com/results?search_query=iron+man+3+trailer")

Add this object in the movies list at the end of the file and Run the module.

That's It! You can enjoy your favourite list of movies on the webite!

Changes Made:

Style:
a. Changed the Background

body {
          padding-top: 80px;
          background-image: url("11.jpg");
      }
