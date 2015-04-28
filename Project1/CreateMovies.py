import movie
import fresh_tomatoes

class Main():
    # Create instances of movie object in Movie class
    DilWaleDulhaniyaLejayeinge = movie.Movie("Dil Wale Dulhaniya Lejayeinge","https://image.tmdb.org/t/p/original/pVGzV02qmHVoKx9ehBNy7m2u5fs.jpg","http://www.youtube.com/watch?v=1U9SpwJ9TCs", "A block buster in 1990's");
    Lagaan = movie.Movie("Lagaan","http://media.movietalkies.com/posters/bollywood/movies/2001/lagaan/lagaan-2001-4b.jpg","http://www.youtube.com/watch?v=FNX1beRgwJ8","A must-watch for Amir Khan fans");
    TwoStates = movie.Movie("Two States","https://pbs.twimg.com/profile_images/438944211245617152/cDjvFT3A.jpeg","http://www.youtube.com/watch?v=CGyAaR2aWcA","The best depiction between North Indian culture and South Indian culture");
    ThreeIdiots = movie.Movie("Three Idiots","http://media1.santabanta.com/full1/Bollywood%20Movies/3%20Idiots/3-idiots-20h.jpg","http://www.youtube.com/watch?v=CGyAaR2aWcA","A must watch for Amir Khan fans");

    # Create a list of movies instantiated above
    movies_list = [DilWaleDulhaniyaLejayeinge,Lagaan,TwoStates,ThreeIdiots];

    fresh_tomatoes.open_movies_page(movies_list);
    
