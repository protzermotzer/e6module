import json
import requests
from PIL import Image
from io import BytesIO

class e6Im():
    def __init__(self, datalist):
        try:
            if list(datalist.keys())[0] == 'posts':
                datalist = datalist['posts']
        except:
            pass
        
        self.approver_id = datalist['approver_id']
        self.change_seq = datalist['change_seq']
        self.comment_count = datalist['comment_count']
        self.created_at = datalist['created_at']
        self.description = datalist['description']
        self.fav_count = datalist['fav_count']
        
        self.file = file_details(datalist['file'])
        
        self.flags = flags(datalist['flags'])
        
        self.id = datalist['id']
        self.is_favorited = datalist['is_favorited']
        self.locked_tags = datalist['locked_tags']
        self.pools = datalist['pools']
        self.preview = preview(datalist['preview'])
        
        self.rating = datalist['rating']
        self.relationships = relationships(datalist['relationships'])
        
        self.sample = sample(datalist['sample'])
        
        self.score = score(datalist['score'])

        self.sources = datalist['sources']
        
        self.tags = tags(datalist['tags'])
        
        
        self.species = datalist['tags']['species']
        self.updated_at = datalist['updated_at']
        self.uploader_id = datalist['uploader_id']
    
    
class file_details():
    def __init__(self, filelist):
        self.ext = filelist['ext']
        self.height = filelist['height']
        self.md5 = filelist['md5']
        self.size = filelist['size']
        self.url = filelist['url']
        self.width = filelist['width']

class flags():
    def __init__(self, flaglist):
        self.deleted = flaglist['deleted']
        self.flagged = flaglist['flagged']
        self.note_locked = flaglist['note_locked']
        self.pending = flaglist['pending']
        self.rating_locked = flaglist['rating_locked']
        self.status_locked = flaglist['status_locked']
        
class preview():
    def __init__(self, previewlist):
        self.height = previewlist['height']
        self.url = previewlist['url']
        self.width = previewlist['width']
        
class relationships():
    def __init__(self, rellist):
        self.children = rellist['children']
        self.has_active_children= rellist['has_active_children']
        self.has_children= rellist['has_children']
        self.parent_id= rellist['parent_id']
        
class sample():
    def __init__(self, samplelist):
        self.has = samplelist['has']
        self.height = samplelist['height']
        self.url = samplelist['url']
        self.width = samplelist['width']
        
class score():
    def __init__(self, scorelist):
        self.down = scorelist['down']
        self.total = scorelist['total']
        self.up = scorelist['up']
        
class tags():
    def __init__(self, taglist):
        self.artist = taglist['artist']
        self.character = taglist['character']
        self.copyright = taglist['copyright']
        self.general = taglist['general']
        self.invalid = taglist['invalid']
        self.lore = taglist['lore']
        self.meta = taglist['meta']
        self.species = taglist['species']
        self.all = self.artist + self.character + self.copyright + self.general + self.invalid + self.lore + self.meta + self.species
    
def getposts(tags, limit=10):
    headers = {"User-agent" : "MyProject/1.0 (By WibbleTime on e621)"}
    e621String = "https://e621.net/posts.json?tags={0}&limit={1}".format(tags, limit)    
    response = requests.get(e621String, headers = headers)
    response = response.json()
    return response

def to_pil(link):
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    return img
