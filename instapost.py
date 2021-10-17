import instaloader
from instaloader import Profile, Post

instance = instaloader.Instaloader()
post = Post.from_shortcode(instance.context,  "CU24OjsPaNA")



instance.download_post(post,target="instadploader")