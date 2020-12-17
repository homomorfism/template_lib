from django.conf import settings
# Create your views here.
from django.db.models import Q

# Create your views here.
from post.models import Post


def get_posts_by_query(query):
    queryset = []

    queries = query.split(" ")

    for q in queries:
        # Only approved ('1') posts are showing
        # Later check that moderators can see all information
        posts = Post.objects.filter(visibility='1').filter(
            Q(title__icontains=q) |
            Q(author__icontains=q) |
            Q(categories__text=q) |
            Q(description__icontains=q)
        )

        for material in posts:
            queryset.append(material)

    # Delete non unique values, sort it by date of publication
    queryset = sorted(list(set(queryset)), key=lambda post: post.date_publication, reverse=True)

    if settings.DEBUG:
        print(f"Debug: by query: {query} {len(queryset)} objects were found!")

    return queryset
