def getrelatedposts(posts_dict, label):
    """
    posts_dict: excludes solved posts
    """
    relatedposts_dict={}
    nbr = 5
    larger_nbr = 10

    posts = posts_dict[label][:nbr]#get latest 5 posts

    # if 5th post and 6th post are in the same time period
    if posts[-1].id.match(posts_dict[label][nbr].id):
        following_posts = posts_dict[label][:larger_nbr]

        index = furtherestSimilarPosts(posts[-1], following_posts)
        posts = posts_dict[label][:index+1]

        posts = sorted(posts, key=lambda post: post.user.upvotes, reverse=True)[:nbr]

    relatedposts_dict[label] = posts

    return relatedposts_dict

class User:
    def __init__(self,
                 id,
                 keywords_list,
                 posts_helped,
                 posts_posted,
                 upvotes
                 ):
        self.id = id #string
        self.keywords = keywords_list #list of key words
        self.posts_helped = posts_helped ## solved or not
        self.posts_posted = posts_posted
        self.upvotes = upvotes #int

    def getpostsrelatedtohelpedposts(self, posts_dict):
        result_dict={}
        for post in self.posts_helped:
            for label in post.keywords:
                result_dict.update(getrelatedposts(posts_dict, label))
        return result_dict

    def getpostsrelatedtokeywords(self,posts_dict):
        result_dict = {}
        for label in self.keywords:
            result_dict = getrelatedposts(posts_dict, label)
        return result_dict

    def getfilteredposts(self, posts_dict):
        result_dict = self.getpostsrelatedtohelpedposts(posts_dict)
        result_dict.update(self.getpostsrelatedtokeywords())

        return result_dict

def furtherestSimilarPosts(post, similar_posts):
    """
    requirements: make sure posts in following_posts are ordered by their dates, lastest with small index
    :param following_posts: 10 latest posts in the same topic with last_post
    :return: index of the furthest close post
    """
    index = 0
    similar_posts = sorted(similar_posts, key= lambda post:post.id, reverse=True)
    for index, post in enumerate(similar_posts):
        if not post.id.match(post.id[:4]):
            break
    return index


class Post:
    def __init__(self,
                 date,
                 data_last_time_update,
                 keywords_list,
                 status,
                 user):
        self.id = date #string
        self.update = data_last_time_update
        self.keywords = keywords_list #list of key words
        #self.status = status ## solved or not
        self.helpee = user







