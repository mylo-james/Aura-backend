from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models.users import User
from app.models.follows import Follow
from app.models.likes import Like
from app.models.posts import Post
from app.models.saved_posts import Saved_Post
from app.models.comments import Comment


# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.


with app.app_context():
    db.drop_all()
    db.create_all()

    users = [User(full_name="John Hampton", username="johnH",
                  password="password", email='john@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
    User(full_name="Dave Hampton", username="daveH",
         password="password", email='dave@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
    User(full_name="Bob Hampton", username="BobH",
         password="password", email='Bob@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
    User(full_name="Dan Hampton", username="DanH",
         password="password", email='Dan@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
    User(full_name="Kelly Hampton", username="KellyH",
         password="password", email='Kelly@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
    User(full_name="Bobby Hampton", username="BobbyH",
        password="password", email='Bobby@gmail.com', profile_image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg')]

    follows = [Follow(user_id=1, user_followed_id=2),
               Follow(user_id=2, user_followed_id=3),
               Follow(user_id=2, user_followed_id=4),
               Follow(user_id=2, user_followed_id=1),
               Follow(user_id=2, user_followed_id=5),
               Follow(user_id=2, user_followed_id=6),
               Follow(user_id=3, user_followed_id=1),
               Follow(user_id=3, user_followed_id=2),
               Follow(user_id=4, user_followed_id=2),
               Follow(user_id=5, user_followed_id=2),
               Follow(user_id=6, user_followed_id=2)]

    posts = [Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=2, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=3, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=4, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=5, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=6, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg'),
            Post(user_id=1, caption='A picture of James :)', image_url='https://slickpics.s3.us-east-2.amazonaws.com/IMAGE-1593494929679.jpeg')]

    likes = [Like(user_id=1, likeable_id=1, likeable_type='post'),
             Like(user_id=2, likeable_id=1, likeable_type='post'),
             Like(user_id=3, likeable_id=1, likeable_type='post'),
             Like(user_id=4, likeable_id=1, likeable_type='post'),
             Like(user_id=5, likeable_id=1, likeable_type='post'),
             Like(user_id=6, likeable_id=1, likeable_type='post')]

    saved_posts = [Saved_Post(user_id=1, post_id=1),
                   Saved_Post(user_id=2, post_id=1),
                   Saved_Post(user_id=3, post_id=1),
                   Saved_Post(user_id=4, post_id=1),
                   Saved_Post(user_id=5, post_id=1),
                   Saved_Post(user_id=6, post_id=1)]

    comments = [Comment(user_id=1, post_id=1, content='Wow this post is cool!'),
                Comment(user_id=2, post_id=1, content='Wow this post is cool!'),
                Comment(user_id=3, post_id=1, content='Wow this post is cool!'),
                Comment(user_id=4, post_id=1, content='Wow this post is cool!'),
                Comment(user_id=5, post_id=1, content='Wow this post is cool!'),
                Comment(user_id=6, post_id=1, content='Wow this post is cool!')]

    for user in users:
        db.session.add(user)

    for post in posts:
        db.session.add(post)

    for like in likes:
        db.session.add(like)

    for post in saved_posts:
        db.session.add(post)

    for comment in comments:
        db.session.add(comment)

    for follow in follows:
        db.session.add(follow)

    db.session.commit()
