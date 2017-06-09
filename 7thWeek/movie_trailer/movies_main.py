import webbrowser

class movies():
    
    def __init__(self,title,story,youtube_url,poster_image_url):
        
        self.title=title
        self.story=story
        self.youtube_url=youtube_url
        self.poster_image_url=poster_image_url
        
        
    
    def open_html_video(self):
        
        webbrowser.open(self.youtube_url)