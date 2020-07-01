#e6module
A python module to neaten up the e621 api process 

## Warning
*Be aware that e621.net only allows 2 requests per *

## Required Modules
- PIL
- json
- requests

## Functions

`esix.getposts(tags, limit=10)` returns dictionary  
`tags`: String of tags you wish to search for  
`limit`: Amount of images you wish to recieve (Hard limit of 230)  

`esix.to_pil(link)` returns PIL Image object  
`link`: Link to be converted to PIL  

`esix.e6Im(datalist)` returns e6Im object  
`datalist`: Dictionary to be parsed  
*Please note that when you recieve the api data, it will be in `{posts: [foobar, barbaz, foobaz]}` format.*  
*This function only takes one dictionary of data as input (e.g. `esix.e6Im(foobar)`, `esix.e6Im(barbaz)`, so be aware of this.*  

## esix.e6Im functions

- `approver_id`
- `change_seq`
- `comment_count`
- `created_at`
- `description`
- `fav_count`
  
- `file`
  - `ext`
  - `height`
  - `md5`
  - `size`
  - `url`
  - `width`
  
- `flags`
  - `deleted`
  - `flagged`
  - `note_locked`
  - `pending`
  - `rating_locked`
  - `status_locked`
  
- `id`
- `is_favorited`
- `locked_tags`
- `pools`
  
- `preview`
  - `height`
  - `url`
  - `width`

- `rating`
  
- `relationships`
  - `children`
  - `has_active`
  - `has_children`
  - `parent_id`
  
- `sample`
  - `has`
  - `height`
  - `url`
  - `width`
  
- `score`
  - `down`
  - `total`
  - `up`
  
- `sources`

- `tags`
  - `artist`
  - `character`
  - `copyright`
  - `general`
  - `invalid`
  - `lore`
  - `meta`
  - `species`
  - `all`
    
- `updated_at`
- `uploader_id`
