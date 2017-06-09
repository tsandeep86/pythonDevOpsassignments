import movies_main
import open_html


ironman=movies_main.movies("Ironman 3",'Tony Stark a billionaier turned super hero tries to save world','https://www.youtube.com/watch?v=NZnlTjDbvdY','http://www.joblo.com/posters/images/full/ironman3-tonysuit-post.jpg')
bahubali2=movies_main.movies("bahubali:The conclusion",'Amarendra bahubali ane nenu','https://www.youtube.com/watch?v=qD-6d8Wo3do','https://i.ytimg.com/vi/z-HSkk4BTw8/maxresdefault.jpg')

movies = [ ironman, bahubali2]

open_html.open_movies_page(movies)