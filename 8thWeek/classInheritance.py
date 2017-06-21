import webbrowser

class videos():
    def __init__(self,title,runtime,y_url):
        self.title=title
        self.runtime=runtime
        self.y_url=y_url
        
class movies(videos):
    
    def __init__(self,title,runtime,y_url,story,poster_url):
        

        self.poster_url=poster_url
        videos.__init__(self, title, runtime,y_url)
        
    def open_y_video(self):
        for url in (self.y_url,self.poster_url):
            webbrowser.open_new_tab(url)


class tvshows(videos):
    
    def __init__(self,title,runtime,y_url,episodes,no_seasons):
        
        self.episodes=episodes
        self.no_seasons=no_seasons
        videos.__init__(self, title, runtime,y_url)
        
    def open_y_video(self):
        webbrowser.open_new_tab(self.y_url)
        
    

wonderwoman=movies('wonderwoman',221,'https://www.youtube.com/watch?v=VSB4wGIdDwo','Princess','http://www.joblo.com/movie-posters/2017/wonder-woman#image-33881')

wonderwoman.open_y_video()
print wonderwoman.runtime

daredevil=tvshows('Daredevil',60,'https://www.youtube.com/watch?v=jAy6NJ_D5vU',23,5)

daredevil.open_y_video()
print daredevil.episodes
